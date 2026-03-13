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

    loader.addEventListener('transitionend', () => {
      loader.remove();
    }, { once: true });

    sessionStorage.setItem(STORAGE_KEY, '1');
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
