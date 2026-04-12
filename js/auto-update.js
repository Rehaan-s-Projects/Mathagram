// js/auto-update.js
// Auto-update + auto-clear-cache.
// - Clears browser caches and stale service workers on every page load.
// - Polls version.json periodically. If version changes, wipes caches and reloads.

const VERSION_CHECK_INTERVAL = 60 * 1000; // every 60s
const VERSION_URL = '/version.json';
const STORED_VERSION_KEY = 'mathagram_version';

let currentVersion = null;

async function clearAllCaches() {
  try {
    if ('caches' in window) {
      const keys = await caches.keys();
      await Promise.all(keys.map(k => caches.delete(k)));
    }
  } catch (e) {}
  try {
    if ('serviceWorker' in navigator) {
      const regs = await navigator.serviceWorker.getRegistrations();
      await Promise.all(regs.map(r => r.unregister()));
    }
  } catch (e) {}
}

async function fetchVersion() {
  const res = await fetch(VERSION_URL + '?t=' + Date.now(), { cache: 'no-store' });
  if (!res.ok) return null;
  const data = await res.json();
  return data.version || null;
}

/**
 * Start auto-update checker. Safe to call multiple times — only starts once.
 */
let started = false;
export function startAutoUpdate() {
  if (started) return;
  started = true;

  // 1. On page load: compare stored version vs server. If different, clear caches.
  (async () => {
    try {
      const stored = localStorage.getItem(STORED_VERSION_KEY);
      const serverVersion = await fetchVersion();
      if (serverVersion) {
        currentVersion = serverVersion;
        if (stored && stored !== serverVersion) {
          await clearAllCaches();
          localStorage.setItem(STORED_VERSION_KEY, serverVersion);
          // Reload once so the fresh assets load
          if (!sessionStorage.getItem('mathagram_reloaded_for_version_' + serverVersion)) {
            sessionStorage.setItem('mathagram_reloaded_for_version_' + serverVersion, '1');
            window.location.reload();
            return;
          }
        } else {
          localStorage.setItem(STORED_VERSION_KEY, serverVersion);
        }
      }
    } catch (e) {}
  })();

  // 2. Periodic poll while tab is open
  setInterval(async () => {
    try {
      const newVersion = await fetchVersion();
      if (currentVersion && newVersion && newVersion !== currentVersion) {
        await clearAllCaches();
        localStorage.setItem(STORED_VERSION_KEY, newVersion);
        window.location.reload();
      }
    } catch (e) {}
  }, VERSION_CHECK_INTERVAL);

  // 3. Check again when tab regains focus
  document.addEventListener('visibilitychange', async () => {
    if (document.visibilityState !== 'visible') return;
    try {
      const newVersion = await fetchVersion();
      if (currentVersion && newVersion && newVersion !== currentVersion) {
        await clearAllCaches();
        localStorage.setItem(STORED_VERSION_KEY, newVersion);
        window.location.reload();
      }
    } catch (e) {}
  });
}
