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
