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
  // Statement-y keywords — collapse simple plurals where the rewrite is the same
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
export function activate() {}
export function deactivate() {}
export function isActive() { return false; }
