// js/nav.js
// Shared navigation auth state handler.
// Updates nav to show user color circle + profile link when logged in,
// or Login/Sign Up buttons when logged out.

import { onAuthChange, getUserProfile } from './auth.js';

function getColorValue(colorName) {
  const colors = {
    blue: '#3b82f6',
    green: '#22c55e',
    orange: '#f97316',
    purple: '#8b5cf6',
    cyan: '#06b6d4',
    pink: '#ec4899',
    gray: '#6b7280'
  };
  return colors[colorName] || colors.blue;
}

/**
 * Initialize nav auth state. Call this on every page.
 * Looks for .nav-links container and replaces Login/Sign Up
 * with color circle + profile link when user is authenticated.
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

      // Get user profile for color
      let displayName = 'Profile';
      let userColor = 'blue';
      try {
        const profile = await getUserProfile();
        if (profile) {
          userColor = profile.color || 'blue';
          displayName = profile.displayName || 'Profile';
        }
      } catch (e) {
        // Use defaults if profile fetch fails
      }

      // Create user nav element
      const initial = displayName.charAt(0).toUpperCase();
      const userEl = document.createElement('div');
      userEl.setAttribute('data-auth', 'user');
      userEl.style.cssText = 'display:flex; align-items:center; gap:8px;';
      userEl.innerHTML = `
        <a href="${basePath}profile.html" style="display:flex; align-items:center; gap:8px; text-decoration:none; color:inherit; padding:4px 12px; border-radius:8px; transition:background 0.2s;">
          <div style="width:28px; height:28px; border-radius:50%; background:${getColorValue(userColor)}; display:flex; align-items:center; justify-content:center; color:#fff; font-size:0.75rem; font-weight:700;">${initial}</div>
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
