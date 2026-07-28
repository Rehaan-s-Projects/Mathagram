// js/ai-keyboard-cam.js
// "AI Security Cameras" — global typing watcher for hate-slur moderation.
//
// Listens to every keystroke into any <input>, <textarea>, or contenteditable
// element on Mathagram. When a slur is typed, it routes the user to the
// existing strike system at /violation.html?strike=1.
//
// Slurs only appear in this file's regex (server-side moderation config); they
// are never rendered as visible content. The visible side-effect is a small
// "🎥 AI Camera Active" badge so users know typing is monitored, plus a brief
// flash overlay before the redirect on violation.

const VIOLATION_URL = '/violation.html?strike=1&reason='
  + encodeURIComponent('Hate speech — slur typed into a Mathagram input field (AI camera detection)');

// Slur regex. Word-boundary anchored so neutral words (Niagara, snigger,
// scunthorpe, etc.) don't false-positive. Case-insensitive.
//
// Add new patterns here only — never display the regex source in UI.
const SLUR_PATTERN = new RegExp(
  '(?:^|\\W)(?:' +
  // racial slurs (n-word and common phonetic variants)
  'n[i1!|][gq6]{2,}[ae3@4][hr]?' + '|' +
  // f-slur (homophobic) — strict word-boundary, exclude legitimate fag-as-bundle in old text
  'f[a@4]gg+[oe0]?[t7]?s?' + '|' +
  // ableist r-slur in clearly-pejorative form
  'r[e3]+t[a@4]rd' + '|' +
  // anti-Asian c-slur
  'c[h]+[i1]nks?' + '|' +
  // anti-Latino slur
  'sp[i1]cs?' +
  ')(?:\\W|$)',
  'i'
);

let triggered = false;

function fireViolation(matched) {
  if (triggered) return;
  triggered = true;

  // Visible flash overlay before redirect.
  const overlay = document.createElement('div');
  overlay.setAttribute('role', 'alertdialog');
  overlay.style.cssText = `
    position: fixed; inset: 0; background: rgba(10,0,0,0.92);
    color: #fca5a5; z-index: 99999;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
    padding: 32px; text-align: center; backdrop-filter: blur(8px);
  `;
  overlay.innerHTML = `
    <div style="font-size:4.5rem; line-height:1; margin-bottom:14px;">🎥</div>
    <h1 style="font-size:1.9rem; font-weight:900; color:#ef4444; margin:0 0 6px; letter-spacing:0.08em; text-transform:uppercase;">AI Camera Detected Slur</h1>
    <p style="font-size:1rem; color:#fecaca; max-width:520px; margin:8px 0;">A slur was typed into a Mathagram input. The incident has been logged and you're being routed to the moderation system.</p>
    <p style="font-size:0.85rem; color:#9ca3af; margin-top:18px; letter-spacing:0.04em;">Redirecting…</p>
  `;
  document.body.appendChild(overlay);

  // Strip the violating characters from the input that triggered it, so the
  // slur doesn't survive in the form's value if the redirect is interrupted.
  try {
    document.querySelectorAll('input, textarea').forEach(el => {
      if (el.value && SLUR_PATTERN.test(' ' + el.value + ' ')) el.value = '';
    });
    document.querySelectorAll('[contenteditable="true"], [contenteditable=""]').forEach(el => {
      if (el.textContent && SLUR_PATTERN.test(' ' + el.textContent + ' ')) el.textContent = '';
    });
  } catch (e) { /* defensive */ }

  // Short delay so the user actually reads the overlay.
  setTimeout(() => { window.location.href = VIOLATION_URL; }, 1100);
}

function checkValue(value) {
  if (!value || typeof value !== 'string' || value.length < 2) return;
  // Pad with whitespace so word-boundary regex catches start/end matches.
  if (SLUR_PATTERN.test(' ' + value + ' ')) fireViolation(value);
}

function attachListener() {
  // Single delegated listener on document captures every input event.
  document.addEventListener('input', (e) => {
    const t = e.target;
    if (!t) return;
    if (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA') {
      checkValue(t.value);
    } else if (t.isContentEditable) {
      checkValue(t.textContent || t.innerText);
    }
  }, true);

  // Also catch paste events directly (input fires too, but this is faster).
  document.addEventListener('paste', (e) => {
    try {
      const text = (e.clipboardData || window.clipboardData)?.getData('text');
      if (text) checkValue(text);
    } catch (err) { /* defensive */ }
  }, true);
}

function installCameraBadge() {
  if (document.getElementById('ai-camera-badge')) return;
  const badge = document.createElement('div');
  badge.id = 'ai-camera-badge';
  badge.setAttribute('aria-label', 'AI moderation camera is active');
  badge.title = 'AI cameras watch typing on Mathagram. Slurs trigger an automatic strike.';
  badge.style.cssText = `
    position: fixed; bottom: 14px; right: 14px; z-index: 800;
    background: rgba(20, 20, 20, 0.78); color: #fca5a5;
    padding: 6px 12px 6px 10px; border-radius: 999px;
    font: 600 0.78rem -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
    letter-spacing: 0.04em; backdrop-filter: blur(8px);
    border: 1px solid rgba(239,68,68,0.35);
    user-select: none; pointer-events: auto;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    display: flex; align-items: center; gap: 6px;
  `;
  // Pulsing red dot before the camera glyph for "live" feel.
  badge.innerHTML = `
    <span style="width:8px;height:8px;border-radius:50%;background:#ef4444;
      box-shadow:0 0 0 0 rgba(239,68,68,0.7); animation:aiCamPulse 1.6s ease-out infinite;"></span>
    <span>🎥 AI Camera Active</span>
  `;
  // Inject keyframes once.
  if (!document.getElementById('ai-camera-badge-style')) {
    const style = document.createElement('style');
    style.id = 'ai-camera-badge-style';
    style.textContent = `
      @keyframes aiCamPulse {
        0%   { box-shadow: 0 0 0 0 rgba(239,68,68,0.65); }
        70%  { box-shadow: 0 0 0 10px rgba(239,68,68,0); }
        100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
      }
    `;
    document.head.appendChild(style);
  }
  document.body.appendChild(badge);
}

/**
 * Boot the AI camera watcher. Idempotent — safe to call from every page.
 */
export function initAiKeyboardCam() {
  if (window.__aiKeyboardCamInstalled) return;
  window.__aiKeyboardCamInstalled = true;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      attachListener();
      installCameraBadge();
    }, { once: true });
  } else {
    attachListener();
    installCameraBadge();
  }
}
