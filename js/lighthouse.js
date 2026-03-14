/**
 * Lighthouse — Loading animation & profile glow controller
 * @module lighthouse
 */

const STORAGE_KEY = 'mathagram-loaded';

/**
 * Initialise the loading-screen animation.
 *
 * - If the user has already seen the loader this session, the overlay is
 *   removed immediately.
 * - Otherwise the loader stays visible for 2 s, fades out, then is removed
 *   from the DOM once the transition ends.
 */
export function initLoadingAnimation() {
  const loader = document.querySelector('.lighthouse-loading');
  if (!loader) return;

  if (sessionStorage.getItem(STORAGE_KEY)) {
    loader.remove();
    return;
  }

  setTimeout(() => {
    loader.classList.add('fade-out');

    // Remove after fade-out completes (fallback timeout in case transitionend doesn't fire)
    let removed = false;
    const cleanup = () => {
      if (removed) return;
      removed = true;
      loader.remove();
      sessionStorage.setItem(STORAGE_KEY, '1');
    };
    loader.addEventListener('transitionend', cleanup, { once: true });
    setTimeout(cleanup, 700);
  }, 2000);
}

/**
 * Set the glow intensity on the profile lighthouse.
 *
 * @param {number} level — integer 1-8
 */
export function setLighthouseLevel(level) {
  const el = document.querySelector('.lighthouse-profile');
  if (!el) return;

  const clamped = Math.max(1, Math.min(8, Math.round(level)));
  el.setAttribute('data-level', String(clamped));
}
