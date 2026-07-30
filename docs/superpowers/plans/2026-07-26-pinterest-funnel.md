# Pinterest Growth Funnel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an organic acquisition funnel — Pinterest → mathagram.org course page → click-to-play YouTube embed + email capture — so discovery traffic produces legitimate, monetizable YouTube watch time and a durable email list.

**Architecture:** Build-time Node scripts inject metadata and generate pin images into the static site; browser-side ES modules mount the video facade and subscribe form on course pages. Pure functions live in small `lib/` modules unit-tested with `node --test`; the CLI wrappers and image rasterization are verified by explicit shell assertions.

**Tech Stack:** Node 22.17.1 (built-in `node:test` / `node:assert` — no package.json, no dependencies), `rsvg-convert` 2.61.3 for SVG→PNG, Firebase JS SDK 10.12.0 from the gstatic CDN, Firestore, Netlify CLI, GA4.

**Spec:** `docs/superpowers/specs/2026-07-26-pinterest-funnel-design.md`

## Global Constraints

Every task's requirements implicitly include this section.

- **CSP lives in `_headers`, never in a `<meta>` tag.** A meta CSP is inherited by translate.goog and breaks translated views. Both the `/*.html` and `/` blocks must be kept in sync.
- **No test framework exists and none is added.** Tests are `node --test` with `node:assert/strict`. There is no `package.json`; do not create one.
- **Use the glob form for `node --test`, not a directory.** `node --test tests/pinterest/` fails on this Node build; `node --test 'tests/pinterest/*.test.mjs'` works. Quote the glob so Node expands it rather than the shell.
- **Another session works in this repo concurrently.** Stage narrowly and explicitly — `git add courses/*/index.html`, never `git add courses/` or `git add -A` — or you will absorb someone else's in-progress work into your commit. Never stage `.claude/scheduled_tasks.lock`.
- **Xcode polls this repo with `git status`**, intermittently holding `.git/index.lock`. On "Unable to create index.lock", wait two seconds and retry. Never delete the lock file.
- **All Node scripts run from the repo root** (`/Users/dakotabrown/rehan-calculus-local`). `extractMeta()` resolves `courses/<slug>/index.html` relative to `process.cwd()`. A prior `cd` in the same shell session will break this — always `cd` to the repo root first.
- **`rsvg-convert` cannot use web fonts and cannot wrap text.** Templates declare `font-family="Verdana, 'DejaVu Sans', sans-serif"` (matching `assets/lighthouse/og-card.svg`) and the generator emits one `<tspan>` per line.
- **Brand values**, taken from `assets/lighthouse/og-card.svg`: background gradient `#141a2e` → `#0c1020`; teal gradient `#00e5c8` → `#22d3ee`; heading text `#ffffff`; body text `#cbd5e1`; muted text `#64748b`.
- **No autoplay on page load.** The video facade adds `autoplay=1` *only* inside the click handler, where playback is user-initiated. A page-load autoplay or hidden embed risks views being filtered as invalid.
- **GA4 measurement ID is `G-1JKG4MN6XX`.** The old `G-Z7TFRFQDQJ` property is dead and inaccessible.
- **Email copy addresses parents, teachers, and learners 13+.** This matches `privacy.html` §10, which already requires parental consent for ages 11–12 and restricts Learning Post to 13+. Never place the subscribe form inside a kid-facing lesson flow.
- **Injected HTML blocks are delimited and idempotent.** Re-running any injection script must produce an empty `git diff`.
- **Deploying is a 5-path clean + absolute `--dir`.** See Task 15. `git push` does not publish mathagram.org. **The user performs the Netlify deploy, not the implementer.** The Firestore rules deploy (Task 12) is controller-authorized.
- **`scripts/quiz-buildout/extract-units.mjs` is off-limits.** It is shared with the ongoing quiz-buildout campaign. It cannot parse 61 of 341 courses' unit arrays; this plan works around that with nullable counts (Task 1) rather than editing it.

## File Structure

**New — build-time (Node, run from repo root)**

| File | Responsibility |
|---|---|
| `scripts/pinterest/lib/course-data.mjs` | Read a course page → normalized course record. Wraps `extractMeta()`. |
| `scripts/pinterest/lib/meta-block.mjs` | Pure: course record → delimited `<head>` meta HTML, and → `<body>` pin element. |
| `scripts/pinterest/lib/inject.mjs` | Pure: idempotent delimited-block insertion/replacement in an HTML string. |
| `scripts/pinterest/lib/wrap-text.mjs` | Pure: greedy line-breaking for SVG `<tspan>` output. |
| `scripts/pinterest/add-course-meta.mjs` | CLI: walk `courses/*/index.html`, apply meta (and optionally pin element). |
| `scripts/pinterest/top-courses.mjs` | CLI: print the top N slugs by total lesson count. |
| `scripts/pinterest/gen-pins.mjs` | CLI: render 3 pin PNGs per selected course via `rsvg-convert`. |
| `scripts/pinterest/templates/v1-title.svg` | Pin template: bold title on gradient. |
| `scripts/pinterest/templates/v2-stat.svg` | Pin template: lesson-count stat card. |
| `scripts/pinterest/templates/v3-hook.svg` | Pin template: question hook. |

**New — browser (ES modules)**

| File | Responsibility |
|---|---|
| `js/videos.js` | Data only: channel URL, slug → video map, `videoForCourse()`. |
| `js/video-embed.js` | Render the click-to-play facade; swap in the iframe; fire GA4 `video_play`. |
| `js/subscribe.js` | Render the subscribe form; validate; write to Firestore; fire GA4 `subscribe`. |

**New — tests & docs**

`tests/pinterest/course-data.test.mjs`, `meta-block.test.mjs`, `inject.test.mjs`, `wrap-text.test.mjs`, `tests/videos.test.mjs`, `tests/subscribe.test.mjs`, `docs/pinterest-playbook.md`

**Modified**

`index.html` (domain-verify, homepage embed, footer channel link), `courses/*/index.html` (341 meta blocks; 5 embed mounts; 40 pin elements), `_headers` (CSP), `firestore.rules` (`subscribers`), `privacy.html` (GA correction + email + YouTube + localStorage), `css/global.css` (facade + form styles)

**Reused as-is:** `scripts/quiz-buildout/extract-units.mjs` — `extractMeta(slug)` returns `{ slug, courseName, unitNames, lessonsPerUnit, ... }` and handles both the tuple and `unitNames.map(...)` course formats. Currently untracked; Task 1 commits it.

---

## Phase A — Metadata foundation

### Task 1: Course data extraction

**Files:**
- Create: `scripts/pinterest/lib/course-data.mjs`
- Create: `tests/pinterest/course-data.test.mjs`
- Commit (existing, untracked): `scripts/quiz-buildout/extract-units.mjs`

**Interfaces:**
- Consumes: `extractMeta(slug)` from `scripts/quiz-buildout/extract-units.mjs`
- Produces:
  - `listCourseSlugs(): string[]` — sorted slugs under `courses/` that contain `index.html`
  - `getCourseData(slug): CourseData` where
    `CourseData = { slug, title, description, category, totalLessons: number|null, unitCount: number|null, url }`
  - `extractTitle(html): string`
  - `extractDescription(html): string`
  - `extractCategory(html): string`
  - `truncate(s, max = 160): string`

**Counts are nullable by design.** `extract-units.mjs` cannot parse the unit array of 61 of
the 341 courses — three separate boundary bugs (an apostrophe inside a single-quoted title; an
end-marker that overshoots into code referencing `lessons`; an end-marker landing inside a
`.map()` callback). That parser is shared with the quiz-buildout campaign, so this plan does
**not** modify it.

Instead `getCourseData()` degrades: `title`, `description`, and `category` come from plain
regex on the HTML and always work, while `totalLessons` and `unitCount` are `null` when the
unit array cannot be parsed. Metadata (Tasks 2–4, all 341 courses) needs no counts. Only the
pin ranking and the v2/v3 templates (Tasks 10–11) do, and they filter nulls out.

- [ ] **Step 1: Write the failing test**

```javascript
// tests/pinterest/course-data.test.mjs
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/course-data.test.mjs`
Expected: FAIL — `Cannot find module '.../lib/course-data.mjs'`

- [ ] **Step 3: Write the implementation**

```javascript
// scripts/pinterest/lib/course-data.mjs
// Normalizes a course index.html into a flat record for metadata and pin generation.
// Must be run with process.cwd() === repo root; extractMeta() resolves paths relative to it.
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { extractMeta } from '../../quiz-buildout/extract-units.mjs';

const COURSES_DIR = 'courses';
const SITE = 'https://mathagram.org';

function decodeEntities(s) {
  return String(s)
    .replace(/&#39;|&rsquo;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&ndash;/g, '–')
    .replace(/&mdash;/g, '—')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&');
}

function stripTags(s) {
  return String(s).replace(/<[^>]+>/g, '');
}

export function extractTitle(html) {
  const m = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
  if (!m) return '';
  return decodeEntities(stripTags(m[1])).replace(/\s+/g, ' ').trim();
}

export function extractDescription(html) {
  const m = html.match(/<header class="course-header">[\s\S]*?<p>([\s\S]*?)<\/p>/);
  if (!m) return '';
  return decodeEntities(stripTags(m[1])).replace(/\s+/g, ' ').trim();
}

export function extractCategory(html) {
  const m = html.match(/<span class="course-badge"[^>]*>([\s\S]*?)<\/span>/);
  if (!m) return '';
  return decodeEntities(stripTags(m[1])).replace(/\s+/g, ' ').trim();
}

export function truncate(s, max = 160) {
  const str = String(s).trim();
  if (str.length <= max) return str;
  const cut = str.slice(0, max - 1);
  const sp = cut.lastIndexOf(' ');
  const body = sp > max * 0.6 ? cut.slice(0, sp) : cut;
  return body.replace(/[\s,;:.–—-]+$/, '') + '…';
}

export function listCourseSlugs() {
  return readdirSync(COURSES_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory() && existsSync(`${COURSES_DIR}/${d.name}/index.html`))
    .map((d) => d.name)
    .sort();
}

export function getCourseData(slug) {
  const html = readFileSync(`${COURSES_DIR}/${slug}/index.html`, 'utf8');

  // Lesson counts are a bonus, not a requirement. extract-units.mjs cannot parse
  // 61 of the 341 courses' unit arrays, and metadata does not need counts — so a
  // parse failure degrades to nulls rather than throwing. Do not "fix" this by
  // editing extract-units.mjs: it is shared with the quiz-buildout tooling.
  let totalLessons = null;
  let unitCount = null;
  try {
    const meta = extractMeta(slug);
    totalLessons = meta.lessonsPerUnit.reduce((a, b) => a + b, 0);
    unitCount = meta.unitNames.length;
  } catch {
    // counts stay null
  }

  return {
    slug,
    title: extractTitle(html),
    description: truncate(extractDescription(html), 160),
    category: extractCategory(html),
    totalLessons,
    unitCount,
    url: `${SITE}/courses/${slug}/`,
  };
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/course-data.test.mjs`
Expected: PASS — 7 tests

- [ ] **Step 5: Confirm the whole catalog yields metadata**

`getCourseData()` must never throw, and every course must produce a title and description.
Counts are allowed to be null for the 61 known-unparseable courses.

Run:
```bash
cd /Users/dakotabrown/rehan-calculus-local && node -e "
import('./scripts/pinterest/lib/course-data.mjs').then(m => {
  const threw = [], noMeta = [], noCounts = [];
  for (const s of m.listCourseSlugs()) {
    try {
      const c = m.getCourseData(s);
      if (!c.title || !c.description) noMeta.push(s);
      if (c.totalLessons === null) noCounts.push(s);
    } catch (e) { threw.push(s + ': ' + e.message); }
  }
  console.log('threw:', threw.length, '| missing title/desc:', noMeta.length, '| null counts:', noCounts.length);
  threw.slice(0, 10).forEach(b => console.log('  THREW ' + b));
  noMeta.slice(0, 10).forEach(b => console.log('  NOMETA ' + b));
});"
```
Expected: `threw: 0 | missing title/desc: 0 | null counts: 61`.

`threw` or `missing title/desc` above zero is a real failure — report it and stop. A `null
counts` figure near 61 is expected and correct; report the exact number but do not treat it as
a failure and do not modify `extract-units.mjs`.

- [ ] **Step 6: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add scripts/quiz-buildout/extract-units.mjs scripts/pinterest/lib/course-data.mjs tests/pinterest/course-data.test.mjs
git commit -m "Add course-data extraction for Pinterest metadata

Wraps the existing extractMeta() unit parser and adds description,
category, lesson-count and canonical-URL normalization."
```

---

### Task 2: Meta block builder

**Files:**
- Create: `scripts/pinterest/lib/meta-block.mjs`
- Create: `tests/pinterest/meta-block.test.mjs`

**Interfaces:**
- Consumes: `CourseData` from Task 1
- Produces:
  - `META_START = '<!-- pin:meta:start -->'`, `META_END = '<!-- pin:meta:end -->'`
  - `PIN_START = '<!-- pin:media:start -->'`, `PIN_END = '<!-- pin:media:end -->'`
  - `escapeAttr(s): string`
  - `buildMetaBlock(course): string` — the `<head>` block, delimiters included
  - `buildPinElement(course, pinPath): string` — the `<body>` block, delimiters included

The pin element is **body** content, not head: an `<img>` inside `<head>` is invalid HTML and browsers hoist it out, which would corrupt the head block on re-parse.

- [ ] **Step 1: Write the failing test**

```javascript
// tests/pinterest/meta-block.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  META_START, META_END, PIN_START, PIN_END,
  escapeAttr, buildMetaBlock, buildPinElement,
} from '../../scripts/pinterest/lib/meta-block.mjs';

const COURSE = {
  slug: 'algebra',
  title: 'Algebra & "Friends"',
  description: 'Learn algebra <free>',
  category: 'Math',
  totalLessons: 1312,
  unitCount: 60,
  url: 'https://mathagram.org/courses/algebra/',
};

test('escapeAttr neutralizes quotes and angle brackets', () => {
  assert.equal(escapeAttr('a & b "c" <d>'), 'a &amp; b &quot;c&quot; &lt;d&gt;');
});

test('buildMetaBlock is wrapped in its delimiters', () => {
  const b = buildMetaBlock(COURSE);
  assert.ok(b.startsWith(META_START));
  assert.ok(b.trimEnd().endsWith(META_END));
});

test('buildMetaBlock emits the required Rich Pin tags', () => {
  const b = buildMetaBlock(COURSE);
  for (const needle of [
    'name="description"',
    'rel="canonical" href="https://mathagram.org/courses/algebra/"',
    'property="og:type" content="article"',
    'property="og:site_name" content="Mathagram"',
    'property="og:url" content="https://mathagram.org/courses/algebra/"',
    'property="og:image" content="https://mathagram.org/assets/lighthouse/og-card.png"',
    'property="article:section" content="Math"',
    'name="twitter:card" content="summary_large_image"',
  ]) {
    assert.ok(b.includes(needle), `missing: ${needle}`);
  }
});

test('buildMetaBlock escapes title and description into attributes', () => {
  const b = buildMetaBlock(COURSE);
  assert.ok(b.includes('content="Algebra &amp; &quot;Friends&quot; — Mathagram"'));
  assert.ok(b.includes('content="Learn algebra &lt;free&gt;"'));
  assert.ok(!b.includes('<free>'));
});

test('buildMetaBlock omits article:section when category is empty', () => {
  const b = buildMetaBlock({ ...COURSE, category: '' });
  assert.ok(!b.includes('article:section'));
});

test('buildPinElement emits a hidden img with absolute pin media', () => {
  const b = buildPinElement(COURSE, '/assets/pins/algebra-v1.png');
  assert.ok(b.startsWith(PIN_START));
  assert.ok(b.trimEnd().endsWith(PIN_END));
  assert.ok(b.includes('data-pin-media="https://mathagram.org/assets/pins/algebra-v1.png"'));
  assert.ok(b.includes('src="/assets/pins/algebra-v1.png"'));
  assert.ok(b.includes('style="display:none"'));
  assert.ok(b.includes('data-pin-description="Algebra &amp; &quot;Friends&quot;'));
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/meta-block.test.mjs`
Expected: FAIL — module not found

- [ ] **Step 3: Write the implementation**

```javascript
// scripts/pinterest/lib/meta-block.mjs
// Pure builders for the delimited HTML blocks injected into course pages.
export const META_START = '<!-- pin:meta:start -->';
export const META_END = '<!-- pin:meta:end -->';
export const PIN_START = '<!-- pin:media:start -->';
export const PIN_END = '<!-- pin:media:end -->';

const SITE = 'https://mathagram.org';
const OG_IMAGE = `${SITE}/assets/lighthouse/og-card.png`;

export function escapeAttr(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export function buildMetaBlock(course) {
  const title = escapeAttr(`${course.title} — Mathagram`);
  const desc = escapeAttr(course.description);
  const url = escapeAttr(course.url);
  const lines = [
    META_START,
    `  <meta name="description" content="${desc}">`,
    `  <link rel="canonical" href="${url}">`,
    `  <meta property="og:type" content="article">`,
    `  <meta property="og:site_name" content="Mathagram">`,
    `  <meta property="og:title" content="${title}">`,
    `  <meta property="og:description" content="${desc}">`,
    `  <meta property="og:url" content="${url}">`,
    `  <meta property="og:image" content="${OG_IMAGE}">`,
    `  <meta property="og:image:width" content="1200">`,
    `  <meta property="og:image:height" content="630">`,
  ];
  if (course.category) {
    lines.push(`  <meta property="article:section" content="${escapeAttr(course.category)}">`);
  }
  lines.push(
    `  <meta name="twitter:card" content="summary_large_image">`,
    `  <meta name="twitter:title" content="${title}">`,
    `  <meta name="twitter:description" content="${desc}">`,
    `  <meta name="twitter:image" content="${OG_IMAGE}">`,
    META_END,
  );
  return lines.join('\n');
}

export function buildPinElement(course, pinPath) {
  const desc = escapeAttr(`${course.title} — free interactive lessons on Mathagram`);
  const src = escapeAttr(pinPath);
  const media = escapeAttr(`${SITE}${pinPath}`);
  return [
    PIN_START,
    `  <img src="${src}" alt="" width="1000" height="1500" style="display:none"`,
    `       data-pin-media="${media}" data-pin-description="${desc}">`,
    PIN_END,
  ].join('\n');
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/meta-block.test.mjs`
Expected: PASS — 6 tests

- [ ] **Step 5: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add scripts/pinterest/lib/meta-block.mjs tests/pinterest/meta-block.test.mjs
git commit -m "Add Rich Pin meta-block and pin-media element builders"
```

---

### Task 3: Idempotent block injection

**Files:**
- Create: `scripts/pinterest/lib/inject.mjs`
- Create: `tests/pinterest/inject.test.mjs`

**Interfaces:**
- Produces: `injectBlock(html, block, { start, end, before }): string` — replaces an existing `start…end` region if present, otherwise inserts `block` immediately before the first occurrence of `before`. Throws if neither the region nor `before` is found.

- [ ] **Step 1: Write the failing test**

```javascript
// tests/pinterest/inject.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { injectBlock } from '../../scripts/pinterest/lib/inject.mjs';

const OPTS = { start: '<!--s-->', end: '<!--e-->', before: '</head>' };
const BLOCK = '<!--s-->\n  <meta name="x" content="1">\n<!--e-->';

test('inserts before the anchor when no block exists', () => {
  const out = injectBlock('<head>\n  <title>t</title>\n</head>', BLOCK, OPTS);
  assert.ok(out.includes(BLOCK));
  assert.ok(out.indexOf(BLOCK) < out.indexOf('</head>'));
  assert.ok(out.includes('<title>t</title>'));
});

test('is idempotent — injecting the same block twice is a no-op', () => {
  const once = injectBlock('<head></head>', BLOCK, OPTS);
  const twice = injectBlock(once, BLOCK, OPTS);
  assert.equal(once, twice);
});

test('replaces a stale block rather than appending a second one', () => {
  const stale = '<head>\n<!--s-->\n  <meta name="x" content="OLD">\n<!--e-->\n</head>';
  const out = injectBlock(stale, BLOCK, OPTS);
  assert.ok(out.includes('content="1"'));
  assert.ok(!out.includes('OLD'));
  assert.equal(out.split('<!--s-->').length - 1, 1);
});

test('preserves content outside the block', () => {
  const html = '<head><title>keep</title>\n<!--s-->old<!--e-->\n</head><body>body</body>';
  const out = injectBlock(html, BLOCK, OPTS);
  assert.ok(out.includes('<title>keep</title>'));
  assert.ok(out.includes('<body>body</body>'));
});

test('throws when the anchor is absent', () => {
  assert.throws(() => injectBlock('<html></html>', BLOCK, OPTS), /anchor/i);
});

test('refuses an ambiguous anchor rather than corrupting the file', () => {
  // A literal </head> inside a script would otherwise receive the block.
  const html = '<head><script>const t = "</head>";</script>\n</head>';
  assert.throws(() => injectBlock(html, BLOCK, OPTS), /more than once/i);
});

test('refuses a dangling start delimiter left by an interrupted write', () => {
  const html = '<head>\n<!--s-->\n  <meta name="x" content="OLD">\n</head>';
  assert.throws(() => injectBlock(html, BLOCK, OPTS), /no matching/i);
});

test('is idempotent when a head block and a body block coexist', () => {
  // This is the real state of a course page after both Task 4 and Task 11 run.
  const HEAD_OPTS = { start: '<!--ms-->', end: '<!--me-->', before: '</head>' };
  const BODY_OPTS = { start: '<!--ps-->', end: '<!--pe-->', before: '</body>' };
  const HEAD_BLOCK = '<!--ms-->\n  <meta name="a" content="1">\n<!--me-->';
  const BODY_BLOCK = '<!--ps-->\n  <img src="/p.png">\n<!--pe-->';
  const doc = '<html><head><title>t</title>\n</head><body><p>hi</p>\n</body></html>';

  const once = injectBlock(injectBlock(doc, HEAD_BLOCK, HEAD_OPTS), BODY_BLOCK, BODY_OPTS);
  const twice = injectBlock(injectBlock(once, HEAD_BLOCK, HEAD_OPTS), BODY_BLOCK, BODY_OPTS);

  assert.equal(once, twice, 'second pass over both blocks must be a no-op');
  assert.equal(once.split('<!--ms-->').length - 1, 1, 'exactly one head block');
  assert.equal(once.split('<!--ps-->').length - 1, 1, 'exactly one body block');
  assert.ok(once.indexOf('<!--ms-->') < once.indexOf('</head>'), 'head block in head');
  assert.ok(once.indexOf('<!--ps-->') > once.indexOf('</head>'), 'body block after head');
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/inject.test.mjs`
Expected: FAIL — module not found

- [ ] **Step 3: Write the implementation**

```javascript
// scripts/pinterest/lib/inject.mjs
// Idempotent delimited-block injection into an HTML string.
//
// This function rewrites 341 committed files, so every ambiguous input fails
// loudly rather than guessing. A wrong guess here corrupts the whole catalog
// and the corruption gets committed before anyone notices.
export function injectBlock(html, block, { start, end, before }) {
  const s = html.indexOf(start);
  const e = html.indexOf(end, s === -1 ? 0 : s);
  if (s !== -1 && e !== -1 && e > s) {
    return html.slice(0, s) + block + html.slice(e + end.length);
  }
  // A start delimiter with no matching end means a previous write was
  // interrupted. Inserting now would leave an orphaned delimiter plus a second
  // block, so refuse.
  if (s !== -1 && e === -1) {
    throw new Error(`injectBlock: found ${start} with no matching ${end}`);
  }
  const at = html.indexOf(before);
  if (at === -1) throw new Error(`injectBlock: anchor ${before} not found`);
  // indexOf takes the FIRST match. If the anchor string also appears earlier —
  // e.g. a literal "</body>" inside a script template literal on a
  // web-development course page — injecting there would mangle the script.
  // Refuse rather than corrupt.
  if (html.indexOf(before, at + before.length) !== -1) {
    throw new Error(`injectBlock: anchor ${before} appears more than once`);
  }
  return html.slice(0, at) + block + '\n' + html.slice(at);
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/inject.test.mjs`
Expected: PASS — 5 tests

- [ ] **Step 5: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add scripts/pinterest/lib/inject.mjs tests/pinterest/inject.test.mjs
git commit -m "Add idempotent delimited HTML block injection"
```

---

### Task 4: Apply metadata to all 341 course pages

**Files:**
- Create: `scripts/pinterest/add-course-meta.mjs`
- Modify: `courses/*/index.html` (all courses)

**Interfaces:**
- Consumes: `listCourseSlugs`, `getCourseData` (Task 1); `buildMetaBlock`, `META_START`, `META_END` (Task 2); `injectBlock` (Task 3)
- Produces: CLI only. `--dry-run` prints what would change without writing. `--only=<slug>[,<slug>]` limits scope. Exit code 1 if any course fails.

- [ ] **Step 1: Write the CLI**

```javascript
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
```

- [ ] **Step 2: Dry-run the whole catalog**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node scripts/pinterest/add-course-meta.mjs --dry-run | tail -5`
Expected: `changed=~341 unchanged=0 failed=0`. If `failed` is non-zero, stop and report the slugs — do not proceed with a partial write.

- [ ] **Step 3: Apply to three courses and inspect the result by eye**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --only=algebra,calculus,circuits
git diff --stat
sed -n '/pin:meta:start/,/pin:meta:end/p' courses/algebra/index.html
```
Expected: 3 files changed; the printed block sits inside `<head>`, has real title/description/category values, and contains no raw `<`, `>`, or unescaped `"` inside attribute values.

- [ ] **Step 4: Verify the trial pages still parse and render**

```bash
cd /Users/dakotabrown/rehan-calculus-local && node scripts/serve_local.mjs &
sleep 2
curl -s localhost:8000/courses/algebra/ | grep -c 'og:title'
```
Expected: `1`. Then open `http://localhost:8000/courses/algebra/` in a browser and confirm the learning path still renders and the console is free of errors. Stop the server afterward.

- [ ] **Step 5: Confirm idempotency on the trial subset**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --only=algebra,calculus,circuits
git diff --stat
```
Expected: the script reports `changed=0 unchanged=3`, and `git diff --stat` is byte-identical to Step 3's output (no new changes).

- [ ] **Step 6: Apply to the full catalog**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs
git diff --stat | tail -3
```
Expected: ~341 files changed, `failed=0`.

- [ ] **Step 7: Run the full test suite, then commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/pinterest/*.test.mjs'
git add scripts/pinterest/add-course-meta.mjs courses/
git commit -m "Add Rich Pin + SEO metadata to all course pages

Course pages previously had no og:*, canonical, or meta description.
Adds an idempotent delimited block to each so Pinterest can build
Article Rich Pins and search engines get real titles and summaries."
```

---

## Phase B — Pinterest domain claim

### Task 5: Domain verification tag

**Files:**
- Modify: `index.html` (head, after the canonical link)

Pinterest verifies the root domain only, so this goes on the homepage and nowhere else.

- [ ] **Step 1: Add the real verification tag**

The user supplied their live code on 2026-07-26. It is **not** a placeholder — use this exact
value. (Pinterest calls this screen "Link to Pinterest → Websites → Claim", not "Claimed
accounts".)

Insert immediately after `<link rel="canonical" href="https://mathagram.org/">` in `index.html`:

```html
  <!-- Pinterest domain claim (Settings → Link to Pinterest → Websites → Claim).
       Pinterest fetches this homepage to verify; it must be deployed before
       clicking Verify on Pinterest's side. -->
  <meta name="p:domain_verify" content="95b7afa457ded04fa7214c5fdb22e95c">
```

Match the surrounding style: no self-closing slash, two-space indent.

- [ ] **Step 2: Verify it is present and unique**

```bash
cd /Users/dakotabrown/rehan-calculus-local
grep -c 'p:domain_verify' index.html
grep -rl 'p:domain_verify' --include='*.html' . | wc -l
```
Expected: `1` and `1` — homepage only.

- [ ] **Step 3: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add index.html
git commit -m "Add Pinterest domain-verify meta tag placeholder to homepage"
```

- [ ] **Step 4: Flag the manual step**

Report to the user that the tag is in place and the homepage must be **deployed** before they
click Verify on Pinterest. The user performs the deploy (see Task 15 Step 5 for the mandatory
5-path clean); the implementer must not run `netlify deploy`.

---

## Phase C — YouTube embeds

### Task 6: Video map

**Files:**
- Create: `js/videos.js`
- Create: `tests/videos.test.mjs`

**Interfaces:**
- Produces:
  - `CHANNEL_URL: string`
  - `VIDEOS: Record<string, { id: string, title: string, seconds: number }>`
  - `videoForCourse(slug): { id, title, seconds } | null`

- [ ] **Step 1: Write the failing test**

```javascript
// tests/videos.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { CHANNEL_URL, VIDEOS, videoForCourse } from '../js/videos.js';

test('channel URL is the real channel', () => {
  assert.equal(CHANNEL_URL, 'https://www.youtube.com/@Mathagram_Org');
});

test('every entry has a valid 11-character YouTube id and positive duration', () => {
  const entries = Object.entries(VIDEOS);
  assert.ok(entries.length >= 6, `expected 6+ entries, got ${entries.length}`);
  for (const [key, v] of entries) {
    assert.match(v.id, /^[\w-]{11}$/, `${key} has a bad id: ${v.id}`);
    assert.ok(v.title && v.title.length > 3, `${key} has no title`);
    assert.ok(Number.isInteger(v.seconds) && v.seconds > 0, `${key} has a bad duration`);
  }
});

test('video ids are unique across the map', () => {
  const ids = Object.values(VIDEOS).map((v) => v.id);
  assert.equal(new Set(ids).size, ids.length);
});

test('videoForCourse resolves mapped slugs and rejects unmapped ones', () => {
  assert.equal(videoForCourse('calculus').id, '5NfBbViWmRQ');
  assert.equal(videoForCourse('circuits').id, 'P3lDex2QSPI');
  assert.equal(videoForCourse('no-such-course'), null);
});

test('videoForCourse is not fooled by inherited Object properties', () => {
  assert.equal(videoForCourse('constructor'), null);
  assert.equal(videoForCourse('toString'), null);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/videos.test.mjs`
Expected: FAIL — module not found

- [ ] **Step 3: Write the implementation**

```javascript
// js/videos.js
// Curated course-slug → YouTube video map. Data only, no DOM access.
export const CHANNEL_URL = 'https://www.youtube.com/@Mathagram_Org';

export const VIDEOS = {
  calculus:                        { id: '5NfBbViWmRQ', title: 'What are Integrals for kids',                 seconds: 26 },
  circuits:                        { id: 'P3lDex2QSPI', title: 'What are Circuits for kids',                  seconds: 22 },
  'clustering-and-classification': { id: '8buAOAnFU64', title: 'Clustering & Classification for kids',        seconds: 26 },
  algebra:                         { id: 'fymLtux-g3c', title: 'Sigma Notation for kids',                     seconds: 26 },
  'social-media-rules':            { id: 'VRroVDswkE4', title: "Before You Post: Edam's 12 Must-Know Rules",  seconds: 136 },
  _home:                           { id: 'E1jJj3Pklz4', title: 'This Site Teaches EVERYTHING For Free',       seconds: 84 },
};

// Unmapped inventory — the channel held 10 videos on 2026-07-26. Kept here so
// adding a mapping later does not require re-reading the channel.
//   LW2a87Tj2iQ  How Voices Work (48s)
//   KCFniwSsbpQ  Mathagram Sigma Cubed Ad (16s)
//   NyisUTZFZSE  Antes de publicar en Mathagram: 12 reglas y 3 strikes (152s, es)
//   eed7efthjho  Sin apps. Sin pagos. Solo aprender: Mathagram (109s, es)

export function videoForCourse(slug) {
  return Object.prototype.hasOwnProperty.call(VIDEOS, slug) ? VIDEOS[slug] : null;
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/videos.test.mjs`
Expected: PASS — 5 tests

- [ ] **Step 5: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add js/videos.js tests/videos.test.mjs
git commit -m "Add curated course-slug to YouTube video map"
```

---

### Task 7: CSP allowances for YouTube

**Files:**
- Modify: `_headers` (both the `/*.html` block and the `/` block)

Without this the iframe and thumbnail are blocked in production and the facade fails silently. CSP stays in `_headers` — never a `<meta>` tag — so translate.goog keeps working.

- [ ] **Step 1: Add the two sources to both CSP blocks**

In `_headers`, in **each** of the `/*.html` and `/` policies:

- append ` https://i.ytimg.com` to the `img-src` directive
- append ` https://www.youtube-nocookie.com` to the `frame-src` directive

Leave every other directive untouched.

- [ ] **Step 2: Verify both blocks changed and nothing else did**

```bash
cd /Users/dakotabrown/rehan-calculus-local
grep -c 'i.ytimg.com' _headers
grep -c 'youtube-nocookie.com' _headers
git diff _headers
```
Expected: `2` and `2`. The diff shows exactly two modified lines, and no `Content-Security-Policy` appears anywhere in an HTML `<meta>` tag:

```bash
grep -rn 'http-equiv="Content-Security-Policy"' --include='*.html' . | wc -l
```
Expected: `0`.

- [ ] **Step 3: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add _headers
git commit -m "CSP: allow YouTube nocookie frames and ytimg thumbnails"
```

---

### Task 8: Click-to-play video facade

**Files:**
- Create: `js/video-embed.js`
- Modify: `css/global.css` (append facade styles)
- Modify: `courses/calculus/index.html`, `courses/circuits/index.html`, `courses/clustering-and-classification/index.html`, `courses/algebra/index.html`, `courses/social-media-rules/index.html`, `index.html`

**Interfaces:**
- Consumes: `videoForCourse` (Task 6)
- Produces:
  - `mountVideoEmbed(container: HTMLElement, video: {id,title,seconds}): void`
  - `initVideoEmbed(slug: string, containerId?: string): void` — default `containerId` is `'course-video'`; removes the container when the slug is unmapped

`hqdefault.jpg` is used for thumbnails, not `maxresdefault.jpg` — max-res does not exist for every upload (short vertical videos in particular) and would render a broken image.

- [ ] **Step 1: Write the implementation**

```javascript
// js/video-embed.js
// Click-to-play YouTube facade: no third-party JS or cookies load until the
// user clicks. Autoplay is applied only in the click handler, never on load.
import { videoForCourse } from './videos.js';

const thumbUrl = (id) => `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;

export function mountVideoEmbed(container, video) {
  if (!container || !video) return;
  container.textContent = '';

  const wrap = document.createElement('div');
  wrap.className = 'yt-facade';

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'yt-facade-btn';
  btn.setAttribute('aria-label', `Play video: ${video.title}`);

  const img = document.createElement('img');
  img.src = thumbUrl(video.id);
  img.alt = '';
  img.loading = 'lazy';
  img.width = 480;
  img.height = 360;

  const play = document.createElement('span');
  play.className = 'yt-facade-play';
  play.setAttribute('aria-hidden', 'true');

  btn.append(img, play);

  const caption = document.createElement('p');
  caption.className = 'yt-facade-title';
  caption.textContent = video.title;

  wrap.append(btn, caption);
  container.append(wrap);

  btn.addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.className = 'yt-facade-frame';
    frame.src = `https://www.youtube-nocookie.com/embed/${video.id}?rel=0&autoplay=1`;
    frame.title = video.title;
    frame.allow = 'accelerometer; encrypted-media; gyroscope; picture-in-picture';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    frame.setAttribute('loading', 'lazy');
    wrap.replaceChild(frame, btn);
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'video_play', {
        video_id: video.id,
        course: container.dataset.course || '',
      });
    }
  }, { once: true });
}

export function initVideoEmbed(slug, containerId = 'course-video') {
  const container = document.getElementById(containerId);
  if (!container) return;
  const video = videoForCourse(slug);
  if (!video) { container.remove(); return; }
  container.dataset.course = slug;
  mountVideoEmbed(container, video);
}
```

- [ ] **Step 2: Append the styles**

Append to `css/global.css`:

```css
/* ---- YouTube click-to-play facade ---- */
.yt-facade { max-width: 560px; margin: 0 auto 32px; }
.yt-facade-btn {
  position: relative; display: block; width: 100%; padding: 0;
  border: 0; border-radius: 12px; overflow: hidden; cursor: pointer;
  background: #0c1020; line-height: 0;
}
.yt-facade-btn img { width: 100%; height: auto; display: block; opacity: 0.92; transition: opacity 0.2s; }
.yt-facade-btn:hover img,
.yt-facade-btn:focus-visible img { opacity: 1; }
.yt-facade-play {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 68px; height: 48px; border-radius: 12px; background: #00e5c8;
}
.yt-facade-play::after {
  content: ''; position: absolute; top: 50%; left: 50%;
  transform: translate(-40%, -50%);
  border-style: solid; border-width: 11px 0 11px 18px;
  border-color: transparent transparent transparent #0c1020;
}
.yt-facade-frame { width: 100%; aspect-ratio: 16 / 9; border: 0; border-radius: 12px; display: block; }
.yt-facade-title {
  margin-top: 10px; font-size: 0.9rem; text-align: center;
  color: var(--color-text-secondary);
}
```

- [ ] **Step 3: Mount on the five mapped course pages**

For each of `calculus`, `circuits`, `clustering-and-classification`, `algebra`, `social-media-rules`:

Insert the container immediately before `<div id="learning-path" class="path-container"></div>`:

```html
  <div id="course-video"></div>
```

And inside the existing `<script type="module">` block, after the `initNav('../../');` line, add (substituting the real slug):

```javascript
    import { initVideoEmbed } from '../../js/video-embed.js';
    initVideoEmbed('calculus');
```

- [ ] **Step 4: Mount on the homepage**

In `index.html`, add `<div id="course-video"></div>` inside the hero section after the tagline, and in the homepage's module script add:

```javascript
    import { initVideoEmbed } from './js/video-embed.js';
    initVideoEmbed('_home');
```

- [ ] **Step 5: Verify in a real browser with CSP applied**

`scripts/serve_local.mjs` does not apply `_headers`, so CSP must be confirmed against production in Task 15. Locally, confirm behavior:

```bash
cd /Users/dakotabrown/rehan-calculus-local && node scripts/serve_local.mjs &
```

Open `http://localhost:8000/courses/calculus/` and confirm:
1. The thumbnail renders with a teal play button; the console is clean.
2. **No request to `youtube-nocookie.com` occurs before clicking** (check the Network tab) — this is the property that keeps the embed fast and the view valid.
3. Clicking swaps in the iframe and the video plays.
4. `http://localhost:8000/courses/cosplay-craft/` (unmapped) shows no empty gap and no console error.

Stop the server afterward.

- [ ] **Step 6: Run tests and commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/*.test.mjs' 'tests/pinterest/*.test.mjs'
git add js/video-embed.js css/global.css index.html courses/calculus/index.html courses/circuits/index.html courses/clustering-and-classification/index.html courses/algebra/index.html courses/social-media-rules/index.html
git commit -m "Add click-to-play YouTube facade to mapped course pages

Loads no third-party JS or cookies until the user clicks, so embedded
views are unambiguously user-initiated and count as valid watch time."
```

---

## Phase D — Pin images

### Task 9: SVG text wrapping

**Files:**
- Create: `scripts/pinterest/lib/wrap-text.mjs`
- Create: `tests/pinterest/wrap-text.test.mjs`

**Interfaces:**
- Produces: `wrapText(text, maxChars, maxLines): string[]` — greedy word wrap; the final line is ellipsized when content is dropped; over-long single words are hard-cut.

- [ ] **Step 1: Write the failing test**

```javascript
// tests/pinterest/wrap-text.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { wrapText } from '../../scripts/pinterest/lib/wrap-text.mjs';

test('short text stays on one line', () => {
  assert.deepEqual(wrapText('Algebra', 20, 3), ['Algebra']);
});

test('wraps greedily on word boundaries within the char budget', () => {
  const lines = wrapText('Introduction to Linear Algebra', 15, 3);
  assert.ok(lines.length > 1);
  for (const l of lines) assert.ok(l.length <= 15, `too long: "${l}"`);
  assert.equal(lines.join(' '), 'Introduction to Linear Algebra');
});

test('never exceeds maxLines and ellipsizes when truncating', () => {
  const lines = wrapText('one two three four five six seven eight nine ten', 10, 2);
  assert.equal(lines.length, 2);
  assert.ok(lines[1].endsWith('…'));
  for (const l of lines) assert.ok(l.length <= 10, `too long: "${l}"`);
});

test('hard-cuts a single word longer than the budget', () => {
  const lines = wrapText('Electroencephalography', 10, 2);
  assert.ok(lines[0].length <= 10);
  assert.ok(lines[0].endsWith('…'));
});

test('collapses whitespace and ignores empty input', () => {
  assert.deepEqual(wrapText('  a   b  ', 10, 2), ['a b']);
  assert.deepEqual(wrapText('', 10, 2), []);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/wrap-text.test.mjs`
Expected: FAIL — module not found

- [ ] **Step 3: Write the implementation**

```javascript
// scripts/pinterest/lib/wrap-text.mjs
// Greedy word wrap for SVG <tspan> output. rsvg-convert does not wrap text and
// does not support <foreignObject>, so line breaks are computed here.
export function wrapText(text, maxChars, maxLines) {
  const words = String(text).split(/\s+/).filter(Boolean);
  const lines = [];
  let cur = '';
  let i = 0;

  for (; i < words.length; i++) {
    const word = words[i];
    const next = cur ? `${cur} ${word}` : word;
    if (next.length <= maxChars) { cur = next; continue; }
    if (cur) { lines.push(cur); cur = ''; }
    if (lines.length >= maxLines) break;
    cur = word.length <= maxChars ? word : `${word.slice(0, maxChars - 1)}…`;
  }

  if (cur && lines.length < maxLines) { lines.push(cur); i = words.length; }

  if (i < words.length && lines.length) {
    const last = lines.length - 1;
    lines[last] = lines[last]
      .slice(0, Math.max(0, maxChars - 1))
      .replace(/[\s,;:.]+$/, '') + '…';
  }
  return lines;
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/wrap-text.test.mjs`
Expected: PASS — 5 tests

- [ ] **Step 5: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add scripts/pinterest/lib/wrap-text.mjs tests/pinterest/wrap-text.test.mjs
git commit -m "Add greedy SVG text wrapping for pin templates"
```

---

### Task 10: Pin templates and generator

**Files:**
- Create: `scripts/pinterest/templates/v1-title.svg`, `v2-stat.svg`, `v3-hook.svg`
- Create: `scripts/pinterest/top-courses.mjs`
- Create: `scripts/pinterest/gen-pins.mjs`
- Create: `assets/pins/` (~120 PNGs)

**Interfaces:**
- Consumes: `listCourseSlugs`, `getCourseData` (Task 1); `wrapText` (Task 9)
- Produces: CLI only. `top-courses.mjs [N]` prints N slugs, one per line. `gen-pins.mjs [--limit=N]` writes `assets/pins/<slug>-v{1,2,3}.png`.

Templates use `{{TOKEN}}` placeholders. `{{TITLE_TSPANS}}` is replaced with generated `<tspan>` elements; every other token is a plain string.

- [ ] **Step 1: Create `v1-title.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1500" viewBox="0 0 1000 1500">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#141a2e"/><stop offset="1" stop-color="#0c1020"/>
    </linearGradient>
    <linearGradient id="teal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00e5c8"/><stop offset="1" stop-color="#22d3ee"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="1500" fill="url(#bg)"/>
  <circle cx="850" cy="220" r="380" fill="#00e5c8" opacity="0.10"/>
  <circle cx="140" cy="1300" r="300" fill="#22d3ee" opacity="0.08"/>
  <g transform="translate(400,120) scale(3.0)">
    <rect x="16" y="56" width="32" height="6" rx="2" fill="#ffffff"/>
    <polygon points="24,56 22,28 42,28 40,56" fill="#ffffff"/>
    <rect x="20" y="22" width="24" height="8" rx="2" fill="#ffffff"/>
    <rect x="24" y="24" width="16" height="4" rx="1" fill="#00e5c8"/>
    <polygon points="28,14 32,8 36,14" fill="#ffffff"/>
    <rect x="26" y="14" width="12" height="8" rx="2" fill="#ffffff"/>
  </g>
  <text x="500" y="620" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="{{TITLE_SIZE}}" font-weight="bold" fill="#ffffff">{{TITLE_TSPANS}}</text>
  <rect x="400" y="{{RULE_Y}}" width="200" height="10" rx="5" fill="url(#teal)"/>
  <text x="500" y="{{SUB_Y}}" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="44" fill="#cbd5e1">{{CATEGORY}}</text>
  <text x="500" y="1300" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="46" font-weight="bold" fill="#00e5c8">100% free · no signup</text>
  <text x="500" y="1380" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="38" fill="#64748b">mathagram.org</text>
</svg>
```

- [ ] **Step 2: Create `v2-stat.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1500" viewBox="0 0 1000 1500">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#141a2e"/><stop offset="1" stop-color="#0c1020"/>
    </linearGradient>
    <linearGradient id="teal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00e5c8"/><stop offset="1" stop-color="#22d3ee"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="1500" fill="url(#bg)"/>
  <circle cx="500" cy="480" r="420" fill="#00e5c8" opacity="0.07"/>
  <text x="500" y="300" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="40" font-weight="bold" fill="#64748b">{{CATEGORY}}</text>
  <text x="500" y="520" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="200" font-weight="bold" fill="url(#teal)">{{LESSONS}}</text>
  <text x="500" y="600" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="52" fill="#cbd5e1">free lessons</text>
  <rect x="350" y="660" width="300" height="8" rx="4" fill="url(#teal)"/>
  <text x="500" y="800" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="{{TITLE_SIZE}}" font-weight="bold" fill="#ffffff">{{TITLE_TSPANS}}</text>
  <text x="500" y="1200" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="42" fill="#cbd5e1">{{UNITS}} units · interactive · no app</text>
  <text x="500" y="1380" text-anchor="middle" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="38" fill="#64748b">mathagram.org</text>
</svg>
```

- [ ] **Step 3: Create `v3-hook.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1500" viewBox="0 0 1000 1500">
  <defs>
    <linearGradient id="bg" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#0c1020"/><stop offset="1" stop-color="#141a2e"/>
    </linearGradient>
    <linearGradient id="teal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00e5c8"/><stop offset="1" stop-color="#22d3ee"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="1500" fill="url(#bg)"/>
  <circle cx="180" cy="240" r="320" fill="#22d3ee" opacity="0.09"/>
  <text x="80" y="300" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="150" font-weight="bold" fill="#00e5c8" opacity="0.45">?</text>
  <text x="80" y="560" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="64" font-weight="bold" fill="#ffffff">Still stuck on</text>
  <text x="80" y="680" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="{{TITLE_SIZE}}" font-weight="bold" fill="url(#teal)">{{TITLE_TSPANS}}</text>
  <rect x="80" y="{{RULE_Y}}" width="240" height="10" rx="5" fill="url(#teal)"/>
  <text x="80" y="1120" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="46" fill="#cbd5e1">{{LESSONS}} step-by-step lessons.</text>
  <text x="80" y="1190" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="46" fill="#cbd5e1">Free. No signup.</text>
  <text x="80" y="1380" font-family="Verdana, 'DejaVu Sans', sans-serif"
        font-size="38" font-weight="bold" fill="#64748b">mathagram.org</text>
</svg>
```

- [ ] **Step 4: Write `top-courses.mjs`**

```javascript
// scripts/pinterest/top-courses.mjs
// Print the top N course slugs by total lesson count, one per line.
// Usage: node scripts/pinterest/top-courses.mjs 40
import { listCourseSlugs, getCourseData } from './lib/course-data.mjs';

const n = Number(process.argv[2] || 40);
// Courses whose unit array could not be parsed have null counts and cannot be
// ranked — the v2/v3 templates print a lesson count, so they are not pinnable.
const rows = listCourseSlugs()
  .map(getCourseData)
  .filter((c) => c.totalLessons !== null);
rows.sort((a, b) => b.totalLessons - a.totalLessons);
for (const c of rows.slice(0, n)) console.log(c.slug);
```

- [ ] **Step 5: Write `gen-pins.mjs`**

```javascript
// scripts/pinterest/gen-pins.mjs
// Render 3 Pinterest pin PNGs (1000x1500) per top course via rsvg-convert.
// Usage: node scripts/pinterest/gen-pins.mjs [--limit=40]
import { readFileSync, writeFileSync, mkdirSync, rmSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { listCourseSlugs, getCourseData } from './lib/course-data.mjs';
import { wrapText } from './lib/wrap-text.mjs';

const TEMPLATES = [
  { name: 'v1', file: 'v1-title.svg', maxChars: 18, maxLines: 3, baseSize: 96,  titleY: 620, lineH: 104 },
  { name: 'v2', file: 'v2-stat.svg',  maxChars: 20, maxLines: 3, baseSize: 76,  titleY: 800, lineH: 88  },
  { name: 'v3', file: 'v3-hook.svg',  maxChars: 16, maxLines: 3, baseSize: 92,  titleY: 680, lineH: 100 },
];

const OUT_DIR = 'assets/pins';
const TPL_DIR = 'scripts/pinterest/templates';
const TMP = 'assets/pins/.tmp.svg';

const limitArg = process.argv.find((a) => a.startsWith('--limit='));
const limit = limitArg ? Number(limitArg.slice('--limit='.length)) : 40;

// One tspan per line, x reset each line so the parent's text-anchor applies.
function tspans(lines, x, lineHeight) {
  return lines
    .map((l, i) => `<tspan x="${x}" dy="${i === 0 ? 0 : lineHeight}">${escapeXml(l)}</tspan>`)
    .join('');
}

function escapeXml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function render(course, tpl) {
  const lines = wrapText(course.title, tpl.maxChars, tpl.maxLines);
  // Step the font down as line count grows so tall titles stay inside the frame.
  const size = Math.round(tpl.baseSize * (lines.length >= 3 ? 0.72 : lines.length === 2 ? 0.86 : 1));
  const lineH = Math.round(tpl.lineH * (size / tpl.baseSize));
  const x = tpl.name === 'v3' ? 80 : 500;
  // Course text goes through function replacers: a string replacement would let a
  // literal `$&` or `$1` in a course title be reinterpreted as a capture reference.
  const svg = readFileSync(`${TPL_DIR}/${tpl.file}`, 'utf8')
    .replaceAll('{{TITLE_TSPANS}}', () => tspans(lines, x, lineH))
    .replaceAll('{{TITLE_SIZE}}', String(size))
    .replaceAll('{{CATEGORY}}', () => escapeXml(course.category || 'Free course'))
    .replaceAll('{{LESSONS}}', String(course.totalLessons))
    .replaceAll('{{UNITS}}', String(course.unitCount))
    .replaceAll('{{RULE_Y}}', String(tpl.titleY + lines.length * lineH - 40))
    .replaceAll('{{SUB_Y}}', String(tpl.titleY + lines.length * lineH + 60));

  writeFileSync(TMP, svg);
  execFileSync('rsvg-convert', [
    '-w', '1000', '-h', '1500', '-f', 'png',
    '-o', `${OUT_DIR}/${course.slug}-${tpl.name}.png`, TMP,
  ]);
}

mkdirSync(OUT_DIR, { recursive: true });

// Null counts mean the unit array could not be parsed; the v2/v3 templates print a
// lesson count, so those courses are excluded from pin generation.
const rows = listCourseSlugs()
  .map(getCourseData)
  .filter((c) => c.totalLessons !== null);
rows.sort((a, b) => b.totalLessons - a.totalLessons);
const selected = rows.slice(0, limit);
console.log(`ranking ${rows.length} courses with known lesson counts; taking top ${limit}`);

let made = 0;
for (const course of selected) {
  for (const tpl of TEMPLATES) { render(course, tpl); made++; }
}
rmSync(TMP, { force: true });
console.log(`generated ${made} pins for ${selected.length} courses in ${OUT_DIR}/`);
```

- [ ] **Step 6: Generate one course and inspect it visually**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/gen-pins.mjs --limit=1
ls -la assets/pins/
for f in assets/pins/*.png; do echo "$f: $(rsvg-convert --version >/dev/null && file -b "$f")"; done
```
Expected: 3 PNGs, each reported as `PNG image data, 1000 x 1500`. **Open all three and look at them.** Confirm the title is inside the frame, not clipped or overlapping the rule or the footer, and that text is legible when scaled to roughly 250px wide (Pinterest feed size). Adjust `maxChars` / `baseSize` per template and regenerate until they read cleanly.

- [ ] **Step 7: Generate the full set of 40 courses**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/gen-pins.mjs --limit=40
ls assets/pins/*.png | wc -l
du -sh assets/pins
file assets/pins/*.png | grep -cv '1000 x 1500'
```
Expected: `120`, roughly 20 MB or less, and `0` files with wrong dimensions.

- [ ] **Step 8: Spot-check the longest and shortest titles**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/top-courses.mjs 40 | head -3
node scripts/pinterest/top-courses.mjs 40 | tail -3
```
Open the `-v1`, `-v2`, `-v3` PNGs for one long-titled and one short-titled course from that list and confirm both wrap acceptably.

- [ ] **Step 9: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/pinterest/*.test.mjs'
git add scripts/pinterest/templates scripts/pinterest/top-courses.mjs scripts/pinterest/gen-pins.mjs assets/pins
git commit -m "Add 2:3 Pinterest pin generation for top 40 courses

Three templates x 40 courses = 120 PNGs at 1000x1500, rendered with
rsvg-convert. Multiple images per URL is what feeds Pinterest's
fresh-pin ranking."
```

---

### Task 11: Wire pin media into the pinned course pages

**Files:**
- Modify: `scripts/pinterest/add-course-meta.mjs` (add `--pins` mode)
- Modify: `courses/*/index.html` for the 40 courses that have pins

**Interfaces:**
- Consumes: `buildPinElement`, `PIN_START`, `PIN_END` (Task 2); `injectBlock` (Task 3)
- Produces: `add-course-meta.mjs --pins` injects the body pin element for every course with an existing `assets/pins/<slug>-v1.png`

- [ ] **Step 1: Extend the CLI**

In `scripts/pinterest/add-course-meta.mjs`, add to the imports:

```javascript
import { existsSync } from 'node:fs';
import { buildPinElement, PIN_START, PIN_END } from './lib/meta-block.mjs';
```

Add `const withPins = args.includes('--pins');` beside the other flag parsing, and inside the per-slug `try` block, after the meta injection and before the write, insert:

```javascript
    let html = after;
    if (withPins) {
      const pin = `/assets/pins/${slug}-v1.png`;
      if (existsSync(`assets/pins/${slug}-v1.png`)) {
        html = injectBlock(html, buildPinElement(getCourseData(slug), pin), {
          start: PIN_START, end: PIN_END, before: '</body>',
        });
      }
    }
    if (html === before) { unchanged++; continue; }
    changed++;
    if (dryRun) console.log(`would update ${path}`);
    else writeFileSync(path, html);
```

Remove the now-superseded `if (after === before)` / write lines so each course is written exactly once.

- [ ] **Step 2: Dry-run and confirm only pinned courses change**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --pins --dry-run | tail -3
```
Expected: `changed=40` (only courses with a generated `-v1.png`), `failed=0`.

- [ ] **Step 3: Apply, then verify placement is in the body**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --pins
SLUG=$(node scripts/pinterest/top-courses.mjs 1)
sed -n '/pin:media:start/,/pin:media:end/p' "courses/$SLUG/index.html"
node -e "
const h=require('fs').readFileSync('courses/$SLUG/index.html','utf8');
console.log('pin after </head>:', h.indexOf('pin:media:start') > h.indexOf('</head>'));
console.log('pin before </body>:', h.indexOf('pin:media:start') < h.indexOf('</body>'));"
```
Expected: the element prints, and both checks are `true` — the `<img>` must never land in `<head>`.

- [ ] **Step 4: Confirm idempotency across both modes**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --pins
git status --short courses/ | wc -l
```
Expected: the run reports `changed=0`, and re-running produces no further modifications beyond Step 3's.

- [ ] **Step 5: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add scripts/pinterest/add-course-meta.mjs courses/
git commit -m "Point Pinterest save button at the 2:3 pin image

og:image stays landscape for Twitter/Facebook; a hidden body element
supplies the vertical image via data-pin-media."
```

---

## Phase E — Email capture

### Task 12: Firestore subscribers rules

**Files:**
- Modify: `firestore.rules`

- [ ] **Step 1: Add the collection rule**

Insert immediately before the `// Deny everything else` block in `firestore.rules`:

```javascript
    // Newsletter subscribers: create-only from the client, never readable.
    // Validation mirrors js/subscribe.js. Export via the Firebase console.
    match /subscribers/{subId} {
      allow create: if request.resource.data.keys().hasOnly(['email','role','source','createdAt'])
        && request.resource.data.email is string
        && request.resource.data.email.size() >= 5
        && request.resource.data.email.size() <= 254
        && request.resource.data.email.matches('^[^@\\\\s]+@[^@\\\\s]+\\\\.[^@\\\\s]+$')
        && request.resource.data.role in ['parent','teacher','learner']
        && request.resource.data.source is string
        && request.resource.data.source.size() <= 64;
      allow read, update, delete: if false;
    }
```

- [ ] **Step 2: Verify the rules compile**

```bash
cd /Users/dakotabrown/rehan-calculus-local
npx --yes firebase-tools@latest firestore:rules:check firestore.rules --project mathagram-cb526 2>&1 | tail -5
```
If that subcommand is unavailable in the installed CLI version, fall back to deploying in Step 3 — a syntax error fails the deploy loudly rather than silently.

- [ ] **Step 3: Deploy the rules**

```bash
cd /Users/dakotabrown/rehan-calculus-local
npx --yes firebase-tools@latest deploy --only firestore:rules --project mathagram-cb526
```
Expected: `Deploy complete!`. Rules deploy independently of the Netlify site.

- [ ] **Step 4: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add firestore.rules
git commit -m "Firestore: add create-only subscribers collection

Client can append a subscriber with a validated email, role and source;
reads, updates and deletes are denied outright."
```

---

### Task 13: Subscribe form

**Files:**
- Create: `js/subscribe.js`
- Create: `tests/subscribe.test.mjs`
- Modify: `css/global.css` (append form styles)
- Modify: the 5 mapped course pages from Task 8

**Interfaces:**
- Consumes: `db` from `js/firebase-config.js`; `collection`, `addDoc`, `serverTimestamp` from the Firebase 10.12.0 Firestore CDN module
- Produces:
  - `isValidEmail(email): boolean`
  - `isThrottled(now, store): boolean` and `markSubmitted(now, store): void`
  - `mountSubscribeForm(container: HTMLElement, source: string): void`

`isValidEmail` / `isThrottled` are pure and unit-tested; `mountSubscribeForm` touches the DOM and Firestore and is verified in the browser.

The pure helpers must live in a DOM-free module so `node --test` can import them without a browser. Put them in `js/subscribe-validate.js` and have `js/subscribe.js` import from it.

- [ ] **Step 1: Write the failing test**

```javascript
// tests/subscribe.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  isValidEmail, isThrottled, markSubmitted, THROTTLE_MS,
} from '../js/subscribe-validate.js';

function fakeStore(initial = {}) {
  const m = new Map(Object.entries(initial));
  return {
    getItem: (k) => (m.has(k) ? m.get(k) : null),
    setItem: (k, v) => m.set(k, String(v)),
  };
}

test('accepts ordinary addresses', () => {
  for (const e of ['a@b.co', 'teacher+list@school.edu', 'x.y@sub.domain.org']) {
    assert.equal(isValidEmail(e), true, `rejected ${e}`);
  }
});

test('rejects malformed addresses and non-strings', () => {
  for (const e of ['', 'nope', 'a@b', 'a b@c.co', 'a@@b.co', null, undefined, 42, {}]) {
    assert.equal(isValidEmail(e), false, `accepted ${JSON.stringify(e)}`);
  }
});

test('rejects addresses longer than 254 characters', () => {
  assert.equal(isValidEmail(`${'a'.repeat(250)}@b.co`), false);
});

test('is not throttled on a fresh browser', () => {
  assert.equal(isThrottled(1_000_000, fakeStore()), false);
});

test('is throttled immediately after a submission', () => {
  const store = fakeStore();
  markSubmitted(1_000_000, store);
  assert.equal(isThrottled(1_000_000, store), true);
  assert.equal(isThrottled(1_000_000 + THROTTLE_MS - 1, store), true);
});

test('throttle expires after the window', () => {
  const store = fakeStore();
  markSubmitted(1_000_000, store);
  assert.equal(isThrottled(1_000_000 + THROTTLE_MS, store), false);
});

test('a corrupt stored value does not permanently lock the form', () => {
  assert.equal(isThrottled(1_000_000, fakeStore({ mga_sub_last: 'garbage' })), false);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/subscribe.test.mjs`
Expected: FAIL — module not found

- [ ] **Step 3: Write the pure validation module**

```javascript
// js/subscribe-validate.js
// DOM-free helpers for the subscribe form, so they can be unit-tested in Node.
export const THROTTLE_KEY = 'mga_sub_last';
export const THROTTLE_MS = 60_000;

export function isValidEmail(email) {
  return typeof email === 'string'
    && email.length >= 5
    && email.length <= 254
    && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

export function isThrottled(now, store) {
  const raw = store.getItem(THROTTLE_KEY);
  const last = Number(raw);
  if (!Number.isFinite(last) || last <= 0) return false;
  return now - last < THROTTLE_MS;
}

export function markSubmitted(now, store) {
  store.setItem(THROTTLE_KEY, String(now));
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/subscribe.test.mjs`
Expected: PASS — 7 tests

- [ ] **Step 5: Write the form module**

```javascript
// js/subscribe.js
// Email capture for new-lesson notifications. Addressed to parents, teachers
// and learners 13+, consistent with privacy.html section 10.
import { db } from './firebase-config.js';
import {
  collection, addDoc, serverTimestamp,
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';
import { isValidEmail, isThrottled, markSubmitted } from './subscribe-validate.js';

export function mountSubscribeForm(container, source) {
  if (!container) return;

  container.innerHTML = `
    <form class="sub-form" novalidate>
      <h2 class="sub-title">Get new lessons by email</h2>
      <p class="sub-copy">For parents and teachers — and learners 13 or older.
        We email when new courses go live. No spam, and we never share your address.</p>
      <label class="sub-label" for="sub-email">Email address</label>
      <input class="sub-input" id="sub-email" type="email" name="email"
             autocomplete="email" required placeholder="you@example.com">
      <label class="sub-label" for="sub-role">I am a</label>
      <select class="sub-input" id="sub-role" name="role">
        <option value="parent">Parent or guardian</option>
        <option value="teacher">Teacher</option>
        <option value="learner">Learner, 13 or older</option>
      </select>
      <label class="sub-check">
        <input type="checkbox" id="sub-ok" name="ok">
        <span>I'm 13 or older, or a parent or teacher signing up on my own behalf.</span>
      </label>
      <input class="sub-hp" type="text" name="website" tabindex="-1" autocomplete="off"
             aria-hidden="true">
      <button class="sub-btn" type="submit" disabled>Notify me</button>
      <p class="sub-msg" role="status" aria-live="polite"></p>
    </form>`;

  const form = container.querySelector('.sub-form');
  const email = container.querySelector('#sub-email');
  const role = container.querySelector('#sub-role');
  const ok = container.querySelector('#sub-ok');
  const honeypot = container.querySelector('.sub-hp');
  const btn = container.querySelector('.sub-btn');
  const msg = container.querySelector('.sub-msg');

  ok.addEventListener('change', () => { btn.disabled = !ok.checked; });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    msg.textContent = '';

    if (honeypot.value !== '') return;            // bot; fail silently
    if (!ok.checked) { msg.textContent = 'Please confirm the checkbox first.'; return; }
    if (!isValidEmail(email.value.trim())) {
      msg.textContent = 'That email address does not look right.';
      return;
    }
    if (isThrottled(Date.now(), window.localStorage)) {
      msg.textContent = 'Just a moment — please try again shortly.';
      return;
    }

    btn.disabled = true;
    try {
      await addDoc(collection(db, 'subscribers'), {
        email: email.value.trim(),
        role: role.value,
        source: String(source).slice(0, 64),
        createdAt: serverTimestamp(),
      });
      markSubmitted(Date.now(), window.localStorage);
      form.innerHTML = '<p class="sub-msg">Thanks — you\'re on the list.</p>';
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'subscribe', { source, role: role.value });
      }
    } catch (err) {
      console.error('[subscribe] write failed', err);
      msg.textContent = 'Something went wrong. Please try again later.';
      btn.disabled = false;
    }
  });
}
```

- [ ] **Step 6: Append the styles**

Append to `css/global.css`:

```css
/* ---- Email capture ---- */
.sub-form { max-width: 460px; margin: 48px auto; padding: 28px 24px;
  border: 1px solid rgba(255,255,255,0.10); border-radius: 14px; background: rgba(255,255,255,0.03); }
.sub-title { font-size: 1.3rem; font-weight: 800; margin-bottom: 8px; }
.sub-copy { font-size: 0.9rem; color: var(--color-text-secondary); line-height: 1.55; margin-bottom: 18px; }
.sub-label { display: block; font-size: 0.8rem; font-weight: 700; margin: 12px 0 6px; }
.sub-input { width: 100%; padding: 11px 13px; font-size: 1rem; border-radius: 9px;
  border: 1px solid rgba(255,255,255,0.16); background: rgba(0,0,0,0.25); color: inherit; }
.sub-check { display: flex; gap: 9px; align-items: flex-start; margin: 16px 0;
  font-size: 0.82rem; color: var(--color-text-secondary); line-height: 1.45; }
.sub-hp { position: absolute; left: -9999px; width: 1px; height: 1px; opacity: 0; }
.sub-btn { width: 100%; padding: 12px; font-size: 1rem; font-weight: 700; border: 0;
  border-radius: 9px; background: var(--color-primary); color: #0c1020; cursor: pointer; }
.sub-btn:disabled { opacity: 0.45; cursor: not-allowed; }
.sub-msg { margin-top: 10px; font-size: 0.85rem; color: var(--color-text-secondary); min-height: 1.2em; }
```

- [ ] **Step 7: Mount on the five mapped course pages**

On each of the 5 pages from Task 8, insert before the `<footer class="footer">` element:

```html
  <div id="subscribe"></div>
```

And in the module script, add (substituting the real slug):

```javascript
    import { mountSubscribeForm } from '../../js/subscribe.js';
    mountSubscribeForm(document.getElementById('subscribe'), 'calculus');
```

Do **not** mount it on any `lesson-*.html` page — the form stays out of kid-facing lesson flows.

- [ ] **Step 8: Verify against live Firestore in a browser**

```bash
cd /Users/dakotabrown/rehan-calculus-local && node scripts/serve_local.mjs &
```

At `http://localhost:8000/courses/calculus/`:
1. Submit button starts disabled; checking the box enables it.
2. A bad address (`nope`) shows the validation message and writes nothing.
3. A valid address shows "Thanks — you're on the list."
4. The document appears in the Firebase console under `subscribers` with `email`, `role`, `source: "calculus"`, `createdAt`.
5. Submitting again immediately shows the throttle message.
6. In the console, `await getDocs(collection(db,'subscribers'))` is **denied** — reads must fail.

Stop the server afterward.

- [ ] **Step 9: Run all tests and commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/*.test.mjs' 'tests/pinterest/*.test.mjs'
git add js/subscribe.js js/subscribe-validate.js tests/subscribe.test.mjs css/global.css courses/calculus/index.html courses/circuits/index.html courses/clustering-and-classification/index.html courses/algebra/index.html courses/social-media-rules/index.html
git commit -m "Add email capture form backed by Firestore

Honeypot plus a 60s client throttle; role gate and affirmation keep the
form aimed at parents, teachers and learners 13+, never kid lesson flows."
```

---

### Task 14: Privacy policy corrections

**Files:**
- Modify: `privacy.html`

This task fixes a **pre-existing false statement**: line 83 claims Mathagram does not use Google Analytics, while GA4 `G-1JKG4MN6XX` has been live site-wide via `nav.js`. That correction is required regardless of this feature.

- [ ] **Step 1: Correct the analytics claim in §5**

Replace the sentence beginning `We do <strong>not</strong> use Google Analytics, Meta Pixel,` with:

```html
    <p><strong>Google Analytics 4</strong> — we use GA4 (measurement ID <code>G-1JKG4MN6XX</code>) to count page views and understand which courses are used, in aggregate. GA4 sets first-party cookies and records IP-derived approximate location. We do <strong>not</strong> use Meta Pixel, TikTok Pixel, Hotjar, Mixpanel, Segment, or any behavioral-advertising trackers. We do <strong>not</strong> sell or rent your personal information to anyone.</p>
```

- [ ] **Step 2: Disclose the YouTube embed in §5**

Insert after the KaTeX CDN paragraph:

```html
    <p><strong>YouTube (youtube-nocookie.com)</strong> — some course pages show a video thumbnail image served from Google. <em>No YouTube player, script, or cookie loads until you click play.</em> Once you click, playback is provided by YouTube in privacy-enhanced mode under <a href="https://policies.google.com/privacy" style="color: var(--color-primary-dark); text-decoration: underline;">Google&rsquo;s Privacy Policy</a>.</p>
```

- [ ] **Step 3: Disclose email collection in §1**

Insert after the `<strong>Learning Post content.</strong>` paragraph:

```html
    <p><strong>Email updates (optional).</strong> If you submit the &ldquo;Get new lessons by email&rdquo; form, we store the email address you enter, the role you select (parent, teacher, or learner 13+), and which page you signed up from. This is separate from your account and is used only to email you when new courses go live. This form is intended for parents, teachers, and learners aged 13 or older, and is never shown inside lessons. We do not share or sell this list. To be removed, contact us using the Contact section below.</p>
```

- [ ] **Step 4: Cover the subscribe list in §7 Data Retention**

Append to the §7 paragraph:

```html
 Email-update subscriptions are retained until you ask to be removed; contact us using the Contact section below and we will delete your address within 30 days.
```

- [ ] **Step 5: Disclose the throttle key in §11**

In §11, change the localStorage list to include the subscribe throttle by replacing `and current strike count` with:

```html
current strike count, and a timestamp that rate-limits the email-signup form
```

- [ ] **Step 6: Update the policy date**

Change `<span id="last-updated">June 17, 2026</span>` to `<span id="last-updated">July 26, 2026</span>`.

- [ ] **Step 7: Verify**

```bash
cd /Users/dakotabrown/rehan-calculus-local
grep -c 'We do <strong>not</strong> use Google Analytics' privacy.html
grep -c 'G-1JKG4MN6XX' privacy.html
grep -c 'youtube-nocookie' privacy.html
grep -c 'Email updates (optional)' privacy.html
grep -c 'July 26, 2026' privacy.html
```
Expected: `0`, `1`, `1`, `1`, `1`. Then load `http://localhost:8000/privacy.html` and confirm the sections render with correct numbering.

- [ ] **Step 8: Get user approval on the wording, then commit**

Show the user the rendered diff of all five edits and get explicit approval before committing — this is a legal document.

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add privacy.html
git commit -m "Privacy: correct false GA claim; disclose email capture and YouTube

Section 5 stated we do not use Google Analytics while GA4 G-1JKG4MN6XX
has been live site-wide via nav.js. Also documents the optional email
list, the click-to-play YouTube embed, and the signup throttle key."
```

---

## Phase F — Measurement and ship

### Task 15: Playbook, channel link, and production deploy

**Files:**
- Create: `docs/pinterest-playbook.md`
- Modify: `index.html` (footer channel link)

- [ ] **Step 1: Add the channel link to the homepage footer**

Inside the `<div class="footer-links">` element in `index.html`, add:

```html
        <a href="https://www.youtube.com/@Mathagram_Org" target="_blank" rel="noopener">YouTube</a>
```

- [ ] **Step 2: Write the playbook**

```markdown
# Pinterest Playbook

## UTM convention

Every pin's destination URL carries:

?utm_source=pinterest&utm_medium=social&utm_campaign=<course-slug>&utm_content=v<1|2|3>

`utm_content` identifies which of the three pin designs earned the click. That is
the field that tells you which creative to scale — check it before spending on ads.

Example:
https://mathagram.org/courses/calculus/?utm_source=pinterest&utm_medium=social&utm_campaign=calculus&utm_content=v2

## Pin assets

`assets/pins/<slug>-v1.png` … `-v3.png`, 1000x1500. Regenerate after course
titles or lesson counts change:

    node scripts/pinterest/gen-pins.mjs --limit=40

## Metadata

Re-run after editing course descriptions (idempotent):

    node scripts/pinterest/add-course-meta.mjs --pins

## GA4 events

- `video_play` — params `video_id`, `course`. Fires when a facade is clicked.
- `subscribe` — params `source`, `role`. Fires on a successful Firestore write.

View in GA4 (G-1JKG4MN6XX) under Reports → Engagement → Events.

## Pin copy convention — search-oriented

Pinterest indexes the pin **description** as search text. Text baked into the
image is not a meaningful ranking signal, so the two are written differently:

- **Descriptions** lead with the phrase people type, then carry secondary terms
  in natural prose. Generated by `buildPinDescription()`, e.g. *"Free Calculus
  lessons — 1312 step-by-step math exercises you can start right now.
  Interactive practice, no signup, no app. Great for homeschool, classroom, and
  self-study."* The `homeschool` / `classroom` / `self-study` terms are
  deliberate: they are high-volume searches in this niche.
- **Image text** may use a curiosity hook (`v3-hook.svg`) — its job is
  converting an impression into a click, not surfacing the pin.

No hashtags. Pinterest deprecated their ranking value and they read as spam.

## Operating cadence

- 3–5 fresh pins/day. Fresh means a new image, not a repin. Three variants per
  course is why the generator exists.
- Board names and pin descriptions are keyword-ranked — use Pinterest's search
  autocomplete for phrasing.
- Expect a 45–90 day ramp. Judge on outbound clicks and cost per signup, never
  impressions.
- Run ads only after organic data shows which variant converts.

## Verifying the funnel works

YouTube Studio → Analytics → Traffic sources → External should show
`mathagram.org` rising. That is monetizable watch time.

## Known limitation

The channel's 10 videos total 10m45s (~65s average). Embeds produce real but
small watch time; reaching 4,000 watch hours needs longer videos or the Shorts
path (10M Shorts views in 90 days). See the design spec.
```

- [ ] **Step 3: Run the full test suite**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/*.test.mjs' 'tests/pinterest/*.test.mjs'
```
Expected: all tests pass. Do not deploy on a red suite.

- [ ] **Step 4: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add docs/pinterest-playbook.md index.html
git commit -m "Add Pinterest playbook and YouTube channel link"
```

- [ ] **Step 5: Deploy with the mandatory 5-path clean**

`git push` does **not** publish mathagram.org. The Netlify CLI regenerates
`.netlify/netlify.toml` after every deploy, and its presence makes the next deploy ship an
empty manifest that Netlify reports as `state=ready` while serving 404s.

```bash
cd /Users/dakotabrown/rehan-calculus-local
rm -rf /Users/dakotabrown/rehan-calculus-local/.netlify/v1 \
       /Users/dakotabrown/rehan-calculus-local/.netlify/functions-internal \
       /Users/dakotabrown/rehan-calculus-local/.netlify/netlify.toml \
       /Users/dakotabrown/rehan-calculus-local/.netlify/edge-functions-dist \
       /Users/dakotabrown/rehan-calculus-local/.netlify/edge-functions-import-map.json
netlify deploy --prod --dir=/Users/dakotabrown/rehan-calculus-local
```

Keep `.netlify/state.json` so the site stays linked. **Check two things in the output before
trusting it:** the `Deploy path:` line must read `/Users/dakotabrown/rehan-calculus-local`
(a stale `cd` silently deploys a subdirectory), and the hashing count must be in the hundreds.
A "deploy complete" after only 1–3 seconds means nothing uploaded.

- [ ] **Step 6: Verify production**

```bash
for u in / /courses.html /courses/calculus/ /privacy.html /assets/pins/calculus-v1.png; do
  printf '%s -> %s\n' "$u" "$(curl -s -o /dev/null -w '%{http_code}' "https://mathagram.org$u")"
done
curl -sI https://mathagram.org/courses/calculus/ | grep -i content-security-policy | grep -c 'youtube-nocookie'
curl -s https://mathagram.org/courses/calculus/ | grep -c 'og:title'
```
Expected: five `200`s, `1` for the CSP check, `1` for the OG check.

If any page 404s, do **not** redeploy repeatedly. Restore the last good deploy first:

```bash
netlify api listSiteDeploys --data '{"site_id":"6672e8dc-f0f8-4c73-a72a-9b8e7506b28b","per_page":5}'
netlify api restoreSiteDeploy --data '{"site_id":"6672e8dc-f0f8-4c73-a72a-9b8e7506b28b","deploy_id":"<last-good>"}'
```

Then run the 5-path clean and deploy exactly once more.

- [ ] **Step 7: Confirm the embed works under production CSP**

Open `https://mathagram.org/courses/calculus/` in a browser. Confirm the thumbnail renders,
the console shows **no CSP violation**, and clicking plays the video. This is the check that
local serving cannot perform, because `scripts/serve_local.mjs` does not apply `_headers`.

- [ ] **Step 8: Re-submit changed URLs to IndexNow**

341 course pages gained canonical tags and descriptions, so tell Bing/Yandex.

```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  "https://api.indexnow.org/IndexNow?url=https://mathagram.org/&key=625faecf69179d0d47639ee87c78f1e1"
```
Expected: `200` or `202`.

- [ ] **Step 9: Report the remaining manual steps**

Tell the user, explicitly, what is still outstanding:
1. Replace `PINTEREST_VERIFICATION_CODE_GOES_HERE` in `index.html` and redeploy — Pinterest analytics and Rich Pins are inactive until then.
2. Create the Pinterest business account, claim the domain, and build keyword-named boards.
3. Validate a course URL in Pinterest's Rich Pin validator once claimed.
4. Pin variants v2/v3 manually from `assets/pins/`; only v1 is wired to the save button.

---

### Task 16: "Save to Pinterest" button

**Depends on:** Task 2 (`buildPinElement`) and Task 11 (body injection). Run after both.

**Files:**
- Modify: `scripts/pinterest/lib/meta-block.mjs`
- Modify: `tests/pinterest/meta-block.test.mjs`
- Modify: `css/global.css` (append)
- Re-run: `scripts/pinterest/add-course-meta.mjs --pins` (updates the 40 pinned course pages)

**Why this exists:** with ads off the table, organic reach depends on visitors pinning pages
themselves. A save button turns every reader into a distributor.

**Interfaces:**
- Produces: `buildPinSaveUrl({ pageUrl, imageUrl, description }): string`
- Produces: `buildPinDescription(course): string`
- Changes: `buildPinElement(course, pinPath)` now emits a visible `<a>` save button in
  addition to the hidden `data-pin-media` image, and sources its description from
  `buildPinDescription()` instead of the interim string Task 2 used

**Search-oriented description copy (user decision, 2026-07-27).** Pinterest indexes the pin
*description* as search text; text baked into the image is not a meaningful ranking signal. So
descriptions lead with the phrase people actually type and carry secondary terms, rather than
using a curiosity hook:

- Click-oriented (rejected): `Still stuck on Integrals? 🤯`
- Search-oriented (adopted): `Free Calculus lessons — 1312 step-by-step math exercises you can
  start right now. Interactive practice, no signup, no app. Great for homeschool, classroom,
  and self-study.`

`homeschool`, `classroom`, and `self-study` are deliberate — they are high-volume Pinterest
searches in this niche. The `v3-hook.svg` template keeps its visual hook; image text converts
the impression into a click and is not what surfaces the pin in the first place.

**No third-party JavaScript and no CSP change.** Pinterest's official `pinit.js` widget is
deliberately *not* used — it would need a new `script-src` entry, load third-party JS, and set
cookies on every course page. Instead the Pinterest pin-create URL is built at **build time**
in Node and injected as a plain anchor. Zero runtime JS, zero CSP impact, works with JS
disabled.

The save link carries `utm_content=save` so GA4 distinguishes visitor-initiated saves from
the pins you publish yourself.

- [ ] **Step 1: Write the failing test**

Append to `tests/pinterest/meta-block.test.mjs`:

```javascript
test('buildPinDescription leads with the search phrase and carries niche keywords', () => {
  const d = buildPinDescription(COURSE);
  assert.ok(d.startsWith('Free Algebra & "Friends" lessons'), `got: ${d}`);
  assert.ok(d.includes('1312 step-by-step math exercises'));
  assert.ok(d.includes('homeschool'));
  assert.ok(d.includes('classroom'));
  assert.ok(d.includes('self-study'));
  assert.ok(d.length <= 350, `descriptions stay short enough to display: ${d.length}`);
});

test('buildPinDescription omits the count when lesson counts are unavailable', () => {
  const d = buildPinDescription({ ...COURSE, totalLessons: null });
  assert.ok(d.includes('step-by-step math exercises'));
  assert.ok(!/\bnull\b/.test(d), 'null must never leak into copy');
  assert.ok(!/\d/.test(d.split('—')[1].split('.')[0]), 'no stray number in the scale clause');
});

test('buildPinDescription falls back when the course has no category', () => {
  const d = buildPinDescription({ ...COURSE, category: '' });
  assert.ok(d.includes('step-by-step lessons'), `got: ${d}`);
  assert.ok(!d.includes('undefined'));
});

test('buildPinSaveUrl targets Pinterest pin-create with encoded params', () => {
  const url = buildPinSaveUrl({
    pageUrl: 'https://mathagram.org/courses/algebra/',
    imageUrl: 'https://mathagram.org/assets/pins/algebra-v1.png',
    description: 'Algebra & "Friends" — free lessons',
  });
  assert.ok(url.startsWith('https://www.pinterest.com/pin/create/button/?'));
  assert.ok(url.includes('url=https%3A%2F%2Fmathagram.org%2Fcourses%2Falgebra%2F'));
  assert.ok(url.includes('media=https%3A%2F%2Fmathagram.org%2Fassets%2Fpins%2Falgebra-v1.png'));
  assert.ok(url.includes('description=Algebra%20%26%20%22Friends%22'));
  assert.ok(!url.includes(' '), 'no raw spaces may survive encoding');
});

test('buildPinSaveUrl tags the destination so saves are attributable', () => {
  const url = buildPinSaveUrl({
    pageUrl: 'https://mathagram.org/courses/algebra/',
    imageUrl: 'https://mathagram.org/assets/pins/algebra-v1.png',
    description: 'x',
  });
  assert.ok(url.includes('utm_source%3Dpinterest'));
  assert.ok(url.includes('utm_content%3Dsave'));
});

test('buildPinElement emits a visible save anchor alongside the hidden image', () => {
  const b = buildPinElement(COURSE, '/assets/pins/algebra-v1.png');
  assert.ok(b.includes('class="pin-save"'));
  assert.ok(b.includes('href="https://www.pinterest.com/pin/create/button/?'));
  assert.ok(b.includes('rel="noopener"'));
  assert.ok(b.includes('target="_blank"'));
  assert.ok(b.includes('Save to Pinterest'));
  // the hidden media image must still be present
  assert.ok(b.includes('data-pin-media='));
  assert.ok(b.includes('style="display:none"'));
});
```

Add `buildPinSaveUrl` and `buildPinDescription` to the existing import list at the top of the
test file.

**One existing Task 2 assertion must also be updated.** Task 2's test
`buildPinElement emits a hidden img with absolute pin media` asserts:

```javascript
  assert.ok(b.includes('data-pin-description="Algebra &amp; &quot;Friends&quot;'));
```

That was written against Task 2's interim description, which began with the course title. The
search-oriented description begins with `Free `, so change that assertion to:

```javascript
  assert.ok(b.includes('data-pin-description="Free Algebra &amp; &quot;Friends&quot; lessons'));
```

Do not delete the assertion — it is still the only check that the description reaches the
attribute escaped.

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/meta-block.test.mjs`
Expected: FAIL — `buildPinSaveUrl is not a function`

- [ ] **Step 3: Implement**

Add to `scripts/pinterest/lib/meta-block.mjs`:

```javascript
// Search-oriented pin copy. Pinterest indexes the description as search text, so
// this leads with the phrase people type and carries the niche's high-volume
// secondary terms (homeschool / classroom / self-study) in natural prose.
// Deliberately NOT a curiosity hook — hooks spike then die; search copy compounds.
export function buildPinDescription(course) {
  const subject = course.category ? `${course.category.toLowerCase()} ` : '';
  const scale = course.totalLessons
    ? `${course.totalLessons} step-by-step ${subject}exercises`
    : `step-by-step ${subject}lessons`;
  return `Free ${course.title} lessons — ${scale} you can start right now. `
    + 'Interactive practice, no signup, no app. '
    + 'Great for homeschool, classroom, and self-study.';
}

export function buildPinSaveUrl({ pageUrl, imageUrl, description }) {
  const dest = new URL(pageUrl);
  dest.searchParams.set('utm_source', 'pinterest');
  dest.searchParams.set('utm_medium', 'social');
  dest.searchParams.set('utm_content', 'save');
  const q = new URLSearchParams({
    url: dest.toString(),
    media: imageUrl,
    description,
  });
  // URLSearchParams encodes spaces as '+'; Pinterest handles %20 more reliably.
  return `https://www.pinterest.com/pin/create/button/?${q.toString().replace(/\+/g, '%20')}`;
}
```

Then extend `buildPinElement` to append the anchor before `PIN_END`:

```javascript
export function buildPinElement(course, pinPath) {
  const pinDesc = buildPinDescription(course);
  const desc = escapeAttr(pinDesc);
  const saveUrl = escapeAttr(buildPinSaveUrl({
    pageUrl: course.url,
    imageUrl: `${SITE}${pinPath}`,
    description: pinDesc,
  }));
  const src = escapeAttr(pinPath);
  const media = escapeAttr(`${SITE}${pinPath}`);
  return [
    PIN_START,
    `  <img src="${src}" alt="" width="1000" height="1500" style="display:none"`,
    `       data-pin-media="${media}" data-pin-description="${desc}">`,
    `  <p class="pin-save-wrap">`,
    `    <a class="pin-save" href="${saveUrl}" target="_blank" rel="noopener"`,
    `       data-pin-do="none">Save to Pinterest</a>`,
    `  </p>`,
    PIN_END,
  ].join('\n');
}
```

`data-pin-do="none"` stops Pinterest's browser extension from decorating the anchor as a
nested pin widget.

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Users/dakotabrown/rehan-calculus-local && node --test tests/pinterest/meta-block.test.mjs`
Expected: PASS — all meta-block tests including the 3 new ones

- [ ] **Step 5: Append the styles**

Append to `css/global.css`:

```css
/* ---- Save to Pinterest ---- */
.pin-save-wrap { text-align: center; margin: 0 0 32px; }
.pin-save {
  display: inline-block; padding: 9px 18px; font-size: 0.85rem; font-weight: 700;
  color: #fff; background: #e60023; border-radius: 999px; text-decoration: none;
}
.pin-save:hover, .pin-save:focus-visible { background: #ad081b; }
```

- [ ] **Step 6: Re-run the injector and confirm idempotency**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node scripts/pinterest/add-course-meta.mjs --pins
SLUG=$(node scripts/pinterest/top-courses.mjs 1)
sed -n '/pin:media:start/,/pin:media:end/p' "courses/$SLUG/index.html"
node scripts/pinterest/add-course-meta.mjs --pins
git status --short courses/ | wc -l
```
Expected: the first run reports `changed=40`; the printed block shows both the hidden image and
the save anchor; the second run reports `changed=0` and adds no further modifications.

- [ ] **Step 7: Verify in a browser**

Serve locally and open a pinned course page. Confirm the red "Save to Pinterest" button renders,
and that clicking it opens Pinterest's pin-create dialog **pre-filled with the vertical
1000×1500 image** (not the landscape og-card). Confirm the Network tab shows **no request to any
Pinterest domain before the click**.

- [ ] **Step 8: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
node --test 'tests/*.test.mjs' 'tests/pinterest/*.test.mjs'
git add scripts/pinterest/lib/meta-block.mjs tests/pinterest/meta-block.test.mjs css/global.css courses/
git commit -m "Add Save to Pinterest button to pinned course pages

Build-time pin-create URL injected as a plain anchor — no pinit.js, no
third-party JS, no CSP change. Tagged utm_content=save so visitor saves
are distinguishable from published pins."
```

---

## Self-Review

**Spec coverage:** §1 domain claim → Task 5. §2 Rich Pin metadata → Tasks 1–4. §3 pin images → Tasks 9–11. §4 embeds → Tasks 6–8. §5 email capture → Tasks 12–13. §6 measurement → Tasks 8, 13, 15. Privacy policy → Task 14. Deploy → Task 15. No spec section is unimplemented.

**Deviations from the spec, and why:**
1. **Pin element moved from `<head>` to `<body>`.** An `<img>` in `<head>` is invalid HTML; browsers hoist it into the body, which would corrupt the delimited head block on re-injection. Task 2 splits the two builders and Task 11 verifies placement.
2. **Thumbnails use `hqdefault.jpg`, not `maxresdefault.jpg`.** Max-res does not exist for every upload — notably short vertical videos, which most of this channel's content is — and would render broken images.
3. **`autoplay=1` is applied in the click handler.** The spec said "autoplay is never used," which was aimed at page-load autoplay. Post-click autoplay is user-initiated, is not a filtered-view risk, and avoids forcing a second click. The global constraint is worded to make the distinction explicit.
4. **Validation helpers split into `js/subscribe-validate.js`.** `js/subscribe.js` imports the Firebase CDN at module scope, so it cannot be imported by `node --test`. The DOM-free split makes the logic testable.
5. **Task 14 fixes a pre-existing privacy-policy error** not mentioned in the spec: §5 denied using Google Analytics while GA4 is live. Discovered while reading the file for the email disclosure.

**Placeholder scan:** the only literal placeholder is `PINTEREST_VERIFICATION_CODE_GOES_HERE`, which is an intentional, documented handoff to the user (Task 5 Step 4, Task 15 Step 9). No TBDs, and every code step contains runnable code.

**Type consistency:** `CourseData` fields (`slug`, `title`, `description`, `category`, `totalLessons`, `unitCount`, `url`) are produced in Task 1 and consumed unchanged in Tasks 2, 4, 10, 11. `injectBlock(html, block, {start, end, before})` has one signature, used in Tasks 4 and 11. `videoForCourse` is defined in Task 6 and used in Task 8. `isValidEmail` / `isThrottled` / `markSubmitted` / `THROTTLE_MS` are defined in Task 13 Step 3 and consumed by its own test and form. The Firestore document shape in Task 13 (`email`, `role`, `source`, `createdAt`) exactly matches the `hasOnly([...])` allow-list in Task 12.
