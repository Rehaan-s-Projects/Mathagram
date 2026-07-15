// Deterministically shuffle each quiz question's choices and update `correct`,
// so the right answer isn't almost-always at index 0. Pure local transform —
// no LLM/API cost. Re-serializes each course's quizzes.js as valid JS.
// Usage: node shuffle-choices.mjs <slug1> <slug2> ...
import { readFileSync, writeFileSync, existsSync } from 'node:fs';

const ROOT = '/Users/dakotabrown/rehan-calculus-local/courses';

// mulberry32 seeded PRNG for reproducible shuffles
function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function hash(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); }
  return h >>> 0;
}

const slugs = process.argv.slice(2);
let changed = 0, skipped = 0;

for (const slug of slugs) {
  const path = `${ROOT}/${slug}/quizzes.js`;
  if (!existsSync(path)) { console.log(`SKIP ${slug}: no quizzes.js`); skipped++; continue; }
  let mod;
  try { mod = await import(`file://${path}?t=${hash(slug)}`); }
  catch (e) { console.log(`SKIP ${slug}: parse fail (${e.message})`); skipped++; continue; }
  const bank = mod.QUIZ_BANK;
  if (!bank || typeof bank !== 'object') { console.log(`SKIP ${slug}: no QUIZ_BANK`); skipped++; continue; }

  for (const unit of Object.keys(bank)) {
    const arr = bank[unit];
    if (!Array.isArray(arr)) continue;
    arr.forEach((q, qi) => {
      if (!Array.isArray(q.choices) || q.choices.length !== 4 || typeof q.correct !== 'number') return;
      const correctText = q.choices[q.correct];
      const rand = rng(hash(`${unit}:${qi}:${q.q}`));
      // Fisher-Yates
      const c = q.choices.slice();
      for (let i = c.length - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        [c[i], c[j]] = [c[j], c[i]];
      }
      q.choices = c;
      q.correct = c.indexOf(correctText);
    });
  }

  // Re-serialize as valid JS (JSON strings are valid JS literals)
  const units = Object.keys(bank).map(Number).sort((a, b) => a - b);
  let out = `// ${slug} — quiz question bank, keyed by unit number. Choices shuffled for answer-position balance.\nexport const QUIZ_BANK = {\n`;
  for (const u of units) {
    out += `  ${u}: [\n`;
    for (const q of bank[u]) {
      out += `    ${JSON.stringify({ q: q.q, choices: q.choices, correct: q.correct, why: q.why })},\n`;
    }
    out += `  ],\n`;
  }
  out += `};\n`;
  writeFileSync(path, out);
  changed++;
  console.log(`OK   ${slug}: ${units.length} units shuffled`);
}
console.log(`\nDONE: ${changed} rewritten, ${skipped} skipped`);
