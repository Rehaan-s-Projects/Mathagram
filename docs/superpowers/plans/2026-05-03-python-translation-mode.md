# Python Translation Mode Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Mathagram's Google Translate-driven translation system with a single client-side Python mode that toggles English ↔ Python via a deterministic text transform.

**Architecture:** A new `js/python-translate.js` ES module owns the transform engine: two ordered regex tables (prose words, math expressions), a `TreeWalker`-based DOM walker with `WeakMap` backups for restore, and a debounced `MutationObserver` for dynamic content. `js/nav.js` is gutted of Google Translate code (language list, widget loader, proxy fallback, course-grid resort) and rewritten to expose a two-entry mode picker (English / 🐍 Python). `index.html`'s "translation besties" reveal logic is removed.

**Tech Stack:** Vanilla ES modules. No bundler, no test framework. Tests run as a manual HTML page (`js/python-translate.test.html`) opened via `python3 -m http.server`.

**Spec:** `docs/superpowers/specs/2026-05-03-python-translation-mode-design.md`

---

## File Structure

| File | Action |
|---|---|
| `js/python-translate.js` | CREATE — transform engine (~250 LOC) |
| `js/python-translate.test.html` | CREATE — fixture-based browser test runner |
| `js/nav.js` | MODIFY — delete ~280 lines of Google Translate code, add ~80 lines for mode picker |
| `index.html` | MODIFY — remove translation-besties HTML and script (~85 lines) |

---

## Test runner conventions

All tasks use the same test runner. To "run tests":

```bash
cd /Users/dakotabrown/rehan-calculus-local
python3 -m http.server 8000
# In browser: http://localhost:8000/js/python-translate.test.html
```

The page auto-runs all fixtures and shows green/red rows. "Expected: PASS" means all rows green. "Expected: FAIL" means specified rows red.

---

## Task 1: Create test runner skeleton with first failing fixture

**Files:**
- Create: `js/python-translate.test.html`

- [ ] **Step 1: Write the failing test**

Create `js/python-translate.test.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>python-translate tests</title>
  <style>
    body { font-family: monospace; padding: 16px; }
    .row { padding: 6px 8px; margin: 2px 0; border-radius: 4px; }
    .pass { background: #d1fae5; color: #064e3b; }
    .fail { background: #fee2e2; color: #7f1d1d; }
    .label { font-weight: 700; }
    pre { display: inline; margin: 0; }
  </style>
</head>
<body>
  <h1>python-translate tests</h1>
  <div id="results"></div>

  <script type="module">
    import * as PT from './python-translate.js';

    const results = document.getElementById('results');
    let passed = 0, failed = 0;

    function eq(name, actual, expected) {
      const ok = actual === expected;
      const row = document.createElement('div');
      row.className = 'row ' + (ok ? 'pass' : 'fail');
      row.innerHTML = `<span class="label">${ok ? 'PASS' : 'FAIL'}</span> ${name} — got: <pre>${escape(String(actual))}</pre>${ok ? '' : ' / want: <pre>' + escape(String(expected)) + '</pre>'}`;
      results.appendChild(row);
      ok ? passed++ : failed++;
    }
    function escape(s) { return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }

    // ─── Fixtures ─────────────────────────────────────────────────────
    eq('word: function → def',
       PT.applyWordMap('a function returns'),
       'a def returns');

    // Summary row
    const summary = document.createElement('div');
    summary.style.cssText = 'margin-top:16px; padding:10px; font-weight:700; border-top:2px solid #333;';
    summary.textContent = `${passed} passed, ${failed} failed`;
    results.appendChild(summary);
  </script>
</body>
</html>
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/dakotabrown/rehan-calculus-local
python3 -m http.server 8000 &
```

Open `http://localhost:8000/js/python-translate.test.html`.

Expected: page shows a JS error in the console (`Failed to fetch dynamically imported module: python-translate.js`) — the module doesn't exist yet. Results div is empty or shows the import error.

- [ ] **Step 3: Commit**

```bash
git add js/python-translate.test.html
git commit -m "Add python-translate test runner skeleton"
```

---

## Task 2: Stub the engine module so the test page loads

**Files:**
- Create: `js/python-translate.js`

- [ ] **Step 1: Write the stub**

Create `js/python-translate.js`:

```js
// js/python-translate.js
// Python translation mode — client-side text transform.
// Replaces real-language translation with a deterministic English→Python
// rewrite for prose words and math expressions.

export function applyWordMap(text) { return text; }
export function applyMathMap(text) { return text; }
export function activate() {}
export function deactivate() {}
export function isActive() { return false; }
```

- [ ] **Step 2: Run test to verify it loads but fails behavior**

Reload `http://localhost:8000/js/python-translate.test.html`.

Expected: 1 red FAIL row — `word: function → def` got `a function returns`, want `a def returns`. No console errors.

- [ ] **Step 3: Commit**

```bash
git add js/python-translate.js
git commit -m "Stub python-translate module exports"
```

---

## Task 3: Implement applyWordMap with single-word substitutions

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add new failing fixtures**

In `js/python-translate.test.html`, after the existing `eq('word: function → def', ...)` line, insert:

```js
    eq('word: True/False/None',
       PT.applyWordMap('It is true and not false, returning nothing.'),
       'It is True and not False, returning None.');
    eq('word: list/dict/set/tuple',
       PT.applyWordMap('use a list, a dictionary, a set, or a tuple'),
       'use a list, a dict, a set, or a tuple');
    eq('word: return/print/import',
       PT.applyWordMap('return the value, print it, then import math'),
       'return the value, print it, then import math');
    eq('word: class',
       PT.applyWordMap('Define a class with two classes inside'),
       'Define a class with two class inside');
```

Reload page. Expected: 5 FAIL rows.

- [ ] **Step 2: Implement wordMap**

Replace the body of `js/python-translate.js` with:

```js
// js/python-translate.js
// Python translation mode — client-side text transform.
// Replaces real-language translation with a deterministic English→Python
// rewrite for prose words and math expressions.

// Order matters: longer/multi-word phrases must come before their shorter
// constituents so we don't half-rewrite them. (Multi-word patterns land in Task 4.)
const wordMap = [
  // Boolean/None constants — case-sensitive when reasonable
  [/\btrue\b/g, 'True'],
  [/\bfalse\b/g, 'False'],
  [/\bnothing\b/gi, 'None'],
  [/\bnull\b/gi, 'None'],
  // Type names
  [/\bdictionary\b/gi, 'dict'],
  [/\bdictionaries\b/gi, 'dict'],
  [/\bfunctions?\b/g, 'def'],
  [/\blists?\b/g, 'list'],
  [/\bsets?\b/g, 'set'],
  [/\btuples?\b/g, 'tuple'],
  [/\bclass(?:es)?\b/g, 'class'],
  // Statement-y keywords (singular forms only — avoid pluralizing)
  [/\breturn\b/g, 'return'],
  [/\bprint\b/g, 'print'],
  [/\bimports?\b/g, 'import'],
  [/\blambda\b/g, 'lambda'],
];

export function applyWordMap(text) {
  let out = text;
  for (const [re, rep] of wordMap) out = out.replace(re, rep);
  return out;
}

export function applyMathMap(text) { return text; }
export function activate() {}
export function deactivate() {}
export function isActive() { return false; }
```

- [ ] **Step 3: Run test to verify it passes**

Reload page.
Expected: 5 PASS rows for the new fixtures + 1 PASS for the original `function → def` fixture.

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Implement applyWordMap single-word substitutions"
```

---

## Task 4: Add multi-word patterns to applyWordMap

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing fixtures**

In `js/python-translate.test.html`, after the previous fixtures, insert:

```js
    eq('multiword: for each X in Y',
       PT.applyWordMap('for each item in items'),
       'for item in items');
    eq('multiword: if X then Y',
       PT.applyWordMap('if x is positive then return x.'),
       'if x is positive: return x.');
    eq('multiword: equals / is equal to / not equal',
       PT.applyWordMap('A equals B; C is equal to D; E is not equal'),
       'A == B; C == D; E != ');
    eq('multiword: range from A to B',
       PT.applyWordMap('iterate range from 0 to 10'),
       'iterate range(0, 10)');
    eq('multiword: lambda function',
       PT.applyWordMap('a lambda function maps x to x+1'),
       'a lambda maps x to x+1');
    eq('multiword: length of',
       PT.applyWordMap('the length of items'),
       'the len() of items');
    eq('multiword: inherits from',
       PT.applyWordMap('Cat inherits from Animal'),
       'Cat (parent) Animal');
```

Reload. Expected: 7 FAIL rows.

- [ ] **Step 2: Add multi-word patterns to wordMap**

In `js/python-translate.js`, prepend the following entries to the **start** of the `wordMap` array (multi-word must run before the single-word entries):

```js
  // Multi-word phrases — must run before their shorter constituents
  [/\bfor each ([a-zA-Z_]\w*) in ([a-zA-Z_]\w*)\b/gi, 'for $1 in $2'],
  [/\bif (.+?) then (.+)$/gi, 'if $1: $2'],
  [/\bis equal to\b/gi, '=='],
  [/\bnot equal\b/gi, '!='],
  [/\bequals\b/gi, '=='],
  [/\brange from (-?\d+) to (-?\d+)\b/gi, 'range($1, $2)'],
  [/\blambda function\b/gi, 'lambda'],
  [/\blength of\b/gi, 'len() of'],
  [/\binherits? from\b/gi, '(parent)'],
  [/\biterate over\b/gi, 'for ... in'],
```

The final `wordMap` literal should look like:

```js
const wordMap = [
  // Multi-word phrases — must run before their shorter constituents
  [/\bfor each ([a-zA-Z_]\w*) in ([a-zA-Z_]\w*)\b/gi, 'for $1 in $2'],
  [/\bif (.+?) then (.+)$/gi, 'if $1: $2'],
  [/\bis equal to\b/gi, '=='],
  [/\bnot equal\b/gi, '!='],
  [/\bequals\b/gi, '=='],
  [/\brange from (-?\d+) to (-?\d+)\b/gi, 'range($1, $2)'],
  [/\blambda function\b/gi, 'lambda'],
  [/\blength of\b/gi, 'len() of'],
  [/\binherits? from\b/gi, '(parent)'],
  [/\biterate over\b/gi, 'for ... in'],
  // Boolean/None constants
  [/\btrue\b/g, 'True'],
  [/\bfalse\b/g, 'False'],
  [/\bnothing\b/gi, 'None'],
  [/\bnull\b/gi, 'None'],
  // Type names
  [/\bdictionary\b/gi, 'dict'],
  [/\bdictionaries\b/gi, 'dict'],
  [/\bfunctions?\b/g, 'def'],
  [/\blists?\b/g, 'list'],
  [/\bsets?\b/g, 'set'],
  [/\btuples?\b/g, 'tuple'],
  [/\bclass(?:es)?\b/g, 'class'],
  // Statement-y keywords
  [/\breturn\b/g, 'return'],
  [/\bprint\b/g, 'print'],
  [/\bimports?\b/g, 'import'],
  [/\blambda\b/g, 'lambda'],
];
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: all 12 rows PASS.

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Add multi-word patterns to applyWordMap"
```

---

## Task 5: Implement applyMathMap with math-context guard

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing fixtures**

In `js/python-translate.test.html`, after the previous fixtures, insert:

```js
    eq('math: Unicode superscript x²',
       PT.applyMathMap('x² + 1'),
       'x**2 + 1');
    eq('math: implicit multiplication 2x',
       PT.applyMathMap('2x + 3 == 7'),
       '2*x + 3 == 7');
    eq('math: f(x) = x²',
       PT.applyMathMap('f(x) = x²'),
       'def f(x): return x**2');
    eq('math: \\sqrt{x}',
       PT.applyMathMap('\\sqrt{x} + 1 = y'),
       'math.sqrt(x) + 1 == y');
    eq('math: \\frac{a}{b}',
       PT.applyMathMap('\\frac{a}{b} = c'),
       '(a)/(b) == c');
    eq('math: LaTeX delimiters strip',
       PT.applyMathMap('compute \\(x² + 1\\) here'),
       'compute x**2 + 1 here');
    eq('math: prose untouched',
       PT.applyMathMap('this is just plain prose with no math'),
       'this is just plain prose with no math');
    eq('math: equals only inside math context',
       PT.applyMathMap('Tom equals Jerry'),
       'Tom equals Jerry'); // no math signal — applyMathMap should leave it alone
```

Reload. Expected: 8 new FAIL rows (except the "prose untouched" one — that already passes since current `applyMathMap` is identity).

- [ ] **Step 2: Implement applyMathMap and isMathy**

In `js/python-translate.js`, replace `export function applyMathMap(text) { return text; }` with:

```js
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
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: all rows PASS (existing 12 + 8 new = 20).

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Implement applyMathMap with isMathy guard"
```

---

## Task 6: Implement DOM walker with WeakMap text-node backup

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing DOM fixtures**

In `js/python-translate.test.html`, just before the summary row block (`const summary = ...`), insert a DOM-test block:

```js
    // ─── DOM walker fixtures ──────────────────────────────────────────
    function makeFixture(html) {
      const host = document.createElement('div');
      host.style.display = 'none';
      host.innerHTML = html;
      document.body.appendChild(host);
      return host;
    }
    function eqText(name, host, expected) {
      // textContent collapses whitespace from nested elements; compare directly.
      eq(name, host.textContent.trim().replace(/\s+/g, ' '), expected);
    }

    {
      const host = makeFixture('<p>The function returns true.</p>');
      PT._walkAndTransform(host);
      eqText('walker: simple paragraph', host, 'The def returns True.');
    }
    {
      const host = makeFixture('<p>Use <code>function</code> in code.</p>');
      PT._walkAndTransform(host);
      eqText('walker: skips <code>', host, 'Use function in code.');
    }
    {
      const host = makeFixture('<div data-no-py><p>function</p></div>');
      PT._walkAndTransform(host);
      eqText('walker: skips data-no-py subtree', host, 'function');
    }
    {
      const host = makeFixture('<p>x²</p><script>function bar(){}</script>');
      PT._walkAndTransform(host);
      eqText('walker: skips <script>', host, 'x**2 function bar(){}');
    }
```

Reload. Expected: 4 FAIL rows (`PT._walkAndTransform is not a function`).

- [ ] **Step 2: Implement walker**

In `js/python-translate.js`, append (after `applyMathMap` definition, before `activate/deactivate/isActive`):

```js
// ─── DOM walker ──────────────────────────────────────────────────────
const SKIP_TAGS = new Set(['SCRIPT', 'STYLE', 'CODE', 'PRE', 'TEXTAREA', 'INPUT']);

const _originalsText = new WeakMap();

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
}

// Exposed for tests; not part of the stable API.
export const _walkAndTransform = walkAndTransform;
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: all rows PASS (20 + 4 new = 24).

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Implement DOM walker with skip-ancestor and WeakMap backup"
```

---

## Task 7: Implement attribute walker (placeholder/title/aria-label)

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing fixtures**

In the test page's DOM block, append:

```js
    {
      const host = makeFixture('<input type="text" placeholder="enter a function">');
      PT._walkAndTransform(host);
      eq('attr: placeholder rewritten',
         host.querySelector('input').getAttribute('placeholder'),
         'enter a def');
    }
    {
      const host = makeFixture('<button aria-label="return value" title="prints true">x</button>');
      PT._walkAndTransform(host);
      const btn = host.querySelector('button');
      eq('attr: aria-label rewritten', btn.getAttribute('aria-label'), 'return value');
      eq('attr: title rewritten', btn.getAttribute('title'), 'prints True');
    }
    {
      const host = makeFixture('<div data-no-py><input placeholder="function"></div>');
      PT._walkAndTransform(host);
      eq('attr: skips data-no-py',
         host.querySelector('input').getAttribute('placeholder'),
         'function');
    }
```

Reload. Expected: 4 new FAIL rows (`null` because attr walker not yet implemented).

- [ ] **Step 2: Add attribute walker**

In `js/python-translate.js`, add this `_originalsAttr` map and `walkAttributes` function near `_originalsText`:

```js
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
```

Then update `walkAndTransform` to also call `walkAttributes`:

Replace this block in `walkAndTransform`:

```js
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
}
```

with:

```js
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
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: all rows PASS (24 + 4 new = 28).

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Add attribute walker for placeholder/title/aria-label"
```

---

## Task 8: Implement activate / deactivate with round-trip restore

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing round-trip fixture**

In the test page's DOM block, append:

```js
    {
      // Build a fixture into a real container so deactivate's full-body walk
      // still finds the nodes.
      const host = makeFixture('<p>The function returns true.</p><input placeholder="enter function">');
      // Activate restricted to host by calling _walkAndTransform; then call
      // a public restore on the host alone via _restoreSubtree.
      PT._walkAndTransform(host);
      eq('round-trip: text transformed',
         host.querySelector('p').textContent, 'The def returns True.');
      eq('round-trip: attr transformed',
         host.querySelector('input').getAttribute('placeholder'), 'enter def');
      PT._restoreSubtree(host);
      eq('round-trip: text restored',
         host.querySelector('p').textContent, 'The function returns true.');
      eq('round-trip: attr restored',
         host.querySelector('input').getAttribute('placeholder'), 'enter function');
    }
    {
      // Public activate/deactivate end-to-end against document.body — but
      // scope reasoning to a marker node we can find before/after.
      const host = makeFixture('<p id="rt-marker">use a list and a set</p>');
      PT.activate();
      eq('activate: isActive() === true', PT.isActive(), true);
      eq('activate: text transformed',
         document.getElementById('rt-marker').textContent, 'use a list and a set'); // no change since `list`→`list`, `set`→`set`
      // Use a phrase that DOES change to verify
      host.querySelector('#rt-marker').textContent = 'a function returns true';
      // Force a re-walk by calling _walkAndTransform on host (Mutation observer
      // is implemented in Task 9; for now use the helper).
      PT._walkAndTransform(host);
      eq('activate: re-walk transforms updated text',
         document.getElementById('rt-marker').textContent, 'a def returns True');
      PT.deactivate();
      eq('deactivate: isActive() === false', PT.isActive(), false);
      eq('deactivate: text restored',
         document.getElementById('rt-marker').textContent, 'a function returns true');
    }
```

Reload. Expected: round-trip rows FAIL (`_restoreSubtree` undefined; activate/deactivate are no-ops).

- [ ] **Step 2: Implement activate, deactivate, and a subtree-restore helper**

In `js/python-translate.js`, replace the no-op `activate`, `deactivate`, `isActive` with:

```js
// ─── Activation ──────────────────────────────────────────────────────
let _active = false;

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
  walkAndTransform(document.body);
}

export function deactivate() {
  if (!_active && !document.body) return;
  if (document.body) restoreSubtree(document.body);
  _active = false;
}

export function isActive() { return _active; }

// Exposed for tests; not part of the stable API.
export const _restoreSubtree = restoreSubtree;
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: all rows PASS.

(If you see a stale FAIL from earlier `host.textContent` rows referencing `function`, it's because `activate()` walked `document.body` and rewrote them. That's expected. Make sure subsequent fixtures are scoped to fresh `makeFixture` hosts, and that any direct `document.querySelector(...)` reads happen *after* the relevant `activate`/`deactivate` step.)

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Implement activate/deactivate with round-trip restore"
```

---

## Task 9: Implement MutationObserver with debounce and feedback-loop guard

**Files:**
- Modify: `js/python-translate.js`
- Modify: `js/python-translate.test.html`

- [ ] **Step 1: Add failing fixture**

In the test page's DOM block, append:

```js
    // MutationObserver: nodes added after activate() should auto-transform.
    await new Promise(async (resolve) => {
      // Ensure clean state
      if (PT.isActive()) PT.deactivate();
      const host = makeFixture('<div id="mo-host"></div>');
      PT.activate();
      // Inject new node after activation
      const p = document.createElement('p');
      p.id = 'mo-target';
      p.textContent = 'a function returns true';
      host.querySelector('#mo-host').appendChild(p);
      // Wait past the observer's ~50ms debounce
      setTimeout(() => {
        eq('observer: dynamically added node transformed',
           document.getElementById('mo-target').textContent,
           'a def returns True');
        PT.deactivate();
        resolve();
      }, 150);
    });
```

Note: this fixture uses `await`, so the fixture body needs to live inside an async function. Refactor the existing test page as follows — keep all prior fixture lines (`eq(...)` and the DOM blocks from Tasks 1–8) intact, just wrap them in an async IIFE:

1. In `js/python-translate.test.html`, locate the line `let passed = 0, failed = 0;`. Everything from the next line down to (but not including) the summary block currently runs at module top level.
2. Wrap that fixture region in `(async () => { ... })();`.
3. Move the summary block (`const summary = ...; results.appendChild(summary);`) inside the async IIFE so it runs after all fixtures resolve.
4. Append the new observer fixture (the `await new Promise(...)` block above) just before the summary block, inside the IIFE.

Final structure of the script body:

```js
import * as PT from './python-translate.js';
const results = document.getElementById('results');
let passed = 0, failed = 0;
function eq(name, actual, expected) { /* unchanged */ }
function escape(s) { /* unchanged */ }

(async () => {
  // -- Existing fixtures (Tasks 1–8) verbatim, in order --

  // -- New observer fixture (this task) --
  await new Promise(async (resolve) => {
    if (PT.isActive()) PT.deactivate();
    const host = makeFixture('<div id="mo-host"></div>');
    PT.activate();
    const p = document.createElement('p');
    p.id = 'mo-target';
    p.textContent = 'a function returns true';
    host.querySelector('#mo-host').appendChild(p);
    setTimeout(() => {
      eq('observer: dynamically added node transformed',
         document.getElementById('mo-target').textContent,
         'a def returns True');
      PT.deactivate();
      resolve();
    }, 150);
  });

  const summary = document.createElement('div');
  summary.style.cssText = 'margin-top:16px; padding:10px; font-weight:700; border-top:2px solid #333;';
  summary.textContent = `${passed} passed, ${failed} failed`;
  results.appendChild(summary);
})();
```

Reload. Expected: observer row FAILs (the `function`/`true` are not auto-transformed because no observer is active).

- [ ] **Step 2: Implement the observer**

In `js/python-translate.js`, add module-private state and observer logic. After the `let _active = false;` line, add:

```js
let _observer = null;
let _applying = false;
let _pending = [];
let _pendingTimer = null;
```

Add this `installObserver` and `uninstallObserver` near the bottom (above the `export` lines if any are still there):

```js
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
```

Update `activate()` and `deactivate()`:

Replace:

```js
export function activate() {
  if (_active) return;
  if (!document.body) { requestAnimationFrame(activate); return; }
  _active = true;
  walkAndTransform(document.body);
}

export function deactivate() {
  if (!_active && !document.body) return;
  if (document.body) restoreSubtree(document.body);
  _active = false;
}
```

with:

```js
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
```

- [ ] **Step 3: Run test to verify it passes**

Reload. Expected: observer row PASSES.

- [ ] **Step 4: Commit**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Add MutationObserver with debounce and feedback-loop guard"
```

---

## Task 10: Delete Google Translate code from js/nav.js

**Files:**
- Modify: `js/nav.js`

This task is pure deletion. After it, `nav.js` no longer references Google Translate, but the dropdown is broken (no entries). Task 11 rebuilds the dropdown. Commit between the two so the deletion is reviewable on its own.

- [ ] **Step 1: Delete the proxy detection block in `initNav`**

In `js/nav.js`, find this block (around lines 35-50):

```js
  // Suppress Google Translate's banner/toolbar (both the in-place widget's
  // and the .translate.goog proxy's). Must run on every page, not just when
  // the in-place widget loads, because the proxy injects its own toolbar.
  injectGoogleTranslateSuppressionStyles();

  // Add Google Translate widget
  addTranslateWidget();

  // If we landed on the .translate.goog proxy, the page is already being
  // translated by Google's proxy — run the courses-grid resort once on load
  // so tiles end up in the translated locale's alphabetical order.
  if (location.hostname.endsWith('.translate.goog') && document.querySelector('.courses-grid')) {
    const m = location.search.match(/[?&]_x_tr_tl=([^&]+)/);
    const targetLang = m ? decodeURIComponent(m[1]) : 'en';
    scheduleResortAfterTranslation(targetLang);
  }
```

Replace with:

```js
  // Add Translate widget (English / 🐍 Python toggle)
  addTranslateWidget();
```

- [ ] **Step 2: Delete `injectGoogleTranslateSuppressionStyles`, `loadGoogleTranslateElement`, `translatePage`, `scheduleResortAfterTranslation`, `sortCourseTilesByTranslatedTitle`**

In `js/nav.js`, find and delete the entire range from:

```js
function injectGoogleTranslateSuppressionStyles() {
```

through the last closing `}` of `sortCourseTilesByTranslatedTitle` (currently line 456). After deletion, the file ends at the closing `}` of `addTranslateWidget` (which Task 11 will rewrite).

Also delete the module-private state used by these functions, currently around lines 263 and 405:

```js
let _googTransPromise = null;
```

```js
let _resortTimer = null;
let _resortObserver = null;
```

- [ ] **Step 3: Verify file still parses**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --check js/nav.js
```

Expected: no output (clean parse). If there's an error like "unexpected token," scan for orphaned helpers or trailing code.

- [ ] **Step 4: Confirm no remaining references**

```bash
grep -nE 'googtrans|translate\.goog|loadGoogleTranslate|scheduleResort|sortCourseTilesByTranslated|injectGoogleTranslate|_googTransPromise|_resortObserver|_resortTimer' js/nav.js
```

Expected: no matches.

- [ ] **Step 5: Commit**

```bash
git add js/nav.js
git commit -m "Remove Google Translate widget, proxy fallback, and course-grid resort from nav.js"
```

---

## Task 11: Replace dropdown with English / 🐍 Python mode picker

**Files:**
- Modify: `js/nav.js`

- [ ] **Step 1: Rewrite `addTranslateWidget`**

In `js/nav.js`, replace the entire `addTranslateWidget` function (currently from `function addTranslateWidget() {` through its closing `}`) with:

```js
function addTranslateWidget() {
  if (document.getElementById('translate-btn')) return;
  const navLinks = document.querySelector('.nav-links');
  if (!navLinks) return;

  // Translate button
  const btn = document.createElement('button');
  btn.id = 'translate-btn';
  btn.title = 'Translate';
  btn.setAttribute('aria-label', 'Translate page');
  btn.style.cssText = 'background:none; border:none; cursor:pointer; padding:4px 8px; font-size:1.2rem; color:var(--color-text-secondary); transition:color 0.2s; display:flex; align-items:center; gap:4px;';
  btn.innerHTML = '<span style="font-size:1.1rem;">&#127760;</span><span style="font-size:0.75rem; font-weight:600;">Translate</span>';

  // Dropdown — marked data-no-py so its own copy never gets rewritten
  const dropdown = document.createElement('div');
  dropdown.id = 'translate-dropdown';
  dropdown.setAttribute('data-no-py', '');
  dropdown.style.cssText = 'display:none; position:absolute; top:100%; right:0; background:var(--color-white); border:1px solid var(--color-border); border-radius:var(--radius); box-shadow:var(--shadow-lg); z-index:999; min-width:240px; flex-direction:column;';

  // Mascot header — Lingo & Babel, your translation guides
  const mascotHeader = document.createElement('div');
  mascotHeader.style.cssText = 'display:flex; align-items:center; gap:10px; padding:12px 14px 10px; background:linear-gradient(135deg,#1FA45C 0%,#FFD93D 50%,#FF6B6B 100%); color:#fff; border-radius:var(--radius) var(--radius) 0 0;';
  mascotHeader.innerHTML = `
    <div style="display:flex; gap:-8px;">
      <img src="/assets/characters/lingo.svg" alt="Lingo the Parrot" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15);" onerror="this.style.display='none'">
      <img src="/assets/characters/babel.svg" alt="Babel the Owl" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15); margin-left:-10px;" onerror="this.style.display='none'">
    </div>
    <div style="flex:1; min-width:0;">
      <div style="font-weight:800; font-size:0.85rem; line-height:1.2;">Lingo &amp; Babel</div>
      <div style="font-size:0.7rem; opacity:0.95; line-height:1.2;">Your translation guides — English or Python!</div>
    </div>`;
  dropdown.appendChild(mascotHeader);

  // Mode list
  const list = document.createElement('div');
  list.style.cssText = 'padding:6px 0;';
  dropdown.appendChild(list);

  function makeEntry(label, mode) {
    const item = document.createElement('button');
    item.style.cssText = 'display:block; width:100%; text-align:left; padding:10px 16px; border:none; background:none; cursor:pointer; font-size:0.9rem; font-family:inherit; color:var(--color-text); transition:background 0.15s;';
    item.textContent = label;
    item.addEventListener('mouseenter', () => { item.style.background = 'var(--color-bg)'; });
    item.addEventListener('mouseleave', () => { item.style.background = 'none'; });
    item.addEventListener('click', () => {
      setMode(mode);
      dropdown.style.display = 'none';
    });
    return item;
  }
  list.appendChild(makeEntry('English', 'en'));
  list.appendChild(makeEntry('🐍 Python', 'py'));

  // Wrapper for positioning
  const wrapper = document.createElement('div');
  wrapper.style.cssText = 'position:relative; display:flex; align-items:center;';
  wrapper.appendChild(btn);
  wrapper.appendChild(dropdown);

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = dropdown.style.display === 'flex';
    dropdown.style.display = isOpen ? 'none' : 'flex';
  });
  document.addEventListener('click', () => { dropdown.style.display = 'none'; });

  navLinks.insertBefore(wrapper, navLinks.firstChild);
}

async function setMode(mode) {
  if (mode === 'py') {
    localStorage.setItem('mathagram-mode', 'py');
    try {
      const m = await import('./python-translate.js');
      m.activate();
    } catch (err) {
      console.warn('python-translate import failed:', err);
    }
  } else {
    localStorage.removeItem('mathagram-mode');
    try {
      const m = await import('./python-translate.js');
      m.deactivate();
    } catch (err) {
      console.warn('python-translate import failed:', err);
    }
  }
}
```

- [ ] **Step 2: Auto-activate on page load if localStorage says so**

In `js/nav.js`, inside `initNav`, just after the line `addTranslateWidget();`, add:

```js
  // Restore Python mode across navigations
  if (typeof localStorage !== 'undefined' && localStorage.getItem('mathagram-mode') === 'py') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoActivatePython);
    } else {
      autoActivatePython();
    }
  }
```

And add the helper function near `setMode`:

```js
function autoActivatePython() {
  import('./python-translate.js').then(m => m.activate()).catch(err => {
    console.warn('python-translate import failed:', err);
  });
}
```

- [ ] **Step 3: Verify nav.js parses**

```bash
node --check js/nav.js
```

Expected: no output.

- [ ] **Step 4: Smoke-test in browser**

```bash
# (server is still running from earlier; if not, run python3 -m http.server 8000)
```

Open `http://localhost:8000/index.html`. Click the 🌐 Translate button. Expected:
- Dropdown opens with Lingo & Babel header showing copy "Your translation guides — English or Python!"
- Two entries below: "English" and "🐍 Python"
- Click "🐍 Python" → page text transforms (e.g., "Mathagram" stays, but words like "function/true/false" if present become def/True/False; the "8 characters with unique voices guide you through every lesson" line becomes "8 character with unique voices guide you through every lesson" because `class(es)`→`class` matches plurals — that's the joke).
- Click 🌐 again, then "English" → original text restored.
- Reload page → still in Python mode (localStorage).
- In English mode, reload → English.

Note any rough edges in the dictionary (phrases that read awkwardly) — they're tunable in `js/python-translate.js`'s `wordMap`.

- [ ] **Step 5: Commit**

```bash
git add js/nav.js
git commit -m "Replace nav dropdown with English / Python mode picker"
```

---

## Task 12: Remove translation-besties from index.html

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Delete the besties HTML block**

In `index.html`, find lines around 197–210:

```html
      <!-- Translation besties — Lingo & Babel — only revealed when the
           page is being viewed through Google Translate (non-English). -->
      <div class="learning-bestie" style="display:none; ...">
        <img src="assets/characters/lingo.svg" ...>
        ...
      </div>
      <div class="learning-bestie" style="display:none; ...">
        <img src="assets/characters/babel.svg" ...>
        ...
      </div>
```

Delete the HTML comment plus both `<div class="learning-bestie">...</div>` blocks. The line just above (the `<div>` for Gosia at lines 191–196) and the closing `</div>` at line 211 (`</div></section>` — the grid wrapper) should bracket the deletion cleanly.

- [ ] **Step 2: Delete the besties `<script>` block**

In `index.html`, find the `<script>` starting around line 214 (`Reveal the two translation besties (Lingo & Babel)...`) through its closing `</script>` (around line 280). Delete the entire script tag and its contents.

- [ ] **Step 3: Confirm no remaining references**

```bash
grep -nE 'translation.?bestie|learning-bestie|isTranslated|googtrans' index.html
```

Expected: no matches.

- [ ] **Step 4: Smoke-test**

Open `http://localhost:8000/index.html`. Expected:
- "8 characters with unique voices guide you through every lesson" subtitle (the original static copy at line 147) is shown.
- The character grid shows 8 characters; no Lingo/Babel entries appear.
- No JS errors in console.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "Remove translation-besties reveal logic from homepage"
```

---

## Task 13: Final smoke checklist + dictionary tuning

**Files:** none modified by default; tune `js/python-translate.js` `wordMap` if a phrase reads awkwardly during smoke.

- [ ] **Step 1: Run the full smoke checklist**

For each item, note pass/fail in the commit message if you tune anything; otherwise just confirm:

1. Homepage in English: looks identical to pre-change (minus the dropdown's language list and the besties grid spots).
2. Homepage in Python mode: tile titles transform; courses-grid still renders; no console errors.
3. Courses page (`/courses.html`) in Python mode: course names transform; toggle back to English restores cleanly.
4. Calculus course page (`/course/calculus/index.html`) in Python mode: unit/lesson titles transform; learning-path zigzag still draws; no console errors.
5. A calculus lesson with math (e.g., `/course/calculus/lesson-1.html`): math expressions in the lesson body transform; LaTeX-wrapped equations transform inside the delimiters.
6. Toggle on → off → on (3 cycles): each cycle restores or re-transforms cleanly.
7. Reload page after activating: page comes up already in Python mode.
8. Lingo & Babel mascot header in the dropdown: copy text is NOT rewritten ("Your translation guides — English or Python!" stays literal).
9. Dropdown items "English" / "🐍 Python": labels not rewritten (under `[data-no-py]`).
10. Network tab on page load (English mode): no requests to `translate.google.com`.
11. After clicking English, reload: localStorage entry `mathagram-mode` is gone.

- [ ] **Step 2: Tune the dictionary if needed**

If any specific phrase reads awkwardly (e.g., a multi-word substitution mangles a sentence), edit `wordMap` in `js/python-translate.js` and re-test. Add a fixture to `js/python-translate.test.html` for the case so the regression is caught next time.

- [ ] **Step 3: Confirm tests still all pass**

Reload `http://localhost:8000/js/python-translate.test.html`. Expected: 0 failed.

- [ ] **Step 4: Commit any tuning changes**

```bash
git add js/python-translate.js js/python-translate.test.html
git commit -m "Tune Python translation dictionary based on smoke test"
```

(If no tuning was needed, skip this commit.)

---

## Done — what's next

After all 13 tasks land:
- The Translate button in nav opens a 2-entry dropdown (English / 🐍 Python).
- Python mode rewrites visible page text via deterministic regex tables.
- Mode persists across navigations.
- Google Translate code, language list, proxy fallback, and translation-besties are gone.
- A manual fixture-based test page (`js/python-translate.test.html`) covers the engine.

**Deploy reminder (from project memory):** mathagram.org publishes via direct Netlify upload, NOT `git push`. If the user asks to deploy, follow the team's existing Netlify deploy workflow (and watch out for the `.netlify/v1` / `.netlify/netlify.toml` / `functions-internal` cleanup gotcha noted in the user's memory).
