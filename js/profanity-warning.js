// js/profanity-warning.js
// Soft profanity watcher — separate from the slur "AI Security Camera"
// (js/ai-keyboard-cam.js).
//
// Slurs route the user to /violation.html?strike=1 (3-strike ban system).
// This file handles general English cuss words with a much softer treatment:
//   - shows a non-punitive toast: "Please don't use bad words on Mathagram."
//   - clears the offending input value
//   - 5-second cooldown so the toast doesn't spam while the user keeps typing
//   - does NOT issue a strike, does NOT redirect
//
// Word list intentionally excludes "damn" and "bastard" (per product call).

// Word-boundary anchored, case-insensitive. Allows light obfuscation
// (asterisks, $-for-s) but not aggressive leetspeak — false positives on a
// soft warning are worse here than missed matches.
const PROFANITY_PATTERN = new RegExp(
  '(?:^|\\W)(?:' +
  'f[u\\*][c]?k(?:ing|ed|er|s)?'        + '|' +
  'sh[i\\*]t(?:s|ting|ty|hole|head)?'   + '|' +
  'b[i\\*]tch(?:es|ing|y)?'             + '|' +
  'a[s\\$]{2}hole(?:s)?'                + '|' +
  'd[i\\*]ck(?:s|head|ish)?'            + '|' +
  'piss(?:ed|ing|er)?'                  + '|' +
  'c[o0]ck(?:s|y|sucker)?'              + '|' +
  'douche(?:bag|y|s)?'                  + '|' +
  'prick(?:s)?'                         + '|' +
  'motherf[u\\*][c]?ker(?:s|ing)?'      + '|' +
  'bullsh[i\\*]t(?:ter|ting)?'          + '|' +
  'wanker(?:s)?'                        + '|' +
  'arse(?:hole|s)?'                     + '|' +
  'twat(?:s)?'                          +
  ')(?:\\W|$)',
  'i'
);

const COOLDOWN_MS = 5000;
let lastWarnedAt = 0;

function showToast() {
  // Reuse one toast element so rapid re-fires don't stack.
  let toast = document.getElementById('profanity-warning-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'profanity-warning-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.style.cssText = `
      position: fixed; top: 18px; left: 50%; transform: translateX(-50%) translateY(-12px);
      z-index: 9000; max-width: 92vw; pointer-events: auto;
      background: #fef3c7; color: #78350f;
      border: 1.5px solid #f59e0b; border-radius: 12px;
      padding: 10px 16px; box-shadow: 0 10px 24px rgba(120, 53, 15, 0.18);
      font: 700 0.92rem -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
      letter-spacing: 0.01em; opacity: 0; transition: opacity 0.2s ease, transform 0.2s ease;
      display: flex; align-items: center; gap: 8px;
    `;
    toast.innerHTML = `
      <span aria-hidden="true" style="font-size:1.1rem;">⚠️</span>
      <span>Please don't use bad words on Mathagram.</span>
    `;
    document.body.appendChild(toast);
  }

  // Show
  requestAnimationFrame(() => {
    toast.style.opacity = '1';
    toast.style.transform = 'translateX(-50%) translateY(0)';
  });

  clearTimeout(toast._hideTimer);
  toast._hideTimer = setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(-50%) translateY(-12px)';
  }, 4000);
}

function fireWarning() {
  const now = Date.now();
  if (now - lastWarnedAt < COOLDOWN_MS) return;
  lastWarnedAt = now;

  showToast();

  // Clear the offending value from any input/textarea/contenteditable.
  try {
    document.querySelectorAll('input, textarea').forEach(el => {
      if (el.value && PROFANITY_PATTERN.test(' ' + el.value + ' ')) el.value = '';
    });
    document.querySelectorAll('[contenteditable="true"], [contenteditable=""]').forEach(el => {
      if (el.textContent && PROFANITY_PATTERN.test(' ' + el.textContent + ' ')) el.textContent = '';
    });
  } catch (e) { /* defensive */ }
}

function checkValue(value) {
  if (!value || typeof value !== 'string' || value.length < 3) return;
  if (PROFANITY_PATTERN.test(' ' + value + ' ')) fireWarning();
}

function attachListener() {
  document.addEventListener('input', (e) => {
    const t = e.target;
    if (!t) return;
    if (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA') {
      checkValue(t.value);
    } else if (t.isContentEditable) {
      checkValue(t.textContent || t.innerText);
    }
  }, true);

  document.addEventListener('paste', (e) => {
    try {
      const text = (e.clipboardData || window.clipboardData)?.getData('text');
      if (text) checkValue(text);
    } catch (err) { /* defensive */ }
  }, true);
}

/**
 * Boot the soft profanity warning. Idempotent — safe to call on every page.
 */
export function initProfanityWarning() {
  if (window.__profanityWarningInstalled) return;
  window.__profanityWarningInstalled = true;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachListener, { once: true });
  } else {
    attachListener();
  }
}
