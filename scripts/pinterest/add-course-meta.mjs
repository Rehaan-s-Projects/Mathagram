// scripts/pinterest/add-course-meta.mjs
// Inject Rich Pin / SEO metadata into course index.html files. Idempotent.
// Usage (from repo root):
//   node scripts/pinterest/add-course-meta.mjs --dry-run
//   node scripts/pinterest/add-course-meta.mjs --only=algebra,calculus
//   node scripts/pinterest/add-course-meta.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { listCourseSlugs, getCourseData } from './lib/course-data.mjs';
import { buildMetaBlock, META_START, META_END } from './lib/meta-block.mjs';
import { injectBlock } from './lib/inject.mjs';

const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const onlyArg = args.find((a) => a.startsWith('--only='));
const only = onlyArg ? onlyArg.slice('--only='.length).split(',').filter(Boolean) : null;

const slugs = only ?? listCourseSlugs();
let changed = 0;
let unchanged = 0;
const failed = [];

for (const slug of slugs) {
  const path = `courses/${slug}/index.html`;
  try {
    const before = readFileSync(path, 'utf8');
    const block = buildMetaBlock(getCourseData(slug));
    const after = injectBlock(before, block, {
      start: META_START, end: META_END, before: '</head>',
    });
    if (after === before) { unchanged++; continue; }
    changed++;
    if (dryRun) console.log(`would update ${path}`);
    else writeFileSync(path, after);
  } catch (err) {
    failed.push(`${slug}: ${err.message}`);
  }
}

console.log(`${dryRun ? '[dry-run] ' : ''}changed=${changed} unchanged=${unchanged} failed=${failed.length}`);
for (const f of failed) console.log(`  FAIL ${f}`);
if (failed.length) process.exitCode = 1;
