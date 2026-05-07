// js/python-translate.js
// Python translation mode — client-side text transform.
// Replaces real-language translation with a deterministic English→Python
// rewrite for prose words and math expressions.

// Order matters: longer/multi-word phrases must come before their shorter
// constituents so we don't half-rewrite them. (Multi-word patterns land in Task 4.)
const wordMap = [
  // Multi-word phrases — must run before their shorter constituents
  [/\bfor each ([a-zA-Z_]\w*) in ([a-zA-Z_]\w*)\b/gi, 'for $1 in $2'],
  [/\bif (.+?) then (.+)$/gi, 'if $1: $2'],
  [/\bis equal to\b/gi, '=='],
  [/\b(?:is )?not equal\b/gi, '!='],
  [/\bequals\b/gi, '=='],
  [/\brange from (-?\d+) to (-?\d+)\b/gi, 'range($1, $2)'],
  [/\blambda function\b/gi, 'lambda'],
  [/\blength of\b/gi, 'len() of'],
  [/\binherits? from\b/gi, '(parent)'],
  [/\biterate over\b/gi, 'for ... in'],
  // Boolean/None constants — case-sensitive when reasonable
  [/\btrue\b/g, 'True'],
  [/\bfalse\b/g, 'False'],
  [/\bnothing\b/gi, 'None'],
  [/\bnull\b/gi, 'None'],
  // Type names
  [/\bdictionar(?:y|ies)\b/gi, 'dict'],
  [/\bfunctions?\b/g, 'def'],
  [/\blists?\b/g, 'list'],
  [/\bsets?\b/g, 'set'],
  [/\btuples?\b/g, 'tuple'],
  [/\bclass(?:es)?\b/g, 'class'],
  // Statement-y keywords — only entries that actually transform.
  // (return/print/lambda map to themselves in Python, so they're skipped.)
  [/\bimports?\b/g, 'import'],
];

export function applyWordMap(text) {
  let out = text;
  for (const [re, rep] of wordMap) out = out.replace(re, rep);
  return out;
}

// ─── Math expression rewrites ────────────────────────────────────────
const SUPER = { '⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','ⁿ':'n' };

// True if the string looks like it contains math: an `=` in an equation-like
// position, an `f(x)`, a digit-letter juxtaposition, a Unicode superscript,
// or a LaTeX delimiter. Conservative: false positives in prose are worse than
// false negatives in math.
function isMathy(text) {
  return /=|f\(x\)|\d[a-zA-Z]|[⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ]|\\\(|\\\)|\$\$|\\sqrt|\\frac/.test(text);
}

// Rewrite a math expression. Order matters:
//   1. \sqrt{} and \frac{} (LaTeX functions) before bare-symbol rewrites
//   2. f(x) = expr → def f(x): return expr (consumes the `=`)
//   3. Unicode superscripts → **n
//   4. digit-letter juxtaposition → digit*letter
//   5. single `=` → `==`
function rewriteMath(s) {
  return s
    .replace(/\\sqrt\{(.+?)\}/g, 'math.sqrt($1)')
    .replace(/\\frac\{(.+?)\}\{(.+?)\}/g, '($1)/($2)')
    .replace(/f\(x\)\s*=\s*(.+?)$/g, 'def f(x): return $1')
    .replace(/([a-zA-Z\)])([⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ]+)/g, (_, base, exp) => {
      const digits = [...exp].map(c => SUPER[c] || c).join('');
      return `${base}**${digits}`;
    })
    .replace(/(\d+)([a-zA-Z])/g, '$1*$2')
    .replace(/(?<![=!<>])=(?!=)/g, '==');
}

export function applyMathMap(text) {
  if (!isMathy(text)) return text;
  // Process LaTeX-delimited segments first, dropping their wrappers.
  let out = text
    .replace(/\\\((.+?)\\\)/g, (_, inner) => rewriteMath(inner))
    .replace(/\$\$(.+?)\$\$/g, (_, inner) => rewriteMath(inner));
  // Then apply math rewrites to the whole string for unwrapped expressions.
  // rewriteMath is idempotent for matches it has already processed.
  out = rewriteMath(out);
  return out;
}

// ─── DOM walker ──────────────────────────────────────────────────────
const SKIP_TAGS = new Set(['SCRIPT', 'STYLE', 'CODE', 'PRE', 'TEXTAREA', 'INPUT']);

const _originalsText = new WeakMap();

const _originalsAttr = new WeakMap();

const ATTR_NAMES = ['placeholder', 'title', 'aria-label'];

function isInDataNoPy(el) {
  let p = el;
  while (p) {
    if (p.hasAttribute && p.hasAttribute('data-no-py')) return true;
    p = p.parentElement;
  }
  return false;
}

function walkAttributes(root) {
  if (!root || root.nodeType !== 1 && !root.querySelectorAll) return;
  const elements = [];
  if (root.nodeType === 1 && ATTR_NAMES.some(a => root.hasAttribute(a))) elements.push(root);
  if (root.querySelectorAll) {
    elements.push(...root.querySelectorAll(ATTR_NAMES.map(a => `[${a}]`).join(',')));
  }
  for (const el of elements) {
    if (isInDataNoPy(el)) continue;
    let backup = _originalsAttr.get(el);
    if (!backup) { backup = new Map(); _originalsAttr.set(el, backup); }
    for (const attr of ATTR_NAMES) {
      const cur = el.getAttribute(attr);
      if (cur == null) continue;
      if (!backup.has(attr)) backup.set(attr, cur);
      try {
        const next = transformText(backup.get(attr));
        if (cur !== next) el.setAttribute(attr, next);
      } catch (e) {
        console.warn('python-translate: attr transform failed', e);
      }
    }
  }
}

function shouldSkip(node) {
  let el = node.parentElement;
  while (el) {
    if (SKIP_TAGS.has(el.tagName)) return true;
    if (el.isContentEditable) return true;
    if (el.hasAttribute && el.hasAttribute('data-no-py')) return true;
    el = el.parentElement;
  }
  return false;
}

function transformText(t) {
  return applyMathMap(applyWordMap(t));
}

function walkAndTransform(root) {
  if (!root) return;
  const start = root.nodeType === 3 ? root.parentNode : root;
  if (!start) return;
  const tw = document.createTreeWalker(start, NodeFilter.SHOW_TEXT, {
    acceptNode: (n) => shouldSkip(n) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
  });
  let node;
  while ((node = tw.nextNode())) {
    if (!_originalsText.has(node)) _originalsText.set(node, node.textContent);
    try {
      const original = _originalsText.get(node);
      const next = transformText(original);
      if (node.textContent !== next) node.textContent = next;
    } catch (e) {
      console.warn('python-translate: text transform failed', e);
    }
  }
  walkAttributes(start);
}

// Exposed for tests; not part of the stable API.
export const _walkAndTransform = walkAndTransform;

// ─── Activation ──────────────────────────────────────────────────────
let _active = false;
let _observer = null;
let _applying = false;
let _pending = [];
let _pendingTimer = null;

function installObserver() {
  if (_observer) return;
  _observer = new MutationObserver((records) => {
    if (_applying) return;
    for (const r of records) {
      if (r.type === 'characterData') _pending.push(r.target);
      else for (const n of r.addedNodes) _pending.push(n);
    }
    if (_pendingTimer) clearTimeout(_pendingTimer);
    _pendingTimer = setTimeout(flushPending, 50);
  });
  _observer.observe(document.body, { childList: true, subtree: true, characterData: true });
}

function uninstallObserver() {
  if (_observer) { _observer.disconnect(); _observer = null; }
  if (_pendingTimer) { clearTimeout(_pendingTimer); _pendingTimer = null; }
  _pending = [];
}

function flushPending() {
  _pendingTimer = null;
  const batch = _pending; _pending = [];
  _applying = true;
  try {
    for (const n of batch) {
      if (!n || !n.isConnected) continue;
      walkAndTransform(n);
    }
  } finally {
    queueMicrotask(() => { _applying = false; });
  }
}

function restoreSubtree(root) {
  if (!root) return;
  const start = root.nodeType === 3 ? root.parentNode : root;
  if (!start) return;
  // Restore text nodes
  const tw = document.createTreeWalker(start, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    const orig = _originalsText.get(n);
    if (orig != null) { n.textContent = orig; _originalsText.delete(n); }
  }
  // Restore attributes
  const attrEls = start.nodeType === 1 ? [start] : [];
  if (start.querySelectorAll) attrEls.push(...start.querySelectorAll('*'));
  for (const el of attrEls) {
    const backup = _originalsAttr.get(el);
    if (!backup) continue;
    for (const [k, v] of backup) el.setAttribute(k, v);
    _originalsAttr.delete(el);
  }
}

export function activate() {
  if (_active) return;
  if (!document.body) { requestAnimationFrame(activate); return; }
  _active = true;
  _applying = true;
  try { walkAndTransform(document.body); }
  finally { queueMicrotask(() => { _applying = false; }); }
  installObserver();
}

export function deactivate() {
  uninstallObserver();
  if (document.body) {
    _applying = true;
    try { restoreSubtree(document.body); }
    finally { queueMicrotask(() => { _applying = false; }); }
  }
  _active = false;
}

export function isActive() { return _active; }

// Exposed for tests; not part of the stable API.
export const _restoreSubtree = restoreSubtree;
