// Idempotent delimited-block injection into an HTML string.
export function injectBlock(html, block, { start, end, before }) {
  const s = html.indexOf(start);
  const e = html.indexOf(end, s === -1 ? 0 : s);

  // If start is found but end is not (or comes before start), reject the malformed block
  if (s !== -1 && e === -1) {
    throw new Error(`injectBlock: found ${start} with no matching ${end}`);
  }

  if (s !== -1 && e !== -1 && e > s) {
    return html.slice(0, s) + block + html.slice(e + end.length);
  }

  const at = html.indexOf(before);
  if (at === -1) throw new Error(`injectBlock: anchor ${before} not found`);

  // Reject if anchor appears more than once (guards against embedded delimiters in script tags, etc.)
  if (html.indexOf(before, at + before.length) !== -1) {
    throw new Error(`injectBlock: anchor ${before} appears more than once`);
  }

  return html.slice(0, at) + block + '\n' + html.slice(at);
}
