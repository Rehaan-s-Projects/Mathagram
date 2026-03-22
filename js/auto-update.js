// js/auto-update.js
// Auto-update: checks for new version and refreshes the page silently.

const VERSION_CHECK_INTERVAL = 60 * 1000; // Check every 60 seconds
const VERSION_URL = '/version.json';

let currentVersion = null;

/**
 * Start auto-update checker.
 * Fetches version.json periodically. If version changes, reloads the page.
 */
export function startAutoUpdate() {
  // Get current version on load
  fetchVersion().then(v => {
    currentVersion = v;
  });

  // Check periodically
  setInterval(async () => {
    try {
      const newVersion = await fetchVersion();
      if (currentVersion && newVersion && newVersion !== currentVersion) {
        console.log('[Mathagram] New version detected:', newVersion);
        // Clear service worker cache
        if ('caches' in window) {
          const keys = await caches.keys();
          await Promise.all(keys.map(k => caches.delete(k)));
        }
        // Force reload from server
        window.location.reload(true);
      }
    } catch (e) {
      // Silently ignore network errors
    }
  }, VERSION_CHECK_INTERVAL);

  // Also check when tab becomes visible again
  document.addEventListener('visibilitychange', async () => {
    if (document.visibilityState === 'visible') {
      try {
        const newVersion = await fetchVersion();
        if (currentVersion && newVersion && newVersion !== currentVersion) {
          window.location.reload(true);
        }
      } catch (e) {}
    }
  });
}

async function fetchVersion() {
  const res = await fetch(VERSION_URL + '?t=' + Date.now(), { cache: 'no-store' });
  if (!res.ok) return null;
  const data = await res.json();
  return data.version || null;
}
