// Idempotent delimited-block injection into an HTML string.
export function injectBlock(html, block, { start, end, before }) {
  const s = html.indexOf(start);
  const e = html.indexOf(end, s === -1 ? 0 : s);
  if (s !== -1 && e !== -1 && e > s) {
    return html.slice(0, s) + block + html.slice(e + end.length);
  }
  const at = html.indexOf(before);
  if (at === -1) throw new Error(`injectBlock: anchor ${before} not found`);
  return html.slice(0, at) + block + '\n' + html.slice(at);
}
