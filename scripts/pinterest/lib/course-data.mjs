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
