/**
 * Lesson Loader — Shows a loading spinner while Firebase auth resolves.
 * - If logged in: auth-gate hides → loader fades out → lesson visible.
 * - If NOT logged in: auth-gate stays visible → loader fades out → sign-in card visible.
 * Either way, the loader removes itself once auth has resolved.
 */

const loader = document.createElement('div');
loader.id = 'lesson-loader';
loader.innerHTML = `
  <style>
    #lesson-loader {
      position: fixed; inset: 0; z-index: 10000;
      background: var(--color-bg, #f8f9fa);
      display: flex; align-items: center; justify-content: center;
      transition: opacity 0.25s ease;
    }
    #lesson-loader.done { opacity: 0; pointer-events: none; }
    #lesson-loader .loader-spinner {
      width: 48px; height: 48px;
      border: 4px solid rgba(0,0,0,0.08);
      border-top-color: #00e5c8;
      border-radius: 50%;
      animation: loader-spin 0.7s linear infinite;
      margin: 0 auto 16px;
    }
    @keyframes loader-spin { to { transform: rotate(360deg); } }
    #lesson-loader p {
      font-size: 1rem; font-weight: 600;
      color: var(--color-text-secondary, #64748b);
      text-align: center;
    }
    #lesson-loader .loader-inner { text-align: center; }
  </style>
  <div class="loader-inner">
    <div class="loader-spinner"></div>
    <p>Loading lesson\u2026</p>
  </div>
`;
document.body.appendChild(loader);

let resolved = false;

function removeLoader() {
  if (resolved) return;
  resolved = true;
  loader.classList.add('done');
  setTimeout(() => loader.remove(), 300);
}

// Watch auth-gate: once its class changes, auth has resolved.
// - .hidden added → user is logged in → remove loader, show lesson
// - .hidden NOT added → user is NOT logged in → remove loader, show sign-in card
const observer = new MutationObserver(() => {
  const gate = document.getElementById('auth-gate-overlay');
  if (!gate) { removeLoader(); observer.disconnect(); return; }
  // Auth resolved either way — gate class was modified by onAuthStateChanged
  removeLoader();
  observer.disconnect();
});

function waitForGate() {
  const gate = document.getElementById('auth-gate-overlay');
  if (gate) {
    // If already hidden (logged in, resolved fast), remove now
    if (gate.classList.contains('hidden')) {
      removeLoader();
      return;
    }
    // Watch for ANY class change on the gate (hidden added or removed)
    observer.observe(gate, { attributes: true, attributeFilter: ['class'] });
  } else {
    requestAnimationFrame(waitForGate);
  }
}
waitForGate();

// Fallback: if auth takes too long (>4s), remove loader anyway
setTimeout(removeLoader, 4000);
