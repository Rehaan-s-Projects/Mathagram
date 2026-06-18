// js/typing-finger-guide.js
// "AI Camera Finger Guide" — shows a color-coded keyboard at the bottom of the
// screen, highlights the correct key on every keystroke, and tells the user
// which finger should press it.
//
// Auto-installs on /courses/typing-skills/* pages. Leaves other pages alone so
// the rest of the site isn't covered by a giant widget.

const FINGERS = {
  LP: { name: 'Left Pinky',  color: '#ef4444' },
  LR: { name: 'Left Ring',   color: '#f97316' },
  LM: { name: 'Left Middle', color: '#eab308' },
  LI: { name: 'Left Index',  color: '#22c55e' },
  TH: { name: 'Thumb',       color: '#6b7280' },
  RI: { name: 'Right Index', color: '#06b6d4' },
  RM: { name: 'Right Middle',color: '#3b82f6' },
  RR: { name: 'Right Ring',  color: '#8b5cf6' },
  RP: { name: 'Right Pinky', color: '#ec4899' }
};

// Standard touch-typing finger map for QWERTY. Each entry: [primary key,
// shifted key, finger key]. Spaces use TH.
const KEY_ROWS = [
  // Number row
  [
    ['`','~','LP'],['1','!','LP'],['2','@','LR'],['3','#','LM'],['4','$','LI'],['5','%','LI'],
    ['6','^','RI'],['7','&','RI'],['8','*','RM'],['9','(','RR'],['0',')','RP'],['-','_','RP'],['=','+','RP'],['Backspace','⌫','RP']
  ],
  // Top row
  [
    ['Tab','Tab','LP'],['q','Q','LP'],['w','W','LR'],['e','E','LM'],['r','R','LI'],['t','T','LI'],
    ['y','Y','RI'],['u','U','RI'],['i','I','RM'],['o','O','RR'],['p','P','RP'],['[','{','RP'],[']','}','RP'],['\\','|','RP']
  ],
  // Home row
  [
    ['CapsLock','Caps','LP'],['a','A','LP'],['s','S','LR'],['d','D','LM'],['f','F','LI'],['g','G','LI'],
    ['h','H','RI'],['j','J','RI'],['k','K','RM'],['l','L','RR'],[';',':','RP'],["'",'"','RP'],['Enter','↵','RP']
  ],
  // Bottom row
  [
    ['Shift','⇧','LP'],['z','Z','LP'],['x','X','LR'],['c','C','LM'],['v','V','LI'],['b','B','LI'],
    ['n','N','RI'],['m','M','RI'],[',','<','RM'],['.','>','RR'],['/','?','RP'],['Shift','⇧','RP']
  ],
  // Space row
  [
    ['Space',' ','TH']
  ]
];

let widget = null;
let messageEl = null;
let activeFlash = null;

function buildKeyEl(key, shifted, finger) {
  const f = FINGERS[finger];
  const el = document.createElement('div');
  el.className = 'tfg-key';
  el.dataset.key = key.toLowerCase();
  el.dataset.shift = shifted.toLowerCase();
  el.dataset.finger = finger;
  el.style.cssText = `
    background: ${f.color}15; border-bottom: 3px solid ${f.color};
    color: #e5e7eb; padding: 6px 4px; min-width: 22px; text-align: center;
    border-radius: 5px; font: 600 0.7rem 'SF Mono', Menlo, Consolas, monospace;
    transition: background 0.12s ease, transform 0.12s ease;
    user-select: none; box-sizing: border-box;
  `;
  // Long keys span more
  const long = ['Tab','CapsLock','Enter','Shift','Backspace','Space'];
  if (long.includes(key)) el.style.minWidth = key === 'Space' ? '180px' : '40px';
  if (key === 'Space') el.style.minWidth = '320px';
  el.textContent = (key === 'Space') ? '⎵ Space' : (key.length === 1 ? key.toUpperCase() : key);
  return el;
}

function buildKeyboard() {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'display:flex; flex-direction:column; gap:4px; align-items:center;';
  KEY_ROWS.forEach(row => {
    const rowEl = document.createElement('div');
    rowEl.style.cssText = 'display:flex; gap:3px; justify-content:center; flex-wrap:nowrap;';
    row.forEach(([k, s, f]) => rowEl.appendChild(buildKeyEl(k, s, f)));
    wrap.appendChild(rowEl);
  });
  return wrap;
}

// 10-finger introduction strip — visualizes each fingertip and its home-row key.
const FINGER_INTRO = [
  { code: 'LP',   label: 'Left Pinky',   home: 'A' },
  { code: 'LR',   label: 'Left Ring',    home: 'S' },
  { code: 'LM',   label: 'Left Middle',  home: 'D' },
  { code: 'LI',   label: 'Left Index',   home: 'F' },
  { code: 'TH-L', label: 'Left Thumb',   home: '⎵', baseFinger: 'TH' },
  { code: 'TH-R', label: 'Right Thumb',  home: '⎵', baseFinger: 'TH' },
  { code: 'RI',   label: 'Right Index',  home: 'J' },
  { code: 'RM',   label: 'Right Middle', home: 'K' },
  { code: 'RR',   label: 'Right Ring',   home: 'L' },
  { code: 'RP',   label: 'Right Pinky',  home: ';' }
];

function buildFingers() {
  const wrap = document.createElement('div');
  wrap.style.cssText = `
    display:flex; gap:8px; justify-content:center; flex-wrap:wrap;
    padding: 4px 6px 12px; border-bottom: 1px dashed rgba(255,255,255,0.08);
    margin-bottom: 10px;
  `;
  FINGER_INTRO.forEach(f => {
    const fingerKey = f.baseFinger || f.code;
    const meta = FINGERS[fingerKey];
    const pad = document.createElement('div');
    pad.className = 'tfg-finger';
    pad.dataset.finger = fingerKey;
    pad.dataset.fingerCode = f.code;
    pad.style.cssText = `
      display:flex; flex-direction:column; align-items:center; gap:4px;
      min-width: 52px; transition: transform 0.18s ease;
    `;
    pad.innerHTML = `
      <div class="tfg-pad" style="
        width:34px; height:34px; border-radius:50%;
        background: ${meta.color}; color:#0b0b0e;
        display:grid; place-items:center;
        font: 800 0.92rem 'SF Mono', Menlo, Consolas, monospace;
        box-shadow: 0 2px 10px ${meta.color}55;
        border: 2px solid rgba(255,255,255,0.12);
      ">${f.home}</div>
      <span style="
        font: 600 0.62rem -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        color:#d1d5db; text-align:center; line-height:1.15; max-width:60px;
      ">${f.label}</span>
    `;
    wrap.appendChild(pad);
  });
  return wrap;
}

let activeFingerFlash = null;
function flashFingerPad(fingerCode) {
  if (!widget) return;
  const pads = widget.querySelectorAll(`.tfg-finger[data-finger="${fingerCode}"]`);
  if (!pads.length) return;
  // Pick first matching pad (TH has 2 — thumbs — flash both)
  pads.forEach(pad => {
    pad.style.transform = 'translateY(-5px) scale(1.18)';
    pad.querySelector('.tfg-pad').style.boxShadow = `0 0 0 4px rgba(255,255,255,0.25), 0 6px 18px rgba(0,0,0,0.4)`;
  });
  if (activeFingerFlash) {
    activeFingerFlash.forEach(p => {
      p.style.transform = '';
      const inner = p.querySelector('.tfg-pad');
      if (inner) inner.style.boxShadow = '';
    });
  }
  activeFingerFlash = Array.from(pads);
  const myFlash = activeFingerFlash;
  setTimeout(() => {
    if (activeFingerFlash !== myFlash) return;
    myFlash.forEach(p => {
      p.style.transform = '';
      const inner = p.querySelector('.tfg-pad');
      if (inner) inner.style.boxShadow = `0 2px 10px ${getComputedStyle(inner).backgroundColor}55`;
    });
    activeFingerFlash = null;
  }, 450);
}

function buildLegend() {
  const legend = document.createElement('div');
  legend.style.cssText = `
    display:flex; flex-wrap:wrap; gap:8px 12px; justify-content:center;
    font: 600 0.72rem -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
    color: #d1d5db; padding: 8px 6px 0;
  `;
  Object.entries(FINGERS).forEach(([k, v]) => {
    const item = document.createElement('span');
    item.style.cssText = 'display:flex; align-items:center; gap:5px; white-space:nowrap;';
    item.innerHTML = `<span style="width:10px;height:10px;border-radius:2px;background:${v.color};display:inline-block;"></span>${v.name}`;
    legend.appendChild(item);
  });
  return legend;
}

function findKeyEl(rawKey) {
  if (!widget) return null;
  const key = rawKey.toLowerCase();
  // Direct match on primary key first
  let el = widget.querySelector(`.tfg-key[data-key="${CSS.escape(key)}"]`);
  if (el) return el;
  // Try matching shifted (e.g., user presses '!' which is shift+1)
  el = widget.querySelector(`.tfg-key[data-shift="${CSS.escape(key)}"]`);
  return el;
}

function flashKey(rawKey) {
  const el = findKeyEl(rawKey);
  if (!el) return null;
  if (activeFlash) {
    activeFlash.style.background = activeFlash._baseBg || activeFlash.style.background;
    activeFlash.style.transform = '';
  }
  const fingerCode = el.dataset.finger;
  const finger = FINGERS[fingerCode];
  el._baseBg = el.style.background;
  el.style.background = finger.color;
  el.style.transform = 'translateY(-2px) scale(1.06)';
  activeFlash = el;
  setTimeout(() => {
    if (activeFlash === el) {
      el.style.background = el._baseBg;
      el.style.transform = '';
      activeFlash = null;
    }
  }, 400);
  // Also light up the matching fingertip in the intro strip
  flashFingerPad(fingerCode);
  // Return both the finger metadata AND the canonical code so callers can
  // compare against AI-detected actual finger.
  return { ...finger, code: fingerCode };
}

function setMessage(html) {
  if (messageEl) messageEl.innerHTML = html;
}

function buildWidget() {
  const w = document.createElement('div');
  w.id = 'tfg-widget';
  w.style.cssText = `
    position: fixed; bottom: 14px; left: 14px; right: 220px;
    background: rgba(15, 15, 18, 0.93); color: #fff;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px; padding: 12px 14px 14px;
    z-index: 850; backdrop-filter: blur(12px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.45);
    max-width: 1080px; margin: 0 auto;
  `;

  const header = document.createElement('div');
  header.style.cssText = `
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    margin-bottom: 10px;
  `;
  const title = document.createElement('div');
  title.style.cssText = 'display:flex; align-items:center; gap:8px;';
  title.innerHTML = `
    <span style="display:inline-block; width:8px; height:8px; border-radius:50%;
      background:#22c55e; box-shadow:0 0 0 0 rgba(34,197,94,0.7);
      animation:tfgPulse 1.6s ease-out infinite;"></span>
    <strong style="font: 700 0.85rem -apple-system, BlinkMacSystemFont, system-ui, sans-serif; letter-spacing: 0.02em;">🎥 AI Camera — Finger Guide</strong>
    <span id="tfg-message" style="margin-left:6px; font: 600 0.78rem -apple-system, system-ui, sans-serif; color:#9ca3af;">Type any key — I'll show you the correct finger.</span>
  `;
  messageEl = title.querySelector('#tfg-message');

  const camBtn = document.createElement('button');
  camBtn.textContent = '🎥 Enable Real Camera';
  camBtn.title = 'Turn on your webcam — AI tracks your real fingers in real time';
  camBtn.style.cssText = `
    background: #ef4444; color: #fff; border: 0;
    border-radius: 999px; padding: 6px 14px; cursor: pointer;
    font: 700 0.78rem -apple-system, system-ui, sans-serif;
    letter-spacing: 0.02em; transition: background 0.15s ease;
  `;
  camBtn.onmouseover = () => camBtn.style.background = '#dc2626';
  camBtn.onmouseout  = () => camBtn.style.background = '#ef4444';
  camBtn.onclick = () => enableRealCamera(camBtn);

  const close = document.createElement('button');
  close.textContent = '✕';
  close.title = 'Hide finger guide';
  close.style.cssText = `
    background: transparent; color: #9ca3af; border: 1px solid #374151;
    border-radius: 6px; width: 26px; height: 26px; cursor: pointer;
    font-size: 0.85rem; line-height: 1;
  `;
  close.onclick = () => {
    if (cameraEnabled) disableRealCamera();
    w.remove();
    widget = null;
  };

  const headerRight = document.createElement('div');
  headerRight.style.cssText = 'display:flex; gap:8px; align-items:center;';
  headerRight.appendChild(camBtn);
  headerRight.appendChild(close);

  header.appendChild(title);
  header.appendChild(headerRight);
  w.appendChild(header);
  w.appendChild(buildCameraPanel());
  w.appendChild(buildScanLog());
  w.appendChild(buildFingers());
  w.appendChild(buildKeyboard());
  w.appendChild(buildLegend());

  // Keyframes
  if (!document.getElementById('tfg-style')) {
    const style = document.createElement('style');
    style.id = 'tfg-style';
    style.textContent = `
      @keyframes tfgPulse {
        0%   { box-shadow: 0 0 0 0 rgba(34,197,94,0.65); }
        70%  { box-shadow: 0 0 0 10px rgba(34,197,94,0); }
        100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
      }
      @keyframes tfgScannerSweep {
        0%   { top: 0%; opacity: 0.85; }
        45%  { opacity: 1; }
        50%  { top: calc(100% - 3px); opacity: 1; }
        55%  { opacity: 1; }
        100% { top: 0%; opacity: 0.85; }
      }
      @media (max-width: 800px) {
        #tfg-widget { right: 14px !important; bottom: 60px !important; padding: 10px !important; }
        #tfg-widget .tfg-key { min-width: 18px !important; padding: 4px 2px !important; font-size: 0.62rem !important; }
      }
    `;
    document.head.appendChild(style);
  }

  return w;
}

function onKey(e) {
  if (!widget) return;
  // Translate special keys to our key names
  let key = e.key;
  if (key === ' ') key = 'Space';
  const expected = flashKey(key);
  if (!expected) {
    setMessage(`Key <strong>${key}</strong> isn't on the typing map.`);
    return;
  }

  const keyDisplay = key === 'Space' ? '⎵ Space' : (key.length === 1 ? key.toUpperCase() : key);

  // If the real camera is on, compare AI-detected pressing finger vs expected.
  if (cameraEnabled) {
    const actual = detectPressingFinger();
    if (actual) {
      if (actual.fingerCode === expected.code) {
        setMessage(`✓ <strong style="color:#22c55e;">CORRECT!</strong> Pressed <strong>${keyDisplay}</strong> with your <strong style="color:${expected.color};">${expected.name}</strong>`);
      } else {
        const actualMeta = FINGERS[actual.fingerCode];
        showWrongFingerAlert(expected.name, actualMeta?.name || actual.fingerCode);
        // Also flash the actual-finger pad red so the user sees which finger AI thought pressed
        flashFingerPad(actual.fingerCode);
      }
      return;
    }
    // AI couldn't tell with confidence
    setMessage(`Pressed <strong>${keyDisplay}</strong> — use <strong style="color:${expected.color};">${expected.name}</strong> (AI couldn't tell which finger you used — show hands more clearly)`);
    return;
  }

  // Camera off — keyboard guide only.
  setMessage(`Pressed <strong style="color:#fff;">${keyDisplay}</strong> — use your <strong style="color:${expected.color};">${expected.name}</strong> finger`);
}

function shouldActivate() {
  return /\/courses?\/typing-skills(\/|$)/.test(window.location.pathname);
}

// ────────────────────────────────────────────────────────────────────────────
// REAL camera + AI hand tracking (MediaPipe Hands).
// Loads only when the user clicks "Enable Real Camera". Stays inside the
// existing widget; never sends video off-device.
// ────────────────────────────────────────────────────────────────────────────

let cameraEnabled = false;
let videoEl = null;
let canvasEl = null;
let handsModel = null;
let mediaStream = null;
let rafId = null;

function loadScriptOnce(src) {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[data-tfg-src="${src}"]`)) return resolve();
    const s = document.createElement('script');
    s.src = src;
    s.async = true;
    s.dataset.tfgSrc = src;
    s.onload = resolve;
    s.onerror = () => reject(new Error('Failed to load ' + src));
    document.head.appendChild(s);
  });
}

async function loadMediaPipe() {
  if (window.Hands) return;
  // Order matters: drawing_utils must be loaded before hands so we can draw
  // landmarks once results come back.
  await loadScriptOnce('https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js');
  await loadScriptOnce('https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js');
}

function buildCameraPanel() {
  const panel = document.createElement('div');
  panel.id = 'tfg-camera-panel';
  panel.style.cssText = `
    position: relative; width: 320px; height: 240px;
    border-radius: 8px; overflow: hidden;
    background: #0a0a0a; border: 1px solid rgba(255,255,255,0.1);
    display: none; margin: 0 auto 6px;
  `;
  videoEl = document.createElement('video');
  videoEl.autoplay = true;
  videoEl.playsInline = true;
  videoEl.muted = true;
  videoEl.style.cssText = 'position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transform:scaleX(-1);';
  canvasEl = document.createElement('canvas');
  canvasEl.width = 320;
  canvasEl.height = 240;
  canvasEl.style.cssText = 'position:absolute; inset:0; width:100%; height:100%; transform:scaleX(-1);';

  // Live indicator
  const liveDot = document.createElement('div');
  liveDot.style.cssText = `
    position:absolute; top:8px; left:8px; z-index:2;
    background: rgba(15,15,18,0.85); color:#fff;
    padding: 3px 10px 3px 8px; border-radius: 999px;
    font: 700 0.7rem -apple-system, system-ui, sans-serif;
    display:flex; align-items:center; gap:6px;
  `;
  liveDot.innerHTML = `
    <span style="width:7px;height:7px;border-radius:50%;background:#ef4444;
      animation:tfgPulse 1.6s ease-out infinite;"></span>
    🎥 LIVE — AI watching
  `;

  // Scanner-line overlay (moves vertically, indicates the AI is actively scanning).
  const scanner = document.createElement('div');
  scanner.id = 'tfg-scanner-line';
  scanner.style.cssText = `
    position:absolute; left:0; right:0; height:3px; z-index:3;
    background: linear-gradient(90deg, transparent 0%, rgba(34,197,94,0.0) 0%, rgba(34,197,94,1) 50%, rgba(34,197,94,0.0) 100%);
    box-shadow: 0 0 14px rgba(34,197,94,0.85), 0 0 24px rgba(34,197,94,0.45);
    top: 0; will-change: top; pointer-events: none;
    animation: tfgScannerSweep 2.2s ease-in-out infinite;
  `;

  // Scanner badge — top-right corner, complements the LIVE badge.
  const scanBadge = document.createElement('div');
  scanBadge.id = 'tfg-scan-badge';
  scanBadge.style.cssText = `
    position:absolute; top:8px; right:8px; z-index:3;
    background: rgba(8,40,18,0.85); color:#86efac;
    padding: 3px 10px 3px 8px; border-radius: 999px;
    font: 700 0.7rem -apple-system, system-ui, sans-serif;
    display:flex; align-items:center; gap:6px;
    border: 1px solid rgba(34,197,94,0.35);
  `;
  scanBadge.innerHTML = `
    <span style="display:inline-block;width:7px;height:7px;border-radius:50%;background:#22c55e;
      animation:tfgPulse 1.6s ease-out infinite;"></span>
    🔍 FINGER SCANNER
  `;

  panel.appendChild(videoEl);
  panel.appendChild(canvasEl);
  panel.appendChild(scanner);
  panel.appendChild(liveDot);
  panel.appendChild(scanBadge);
  return panel;
}

// Detection-log panel beneath the camera. Shows a rolling log of which fingers
// the AI is currently scanning + verifying.
let scanLogEl = null;
function buildScanLog() {
  const wrap = document.createElement('div');
  wrap.id = 'tfg-scan-log-wrap';
  wrap.style.cssText = `
    max-width: 320px; margin: 0 auto 10px;
    background: #060709; border: 1px solid #1f2433;
    border-radius: 6px; padding: 6px 10px;
    font: 600 0.7rem 'SF Mono', Menlo, Consolas, monospace;
    color: #86efac; display: none;
  `;
  wrap.innerHTML = `
    <div style="color:#9ca3af; letter-spacing:0.06em; font-size:0.65rem; margin-bottom:2px;">
      ▸ FINGER SCANNER OUTPUT
    </div>
    <div id="tfg-scan-log" style="min-height:18px; line-height:1.3;">awaiting hands…</div>
  `;
  scanLogEl = wrap.querySelector('#tfg-scan-log');
  return wrap;
}

function updateScanLog(handsSnapshot) {
  if (!scanLogEl) return;
  if (!handsSnapshot.length) {
    scanLogEl.textContent = 'no hands in frame';
    scanLogEl.style.color = '#6b7280';
    return;
  }
  const lines = [];
  for (const hand of handsSnapshot) {
    const tipsByName = {
      thumb: hand.landmarks[4],
      index: hand.landmarks[8],
      middle: hand.landmarks[12],
      ring: hand.landmarks[16],
      pinky: hand.landmarks[20]
    };
    // Show which finger is most-extended (lowest Y in our coord space)
    let bestName = '—', bestY = -Infinity;
    for (const [name, lm] of Object.entries(tipsByName)) {
      if (lm && lm.y > bestY) { bestY = lm.y; bestName = name; }
    }
    lines.push(`✓ ${hand.handedness.toLowerCase()} hand — extended: <b style="color:#fbbf24;">${bestName}</b>`);
  }
  scanLogEl.innerHTML = lines.join('<br>');
  scanLogEl.style.color = '#86efac';
}

// Latest landmark snapshot — used by detectPressingFinger() at keypress time.
let lastHandsSnapshot = [];

function onHandResults(results) {
  if (!canvasEl) return;
  const ctx = canvasEl.getContext('2d');
  ctx.save();
  ctx.clearRect(0, 0, canvasEl.width, canvasEl.height);
  lastHandsSnapshot = [];
  if (results.multiHandLandmarks && results.multiHandLandmarks.length) {
    for (let i = 0; i < results.multiHandLandmarks.length; i++) {
      const landmarks = results.multiHandLandmarks[i];
      const handed = results.multiHandedness?.[i]?.label || 'Right';
      lastHandsSnapshot.push({ handedness: handed, landmarks });
      // Draw connections (palm + fingers)
      if (window.drawConnectors && window.HAND_CONNECTIONS) {
        window.drawConnectors(ctx, landmarks, window.HAND_CONNECTIONS, {
          color: handed === 'Left' ? '#22c55e' : '#06b6d4',
          lineWidth: 2
        });
      }
      // Draw the 21 landmark dots
      if (window.drawLandmarks) {
        window.drawLandmarks(ctx, landmarks, {
          color: '#fbbf24',
          fillColor: '#ef4444',
          lineWidth: 1,
          radius: 3
        });
      }
    }
    if (!lastWrongAlertActive) {
      setMessage(`🎥 AI tracking <strong style="color:#fff;">${results.multiHandLandmarks.length}</strong> hand(s) — type a key, AI compares the finger you used vs the correct one`);
    }
  } else {
    if (!lastWrongAlertActive) setMessage('🎥 Camera on — show your hands in front of the camera');
  }
  // Update the scanner output panel with the latest detected fingers
  updateScanLog(lastHandsSnapshot);
  ctx.restore();
}

// MediaPipe Hands landmark indices: 4 = thumb tip, 8 = index, 12 = middle, 16 = ring, 20 = pinky.
const FINGERTIPS = [
  { idx: 4,  suffix: 'TH' /* thumb */ },
  { idx: 8,  suffix: 'I'  /* index */ },
  { idx: 12, suffix: 'M'  /* middle */ },
  { idx: 16, suffix: 'R'  /* ring */ },
  { idx: 20, suffix: 'P'  /* pinky */ }
];

/**
 * Detect which fingertip is "pressing" right now — heuristic: the fingertip
 * with the LOWEST y on each hand (closest to keyboard from a top-down POV)
 * AND lower than all other fingertips on the same hand by a margin.
 *
 * Returns { fingerCode, handedness } or null if can't tell confidently.
 */
function detectPressingFinger() {
  if (!lastHandsSnapshot.length) return null;
  let best = null;
  for (const hand of lastHandsSnapshot) {
    let lowestY = -Infinity, lowestTip = null;
    let secondLowestY = -Infinity;
    for (const tip of FINGERTIPS) {
      const lm = hand.landmarks[tip.idx];
      if (!lm) continue;
      if (lm.y > lowestY) {
        secondLowestY = lowestY;
        lowestY = lm.y;
        lowestTip = tip;
      } else if (lm.y > secondLowestY) {
        secondLowestY = lm.y;
      }
    }
    if (!lowestTip) continue;
    // Need a clear margin between the most-extended finger and the next, otherwise
    // the AI isn't confident which finger is pressing.
    const margin = lowestY - secondLowestY;
    if (margin < 0.015) continue;
    if (!best || lowestY > best.lowestY) {
      const handPrefix = hand.handedness === 'Left' ? 'L' : 'R';
      const fingerCode = lowestTip.suffix === 'TH' ? 'TH' : (handPrefix + lowestTip.suffix);
      best = { fingerCode, handedness: hand.handedness, lowestY, margin };
    }
  }
  return best;
}

let lastWrongAlertActive = false;
function showWrongFingerAlert(expectedName, actualName) {
  lastWrongAlertActive = true;
  setMessage(`❌ <strong style="color:#ef4444;">WRONG FINGER!</strong> AI saw your <strong style="color:#ef4444;">${actualName}</strong> press the key — should have been your <strong style="color:#22c55e;">${expectedName}</strong>`);
  // Pulse the camera panel red so it's hard to miss
  const panel = document.getElementById('tfg-camera-panel');
  if (panel) {
    panel.style.boxShadow = '0 0 0 3px #ef4444';
    setTimeout(() => {
      if (panel) panel.style.boxShadow = '';
      lastWrongAlertActive = false;
    }, 1400);
  } else {
    setTimeout(() => { lastWrongAlertActive = false; }, 1400);
  }
}

async function enableRealCamera(button) {
  if (cameraEnabled) return;
  try {
    button.disabled = true;
    button.textContent = '⏳ Loading AI…';

    // Lazy-load MediaPipe Hands
    setMessage('Loading MediaPipe Hands AI model…');
    await loadMediaPipe();

    // Ask for camera permission
    setMessage('Requesting camera permission…');
    mediaStream = await navigator.mediaDevices.getUserMedia({
      video: { width: { ideal: 320 }, height: { ideal: 240 }, facingMode: 'user' },
      audio: false
    });

    // Show the panel + scan log
    const panel = document.getElementById('tfg-camera-panel');
    if (panel) panel.style.display = 'block';
    const logWrap = document.getElementById('tfg-scan-log-wrap');
    if (logWrap) logWrap.style.display = 'block';

    videoEl.srcObject = mediaStream;
    await videoEl.play();

    // Initialize Hands
    handsModel = new window.Hands({
      locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
    });
    handsModel.setOptions({
      maxNumHands: 2,
      modelComplexity: 1,
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5
    });
    handsModel.onResults(onHandResults);

    // Continuous frame processing
    const processFrame = async () => {
      if (!videoEl || videoEl.paused || videoEl.ended) return;
      try { await handsModel.send({ image: videoEl }); } catch (e) { /* defensive */ }
      rafId = requestAnimationFrame(processFrame);
    };
    rafId = requestAnimationFrame(processFrame);

    cameraEnabled = true;
    button.textContent = '🛑 Stop Camera';
    button.disabled = false;
    button.onclick = () => disableRealCamera(button);
    setMessage('🎥 Camera on — show your hands in front of the camera');
  } catch (err) {
    button.disabled = false;
    button.textContent = '🎥 Enable Real Camera';
    let msg = `Camera error: ${err.message}`;
    if (err.name === 'NotAllowedError') msg = '❌ Camera access denied. Allow camera access in your browser to enable AI hand tracking.';
    if (err.name === 'NotFoundError') msg = '❌ No camera found on this device.';
    if (err.name === 'NotReadableError') msg = '❌ Camera is in use by another app.';
    setMessage(msg);
  }
}

function disableRealCamera(button) {
  if (!cameraEnabled) return;
  if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
  if (mediaStream) { mediaStream.getTracks().forEach(t => t.stop()); mediaStream = null; }
  if (videoEl) { videoEl.srcObject = null; }
  if (handsModel) { try { handsModel.close(); } catch (e) {} handsModel = null; }
  const panel = document.getElementById('tfg-camera-panel');
  if (panel) panel.style.display = 'none';
  const logWrap = document.getElementById('tfg-scan-log-wrap');
  if (logWrap) logWrap.style.display = 'none';
  if (canvasEl) canvasEl.getContext('2d').clearRect(0, 0, canvasEl.width, canvasEl.height);
  cameraEnabled = false;
  if (button) {
    button.textContent = '🎥 Enable Real Camera';
    button.onclick = () => enableRealCamera(button);
  }
  setMessage('Camera stopped. Type any key to see the keyboard guide.');
}

/**
 * Boot the AI Camera Finger Guide. Idempotent. Only activates on Typing Skills
 * pages so it doesn't crowd the rest of the site.
 */
export function initTypingFingerGuide() {
  if (window.__tfgInstalled) return;
  if (!shouldActivate()) return;
  window.__tfgInstalled = true;

  const install = () => {
    widget = buildWidget();
    document.body.appendChild(widget);
    document.addEventListener('keydown', onKey, true);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', install, { once: true });
  } else {
    install();
  }
}
