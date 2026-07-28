// Reproduce listening-practice behavior on a lesson page UNDER THE EXACT
// PRODUCTION CSP, in real (headless) Chrome via the DevTools Protocol.
// Captures: console messages, uncaught exceptions, CSP violations, failed requests.
import http from 'node:http';
import { spawn } from 'node:child_process';
import { readFileSync, existsSync, statSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const PAGE = process.argv[2] || '/courses/trigonometry/lesson-6.html';
const PORT = 8799;
const DBG = 9223;
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// EXACT production CSP copied from _headers (the /*.html block).
const CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://www.gstatic.com https://apis.google.com https://www.googletagmanager.com https://translate.google.com https://translate.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net https://www.gstatic.com https://translate.googleapis.com; font-src 'self' https://fonts.gstatic.com https://www.gstatic.com https://translate.googleapis.com; img-src 'self' data: https://translate.googleapis.com https://translate.google.com https://www.google.com https://www.gstatic.com https://www.google-analytics.com https://*.google-analytics.com; frame-src 'self' https://mathagram-cb526.firebaseapp.com https://accounts.google.com https://apis.google.com https://translate.googleapis.com https://translate.google.com; connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com https://www.googletagmanager.com https://firestore.googleapis.com https://identitytoolkit.googleapis.com https://securetoken.googleapis.com https://www.googleapis.com https://mathagram-cb526.firebaseapp.com https://translate.googleapis.com https://translate.google.com;";

const MIME = { '.html':'text/html', '.js':'text/javascript', '.mjs':'text/javascript',
  '.css':'text/css', '.json':'application/json', '.svg':'image/svg+xml',
  '.png':'image/png', '.m4a':'audio/mp4', '.woff2':'font/woff2', '.ico':'image/x-icon' };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  let fp = path.join(ROOT, p);
  if (existsSync(fp) && statSync(fp).isDirectory()) fp = path.join(fp, 'index.html');
  const ext = path.extname(fp);
  // Apply the production CSP to EVERY response, exactly as prod would for HTML.
  res.setHeader('Content-Security-Policy', CSP);
  if (ext === '.js' || ext === '.css' || ext === '.svg') res.setHeader('Access-Control-Allow-Origin', '*');
  if (!existsSync(fp)) { res.writeHead(404); return res.end('404 ' + p); }
  res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
  res.end(readFileSync(fp));
});

const cdp = (() => {
  let ws, id = 0; const waiters = new Map(); const handlers = [];
  return {
    async connect(url) {
      ws = new WebSocket(url);
      await new Promise((ok, no) => { ws.onopen = ok; ws.onerror = no; });
      ws.onmessage = (m) => {
        const msg = JSON.parse(m.data);
        if (msg.id && waiters.has(msg.id)) { waiters.get(msg.id)(msg.result); waiters.delete(msg.id); }
        else if (msg.method) handlers.forEach(h => h(msg));
      };
    },
    send(method, params = {}, sessionId) {
      const mid = ++id;
      ws.send(JSON.stringify({ id: mid, method, params, sessionId }));
      return new Promise(r => waiters.set(mid, r));
    },
    on(fn) { handlers.push(fn); },
  };
})();

const events = { console: [], exceptions: [], csp: [], failed: [] };

await new Promise(r => server.listen(PORT, '127.0.0.1', r));

const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${DBG}`,
  '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  '--user-data-dir=/tmp/repro-listening-prof', 'about:blank'],
  { stdio: 'ignore' });

async function getWsUrl() {
  for (let i = 0; i < 50; i++) {
    try { const j = await (await fetch(`http://127.0.0.1:${DBG}/json/version`)).json();
      if (j.webSocketDebuggerUrl) return j.webSocketDebuggerUrl; } catch {}
    await new Promise(r => setTimeout(r, 200));
  }
  throw new Error('Chrome CDP not reachable');
}

const report = [];
try {
  await cdp.connect(await getWsUrl());
  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });

  cdp.on((msg) => {
    if (msg.sessionId !== sessionId) return;
    const p = msg.params || {};
    if (msg.method === 'Runtime.consoleAPICalled')
      events.console.push(`[${p.type}] ` + p.args.map(a => a.value ?? a.description ?? a.unserializableValue ?? '').join(' '));
    if (msg.method === 'Runtime.exceptionThrown')
      events.exceptions.push(p.exceptionDetails?.exception?.description || p.exceptionDetails?.text || JSON.stringify(p.exceptionDetails));
    if (msg.method === 'Log.entryAdded') {
      const e = p.entry;
      if (e.source === 'security' || /Content Security Policy|Refused to/i.test(e.text || ''))
        events.csp.push(`${e.text}`);
      else if (e.level === 'error') events.console.push(`[log.error] ${e.text}`);
    }
    if (msg.method === 'Network.loadingFailed')
      events.failed.push(`${p.type} ${p.errorText} ${p.requestId}`);
  });

  await cdp.send('Runtime.enable', {}, sessionId);
  await cdp.send('Log.enable', {}, sessionId);
  await cdp.send('Network.enable', {}, sessionId);
  await cdp.send('Page.enable', {}, sessionId);
  await cdp.send('Page.navigate', { url: `http://127.0.0.1:${PORT}${PAGE}` }, sessionId);

  await new Promise(r => setTimeout(r, 5000));

  // Probe the live DOM: did the listening exercise actually render?
  const probe = await cdp.send('Runtime.evaluate', { expression: `(() => {
    const q = (s) => document.querySelector(s);
    return JSON.stringify({
      title: document.title,
      hasListeningArea: !!q('.listening-area'),
      hasVolumeBtn: !!q('.listening-volume-btn'),
      hint: q('.listening-hint') ? q('.listening-hint').textContent : null,
      exerciseHtmlLen: (q('.exercise-container')||{}).innerHTML?.length || 0,
      bodyTextSample: document.body.innerText.slice(0, 160)
    });
  })()`, returnByValue: true, sessionId }, sessionId);

  report.push('PAGE: ' + PAGE);
  report.push('DOM PROBE: ' + (probe.result?.value || JSON.stringify(probe)));
} catch (e) {
  report.push('HARNESS ERROR: ' + e.message);
} finally {
  console.log('\n========== REPRO REPORT (under production CSP) ==========');
  console.log(report.join('\n'));
  const show = (name, arr) => { console.log(`\n--- ${name} (${arr.length}) ---`); arr.slice(0, 20).forEach(x => console.log('  • ' + x)); };
  show('CSP VIOLATIONS', events.csp);
  show('UNCAUGHT EXCEPTIONS', events.exceptions);
  show('FAILED REQUESTS', events.failed);
  show('CONSOLE', events.console);
  chrome.kill('SIGKILL');
  server.close();
  setTimeout(() => process.exit(0), 300);
}
