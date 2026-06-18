// js/ui-sounds.js
// Mathagram website UI sound layer.
// Inspired by modern browser UI feedback (Microsoft Edge-style — brief,
// polite, low-frequency clicks and ascending success chimes) but all chimes
// are synthesized live via the Web Audio API, so no audio files are shipped.
//
// Public API:
//   initUiSounds()            — auto-binds delegated listeners + mounts the
//                               🔊 / 🔇 floating toggle. Idempotent.
//   playClick(), playSuccess(), playError(), playNotify(),
//   playOpen(),  playClose()  — manual triggers if needed.
//   setMuted(true|false), isMuted()
//
// Mute state persists in localStorage under 'mathagram-ui-sounds-muted'.
// Default: ON. Users can toggle with the floating button or by calling
// setMuted(true).

const STORAGE_KEY = 'mathagram-ui-sounds-muted';

let _ctx = null;
let _initted = false;
let _toggleBtn = null;

function _ensureCtx() {
  if (_ctx) {
    if (_ctx.state === 'suspended') _ctx.resume();
    return _ctx;
  }
  const Ctor = window.AudioContext || window.webkitAudioContext;
  if (!Ctor) return null;
  _ctx = new Ctor();
  return _ctx;
}

export function isMuted() {
  try { return localStorage.getItem(STORAGE_KEY) === '1'; } catch { return false; }
}

export function setMuted(muted) {
  try { localStorage.setItem(STORAGE_KEY, muted ? '1' : '0'); } catch {}
  _renderToggle();
}

// ─── Synthesized chimes ────────────────────────────────────────────────
//
// All chimes share the same envelope shape: very fast attack (1–10ms), short
// decay (40–200ms), exponential tail to silence. Volume is intentionally low
// (peak 0.10–0.16) so the sounds sit behind content rather than over it.

function _tone(opts) {
  if (isMuted()) return;
  const ctx = _ensureCtx();
  if (!ctx) return;
  const {
    freq = 720,
    type = 'triangle',
    duration = 0.08,
    peak = 0.12,
    attack = 0.005,
    detune = 0,
    sweepTo = null
  } = opts;
  const t0 = ctx.currentTime;
  const t1 = t0 + duration;
  const gain = ctx.createGain();
  gain.gain.setValueAtTime(0, t0);
  gain.gain.linearRampToValueAtTime(peak, t0 + attack);
  gain.gain.exponentialRampToValueAtTime(0.0001, t1);
  gain.connect(ctx.destination);
  const osc = ctx.createOscillator();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, t0);
  if (sweepTo != null) osc.frequency.exponentialRampToValueAtTime(sweepTo, t1);
  osc.detune.setValueAtTime(detune, t0);
  osc.connect(gain);
  osc.start(t0);
  osc.stop(t1 + 0.02);
}

// A single soft click — primary feedback for button presses.
export function playClick() {
  _tone({ freq: 720, type: 'triangle', duration: 0.045, peak: 0.10 });
  _tone({ freq: 1080, type: 'sine',    duration: 0.035, peak: 0.05, attack: 0.001 });
}

// Two-note ascending chime for confirmations / completions.
export function playSuccess() {
  if (isMuted()) return;
  _tone({ freq: 523.25, type: 'triangle', duration: 0.16, peak: 0.13 });   // C5
  const ctx = _ensureCtx();
  if (!ctx) return;
  const delayMs = 110;
  setTimeout(() => _tone({ freq: 783.99, type: 'triangle', duration: 0.22, peak: 0.13 }), delayMs); // G5
}

// Low, polite "nope" for invalid actions.
export function playError() {
  _tone({ freq: 280, type: 'square', duration: 0.10, peak: 0.10, sweepTo: 200 });
}

// Soft "ding" for notifications / new content.
export function playNotify() {
  _tone({ freq: 880, type: 'sine', duration: 0.25, peak: 0.12, attack: 0.008 });
}

// Brief upward sweep — modal/panel opens.
export function playOpen() {
  _tone({ freq: 440, type: 'sine', duration: 0.13, peak: 0.10, sweepTo: 880, attack: 0.004 });
}

// Brief downward sweep — modal/panel closes.
export function playClose() {
  _tone({ freq: 660, type: 'sine', duration: 0.13, peak: 0.10, sweepTo: 330, attack: 0.004 });
}

// ─── Delegated bindings ────────────────────────────────────────────────
//
// Click sound fires on any <button> / .btn / anchor with class .btn or
// .btn-primary / .btn-outline / .btn-alt. We intentionally do NOT bind on
// every click event — only ones that look like UI controls — so we don't
// double-trigger on rich interactive widgets (piano keys, drum pads,
// quiz options) that already produce their own audio feedback.

function _isUiControl(target) {
  if (!target || target.nodeType !== 1) return false;
  // Walk up at most 3 levels — controls are usually leaf-ish.
  let el = target;
  for (let i = 0; i < 4 && el; i++) {
    if (el.classList && (
      el.classList.contains('btn') ||
      el.classList.contains('nav-logo') ||
      el.classList.contains('filter-btn') ||
      el.classList.contains('alpha-btn')
    )) return true;
    // Skip top-level click sound on things that produce their own audio.
    if (el.classList && (
      el.classList.contains('white-key') ||
      el.classList.contains('black-key') ||
      el.classList.contains('answer') ||
      el.classList.contains('person')
    )) return false;
    el = el.parentElement;
  }
  return false;
}

function _onDocClick(e) {
  if (!_isUiControl(e.target)) return;
  playClick();
}

// ─── Floating mute toggle ──────────────────────────────────────────────

const TOGGLE_ID = 'mathagram-ui-sound-toggle';

function _renderToggle() {
  if (!_toggleBtn) return;
  const muted = isMuted();
  _toggleBtn.textContent = muted ? '🔇' : '🔊';
  _toggleBtn.setAttribute('aria-label', muted ? 'Enable UI sounds' : 'Mute UI sounds');
  _toggleBtn.title = muted ? 'UI sounds: off (click to enable)' : 'UI sounds: on (click to mute)';
  _toggleBtn.classList.toggle('muted', muted);
}

function _mountToggle() {
  if (document.getElementById(TOGGLE_ID)) {
    _toggleBtn = document.getElementById(TOGGLE_ID);
    _renderToggle();
    return;
  }
  const style = document.createElement('style');
  style.textContent = `
    #${TOGGLE_ID} {
      position: fixed; bottom: 18px; right: 18px;
      width: 42px; height: 42px; border-radius: 50%;
      border: 1px solid rgba(0, 0, 0, 0.08);
      background: rgba(255, 255, 255, 0.96);
      box-shadow: 0 6px 18px rgba(15, 23, 42, 0.12), 0 2px 4px rgba(15, 23, 42, 0.08);
      font-size: 20px; line-height: 1; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
      transition: transform 0.12s ease, box-shadow 0.18s ease, opacity 0.18s ease;
      opacity: 0.78;
      z-index: 9998;
      padding: 0;
    }
    #${TOGGLE_ID}:hover { opacity: 1; transform: translateY(-1px); box-shadow: 0 10px 24px rgba(15, 23, 42, 0.18); }
    #${TOGGLE_ID}:active { transform: translateY(0); }
    #${TOGGLE_ID}.muted { background: rgba(243, 244, 246, 0.96); filter: grayscale(0.4); }
    @media (max-width: 540px) {
      #${TOGGLE_ID} { bottom: 12px; right: 12px; width: 38px; height: 38px; font-size: 18px; }
    }
  `;
  document.head.appendChild(style);
  const btn = document.createElement('button');
  btn.id = TOGGLE_ID;
  btn.type = 'button';
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const next = !isMuted();
    setMuted(next);
    // Audible confirmation when un-muting.
    if (!next) playClick();
  });
  document.body.appendChild(btn);
  _toggleBtn = btn;
  _renderToggle();
}

// ─── Init ──────────────────────────────────────────────────────────────

export function initUiSounds() {
  if (_initted) return;
  _initted = true;
  // Lazy-init AudioContext on first user gesture (browser autoplay policy).
  const warmup = () => {
    _ensureCtx();
    window.removeEventListener('pointerdown', warmup);
    window.removeEventListener('keydown', warmup);
  };
  window.addEventListener('pointerdown', warmup, { once: true });
  window.addEventListener('keydown', warmup, { once: true });

  // Delegated click sound for UI controls.
  document.addEventListener('click', _onDocClick, { capture: true });

  // Floating mute button removed — click-sound mute now lives in the
  // General Settings card on the homepage (single, non-duplicated control).
}
