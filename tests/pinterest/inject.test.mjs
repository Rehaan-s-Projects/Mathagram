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

test('throws when a start delimiter has no matching end', () => {
  const dangling = '<head><!--s--><meta>text</head>';
  assert.throws(
    () => injectBlock(dangling, BLOCK, OPTS),
    /found.*with no matching/i
  );
});

test('throws when the anchor appears more than once', () => {
  // Scenario: script tag contains literal HTML with </head> inside it
  const ambiguous = '<head><script>const html = `<head>x</head>`;</script></head>';
  assert.throws(
    () => injectBlock(ambiguous, BLOCK, OPTS),
    /appears more than once/i
  );
});

test('is idempotent with both meta and pin blocks', () => {
  // Simulate the state after Task 4 (meta block in head) and Task 11 (pin block in body)
  const metaOpts = { start: '<!--m:start-->', end: '<!--m:end-->', before: '</head>' };
  const pinOpts = { start: '<!--p:start-->', end: '<!--p:end-->', before: '</body>' };
  const metaBlock = '<!--m:start-->\n  <meta>\n<!--m:end-->';
  const pinBlock = '<!--p:start-->\n  <img>\n<!--p:end-->';

  const html = '<html><head></head><body></body></html>';

  // Inject both blocks
  const with_meta = injectBlock(html, metaBlock, metaOpts);
  const with_both = injectBlock(with_meta, pinBlock, pinOpts);

  // Re-inject both blocks — should be idempotent
  const again_meta = injectBlock(with_both, metaBlock, metaOpts);
  const again_both = injectBlock(again_meta, pinBlock, pinOpts);

  assert.equal(with_both, again_both);
});

test('preserves exactly one of each block with two-block coexistence', () => {
  // Verify the state after injecting both meta and pin blocks
  const metaOpts = { start: '<!--m:start-->', end: '<!--m:end-->', before: '</head>' };
  const pinOpts = { start: '<!--p:start-->', end: '<!--p:end-->', before: '</body>' };
  const metaBlock = '<!--m:start-->\n  <meta>\n<!--m:end-->';
  const pinBlock = '<!--p:start-->\n  <img>\n<!--p:end-->';

  const html = '<html><head></head><body></body></html>';
  const with_meta = injectBlock(html, metaBlock, metaOpts);
  const with_both = injectBlock(with_meta, pinBlock, pinOpts);

  // Verify exactly one of each delimiter pair exists
  assert.equal(with_both.split('<!--m:start-->').length - 1, 1);
  assert.equal(with_both.split('<!--m:end-->').length - 1, 1);
  assert.equal(with_both.split('<!--p:start-->').length - 1, 1);
  assert.equal(with_both.split('<!--p:end-->').length - 1, 1);
});
