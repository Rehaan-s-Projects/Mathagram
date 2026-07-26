// Extract course quiz-metadata from a course index.html, regardless of format.
// Handles both the tuple format (`const units = [[u,"Name",[titles...]],...]`)
// and the unitNames.map format (`const unitNames=[...]; const units = unitNames.map(...)`).
// Usage: node extract-units.mjs <slug>   → prints JSON meta to stdout.
import { readFileSync } from 'fs';

export function extractMeta(slug) {
  const path = `courses/${slug}/index.html`;
  const html = readFileSync(path, 'utf8');

  // course display name from <h1>
  const h1 = (html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || [, ''])[1]
    .replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&#39;/g, "'").trim();

  // id prefix from lessons.push({ id: '<prefix>'+n ...})
  const idPrefix = (html.match(/id:\s*'([a-z0-9-]+)'\s*\+\s*n/i) || [, ''])[1];

  // Grab the code that builds `units`. Start at the earliest of `const unitNames`
  // or `const units`, end just before the lessons loop (`let n` / `const lessons`).
  const startNames = html.indexOf('const unitNames');
  const startUnits = html.indexOf('const units');
  let start = startUnits;
  if (startNames !== -1 && (startNames < startUnits || startUnits === -1)) start = startNames;
  if (start === -1) throw new Error('no unit definition found in ' + path);

  // end marker: first of these after start
  const ends = ['let n = 0', 'let n=0', 'const lessons = []', 'const lessons=[]']
    .map(m => html.indexOf(m, start)).filter(i => i !== -1);
  const end = Math.min(...ends);
  if (!isFinite(end)) throw new Error('no lessons-loop marker after units in ' + path);

  const snippet = html.slice(start, end);

  // Evaluate the snippet in a minimal sandbox to obtain the `units` array.
  // The snippet only references array/string literals + .map; safe to eval here.
  let units;
  try {
    units = eval(`(function(){ ${snippet}; return units; })()`);
  } catch (e) {
    throw new Error('eval of units snippet failed for ' + slug + ': ' + e.message);
  }

  if (!Array.isArray(units) || !units.length) throw new Error('units empty for ' + slug);

  const unitNames = units.map(u => u[1]);
  const lessonsPerUnit = units.map(u => u[2].length);

  return {
    slug,
    courseName: h1,
    idPrefix,
    totalUnits: units.length,
    lessonsPerUnit,
    unitNames,
    uniform: lessonsPerUnit.every(c => c === lessonsPerUnit[0]),
  };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const slug = process.argv[2];
  if (!slug) { console.error('usage: node extract-units.mjs <slug>'); process.exit(1); }
  console.log(JSON.stringify(extractMeta(slug), null, 2));
}
