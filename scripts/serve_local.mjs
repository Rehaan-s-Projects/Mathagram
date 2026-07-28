// Minimal static server for the repo root with correct JS-module MIME types,
// so ES-module pages (which can't load over file://) work in a real browser.
import http from 'node:http';
import { readFileSync, existsSync, statSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const PORT = Number(process.argv[2]) || 8123;
const MIME = { '.html':'text/html', '.js':'text/javascript', '.mjs':'text/javascript',
  '.css':'text/css', '.json':'application/json', '.svg':'image/svg+xml', '.png':'image/png',
  '.m4a':'audio/mp4', '.mp4':'video/mp4', '.woff2':'font/woff2', '.woff':'font/woff',
  '.ttf':'font/ttf', '.ico':'image/x-icon' };

http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  let fp = path.join(ROOT, p);
  if (existsSync(fp) && statSync(fp).isDirectory()) fp = path.join(fp, 'index.html');
  const ext = path.extname(fp);
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (!existsSync(fp)) { res.writeHead(404); return res.end('404 ' + p); }
  res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
  res.end(readFileSync(fp));
}).listen(PORT, '127.0.0.1', () => console.log(`serving ${ROOT} at http://127.0.0.1:${PORT}`));
