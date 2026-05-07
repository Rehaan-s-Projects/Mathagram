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

export function applyMathMap(text) { return text; }
export function activate() {}
export function deactivate() {}
export function isActive() { return false; }
