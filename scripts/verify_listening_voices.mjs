// VERIFY (TDD, under production CSP): the listening exercise reads questions
// in the Mathagram CHARACTER voice, not a generic voice.
// Spies on speechSynthesis.speak BEFORE page scripts run, then asserts the
// first auto-played question uses Edam's voice settings (pitch 0.8 / rate 0.9).
//
//   FAIL  -> generic voice (pitch 1.0 / rate 0.85)  == bug present
//   PASS  -> Edam's settings (pitch 0.8 / rate 0.9) == fixed
import http from 'node:http';
import { spawn } from 'node:child_process';
import { readFileSync, existsSync, statSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const PAGE = process.argv[2] || '/courses/trigonometry/lesson-6.html';
const PORT = 8801, DBG = 9224;
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://www.gstatic.com https://apis.google.com https://www.googletagmanager.com https://translate.google.com https://translate.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net https://www.gstatic.com https://translate.googleapis.com; font-src 'self' https://fonts.gstatic.com https://www.gstatic.com https://translate.googleapis.com; img-src 'self' data: https://translate.googleapis.com https://translate.google.com https://www.google.com https://www.gstatic.com https://www.google-analytics.com https://*.google-analytics.com; frame-src 'self' https://mathagram-cb526.firebaseapp.com https://accounts.google.com https://apis.google.com https://translate.googleapis.com https://translate.google.com; connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com https://www.googletagmanager.com https://firestore.googleapis.com https://identitytoolkit.googleapis.com https://securetoken.googleapis.com https://www.googleapis.com https://mathagram-cb526.firebaseapp.com https://translate.googleapis.com https://translate.google.com;";
const MIME = { '.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.json':'application/json', '.svg':'image/svg+xml', '.png':'image/png', '.m4a':'audio/mp4', '.woff2':'font/woff2', '.ico':'image/x-icon' };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  let fp = path.join(ROOT, p);
  if (existsSync(fp) && statSync(fp).isDirectory()) fp = path.join(fp, 'index.html');
  const ext = path.extname(fp);
  res.setHeader('Content-Security-Policy', CSP);
  if (ext === '.js' || ext === '.css' || ext === '.svg') res.setHeader('Access-Control-Allow-Origin', '*');
  if (!existsSync(fp)) { res.writeHead(404); return res.end('404 ' + p); }
  res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
  res.end(readFileSync(fp));
});

const cdp = (() => {
  let ws, id = 0; const waiters = new Map(); const handlers = [];
  return {
    async connect(url) { ws = new WebSocket(url);
      await new Promise((ok, no) => { ws.onopen = ok; ws.onerror = no; });
      ws.onmessage = (m) => { const msg = JSON.parse(m.data);
        if (msg.id && waiters.has(msg.id)) { waiters.get(msg.id)(msg.result); waiters.delete(msg.id); }
        else if (msg.method) handlers.forEach(h => h(msg)); }; },
    send(method, params = {}, sessionId) { const mid = ++id;
      ws.send(JSON.stringify({ id: mid, method, params, sessionId }));
      return new Promise(r => waiters.set(mid, r)); },
    on(fn) { handlers.push(fn); },
  };
})();

const cspViolations = [];
await new Promise(r => server.listen(PORT, '127.0.0.1', r));
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${DBG}`, '--disable-gpu',
  '--no-first-run', '--no-default-browser-check', '--user-data-dir=/tmp/verify-listening-prof', 'about:blank'], { stdio: 'ignore' });

async function getWsUrl() {
  for (let i = 0; i < 50; i++) { try { const j = await (await fetch(`http://127.0.0.1:${DBG}/json/version`)).json();
    if (j.webSocketDebuggerUrl) return j.webSocketDebuggerUrl; } catch {} await new Promise(r => setTimeout(r, 200)); }
  throw new Error('Chrome CDP not reachable');
}

let exitCode = 1;
try {
  await cdp.connect(await getWsUrl());
  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
  cdp.on((msg) => { if (msg.sessionId !== sessionId) return;
    if (msg.method === 'Log.entryAdded') { const e = msg.params.entry;
      if (e.source === 'security' || /Content Security Policy|Refused to/i.test(e.text || '')) cspViolations.push(e.text); } });
  await cdp.send('Runtime.enable', {}, sessionId);
  await cdp.send('Log.enable', {}, sessionId);
  await cdp.send('Page.enable', {}, sessionId);
  // Spy installed BEFORE any page script runs.
  await cdp.send('Page.addScriptToEvaluateOnNewDocument', { source: `
    window.__spoken = [];
    const _speak = window.speechSynthesis.speak.bind(window.speechSynthesis);
    window.speechSynthesis.speak = function(u) {
      try { window.__spoken.push({ text: (u.text||'').slice(0,40), pitch: u.pitch, rate: u.rate, voice: u.voice && u.voice.name || null }); } catch (e) {}
      return _speak(u);
    };
  ` }, sessionId);
  await cdp.send('Page.navigate', { url: `http://127.0.0.1:${PORT}${PAGE}` }, sessionId);
  await new Promise(r => setTimeout(r, 5500)); // 1.5s voicesReady + auto-play delay + margin

  const ev = await cdp.send('Runtime.evaluate', { expression: 'JSON.stringify(window.__spoken||[])', returnByValue: true, sessionId }, sessionId);
  // Ignore the silent warm-up utterance (volume 0 / rate 10).
  const spoken = JSON.parse(ev.result.value).filter(s => !(s.rate >= 5));

  console.log('\n========== VERIFY: listening uses character voice (under prod CSP) ==========');
  console.log('PAGE:', PAGE);
  console.log('CSP violations:', cspViolations.length, cspViolations.slice(0,5));
  console.log('Spoken utterances captured:', JSON.stringify(spoken, null, 2));

  // Edam's settings from VOICE_SETTINGS: pitch 0.8, rate 0.9.
  const first = spoken[0];
  const near = (a, b) => Math.abs(a - b) < 0.001;
  const usesEdam = first && near(first.pitch, 0.8) && near(first.rate, 0.9);
  const generic  = first && near(first.pitch, 1.0) && near(first.rate, 0.85);

  if (!first)        console.log('\nRESULT: ❓ INCONCLUSIVE — no question was spoken.');
  else if (usesEdam) { console.log('\nRESULT: ✅ PASS — question read in Edam\'s character voice (pitch 0.8 / rate 0.9).'); exitCode = 0; }
  else if (generic)  console.log('\nRESULT: ❌ FAIL — question read in the GENERIC voice (pitch 1.0 / rate 0.85). Character voices not used.');
  else               console.log(`\nRESULT: ❌ FAIL — unexpected voice settings (pitch ${first.pitch} / rate ${first.rate}).`);
  if (cspViolations.length) { console.log('RESULT: ❌ FAIL — CSP violations present.'); exitCode = 1; }
} catch (e) {
  console.log('HARNESS ERROR:', e.message);
} finally {
  chrome.kill('SIGKILL'); server.close();
  setTimeout(() => process.exit(exitCode), 300);
}
