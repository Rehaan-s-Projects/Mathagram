import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  extractTitle, extractDescription, extractCategory, truncate,
  listCourseSlugs, getCourseData,
} from '../../scripts/pinterest/lib/course-data.mjs';

const SAMPLE = `<!DOCTYPE html><html><head><title>x</title></head><body>
  <header class="course-header">
    <span class="course-badge" style="background:var(--color-math)">Math</span>
    <h1>Algebra</h1>
    <p>The ultimate algebra course &amp; more. 1312 lessons across 60 units.</p>
  </header>
</body></html>`;

test('extractTitle pulls the h1 and decodes entities', () => {
  assert.equal(extractTitle(SAMPLE), 'Algebra');
  assert.equal(extractTitle('<h1>Cantor&#39;s Set &amp; Co</h1>'), "Cantor's Set & Co");
});

test('extractDescription pulls the course-header paragraph and decodes entities', () => {
  assert.equal(
    extractDescription(SAMPLE),
    'The ultimate algebra course & more. 1312 lessons across 60 units.'
  );
});

test('extractDescription returns empty string when no course-header exists', () => {
  assert.equal(extractDescription('<html><body><p>nope</p></body></html>'), '');
});

test('extractCategory pulls the badge text', () => {
  assert.equal(extractCategory(SAMPLE), 'Math');
});

test('truncate leaves short strings untouched', () => {
  assert.equal(truncate('short', 160), 'short');
});

test('truncate breaks on a word boundary and appends an ellipsis', () => {
  const out = truncate('alpha beta gamma delta epsilon', 20);
  assert.ok(out.length <= 20, `got length ${out.length}`);
  assert.ok(out.endsWith('…'));
  assert.ok(!out.includes('  '));
  assert.ok('alpha beta gamma delta epsilon'.startsWith(out.slice(0, -1)));
});

test('listCourseSlugs finds real courses and is sorted', () => {
  const slugs = listCourseSlugs();
  assert.ok(slugs.length > 300, `expected 300+ slugs, got ${slugs.length}`);
  assert.ok(slugs.includes('algebra'));
  assert.ok(slugs.includes('calculus'));
  assert.deepEqual(slugs, [...slugs].sort());
});

test('getCourseData reads a real course end to end', () => {
  const c = getCourseData('algebra');
  assert.equal(c.slug, 'algebra');
  assert.equal(c.title, 'Algebra');
  assert.equal(c.category, 'Math');
  assert.equal(c.url, 'https://mathagram.org/courses/algebra/');
  assert.ok(c.totalLessons > 100, `expected many lessons, got ${c.totalLessons}`);
  assert.ok(c.unitCount > 10, `expected many units, got ${c.unitCount}`);
  assert.ok(c.description.length > 20);
  assert.ok(c.description.length <= 160);
});

test('getCourseData still yields metadata when the unit array cannot be parsed', () => {
  // set-theory is one of the 61 courses extract-units.mjs cannot parse.
  const c = getCourseData('set-theory');
  assert.ok(c.title.length > 0, 'title must survive an unparseable unit array');
  assert.ok(c.description.length > 0, 'description must survive');
  assert.equal(c.url, 'https://mathagram.org/courses/set-theory/');
  assert.equal(c.totalLessons, null);
  assert.equal(c.unitCount, null);
});

test('every course in the catalog yields a title and description', () => {
  const missing = [];
  for (const slug of listCourseSlugs()) {
    const c = getCourseData(slug);
    if (!c.title || !c.description) missing.push(slug);
  }
  assert.deepEqual(missing, [], `courses missing title/description: ${missing.join(', ')}`);
});
