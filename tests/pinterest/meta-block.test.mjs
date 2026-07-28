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

test('buildMetaBlock escapes the course url into attributes', () => {
  const b = buildMetaBlock({ ...COURSE, url: 'https://mathagram.org/c/a"b&c/' });
  assert.ok(b.includes('href="https://mathagram.org/c/a&quot;b&amp;c/"'));
  assert.ok(!b.includes('a"b&c'), 'raw quote/ampersand must not survive');
});

test('buildPinElement escapes the pin path into attributes', () => {
  const b = buildPinElement(COURSE, '/assets/pins/a"b&c-v1.png');
  assert.ok(b.includes('src="/assets/pins/a&quot;b&amp;c-v1.png"'));
  assert.ok(!b.includes('a"b&c-v1.png'), 'raw quote/ampersand must not survive');
});
