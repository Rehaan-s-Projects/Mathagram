// js/nav.js
// Shared navigation auth state handler.
// Updates nav to show user avatar + profile link when logged in,
// or Login/Sign Up buttons when logged out.

import { onAuthChange, getUserProfile } from './auth.js';
import { CHARACTERS } from './characters.js';

/**
 * Initialize nav auth state. Call this on every page.
 * Looks for .nav-links container and replaces Login/Sign Up
 * with avatar + profile link when user is authenticated.
 *
 * @param {string} basePath - relative path to root (e.g., '' for root pages, '../../' for course lessons)
 */
export function initNav(basePath = '') {
  onAuthChange(async (user) => {
    const navLinks = document.querySelector('.nav-links');
    if (!navLinks) return;

    // Find and remove existing auth links
    const loginLink = navLinks.querySelector('[data-auth="login"]');
    const signupLink = navLinks.querySelector('[data-auth="signup"]');
    const userNav = navLinks.querySelector('[data-auth="user"]');

    if (user) {
      // Hide login/signup
      if (loginLink) loginLink.style.display = 'none';
      if (signupLink) signupLink.style.display = 'none';

      // Don't duplicate if already added
      if (userNav) {
        userNav.style.display = 'flex';
        return;
      }

      // Get user profile for character
      let charFile = 'edam.svg';
      let displayName = 'Profile';
      try {
        const profile = await getUserProfile();
        if (profile) {
          const charData = CHARACTERS[profile.character];
          if (charData) charFile = charData.file;
          displayName = profile.displayName || 'Profile';
        }
      } catch (e) {
        // Use defaults if profile fetch fails
      }

      // Create user nav element
      const userEl = document.createElement('div');
      userEl.setAttribute('data-auth', 'user');
      userEl.style.cssText = 'display:flex; align-items:center; gap:8px;';
      userEl.innerHTML = `
        <a href="${basePath}profile.html" style="display:flex; align-items:center; gap:8px; text-decoration:none; color:inherit; padding:4px 12px; border-radius:8px; transition:background 0.2s;">
          <img src="${basePath}assets/characters/${charFile}" alt="${displayName}" style="width:28px; height:28px; border-radius:50%; border:2px solid var(--color-primary);">
          <span style="font-size:0.85rem; font-weight:600;">${escapeHtml(displayName)}</span>
        </a>
      `;
      navLinks.appendChild(userEl);
    } else {
      // Show login/signup
      if (loginLink) loginLink.style.display = '';
      if (signupLink) signupLink.style.display = '';
      if (userNav) userNav.style.display = 'none';
    }
  });
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
