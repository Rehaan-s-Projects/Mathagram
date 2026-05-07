// js/nav.js
// Shared navigation auth state handler.
// Updates nav to show user color circle + profile link when logged in,
// or Login/Sign Up buttons when logged out.

import { onAuthChange, getUserProfile } from './auth.js';
import { startAutoUpdate } from './auto-update.js';
import { initProfanityWarning } from './profanity-warning.js';

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
  // Run auto-update + cache-clear on every page
  startAutoUpdate();

  // Add Translate widget (English / 🐍 Python toggle)
  addTranslateWidget();

  // Restore Python mode across navigations
  if (typeof localStorage !== 'undefined' && localStorage.getItem('mathagram-mode') === 'py') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoActivatePython);
    } else {
      autoActivatePython();
    }
  }

  // Soft profanity warning — toast on common cuss words; no strike, no redirect.
  // Idempotent: safe to call repeatedly across pages.
  initProfanityWarning();

  onAuthChange(async (user) => {
    const navLinks = document.querySelector('.nav-links');
    if (!navLinks) return;

    // Find and remove existing auth links
    const loginLink = navLinks.querySelector('[data-auth="login"]');
    const signupLink = navLinks.querySelector('[data-auth="signup"]');
    const userNav = navLinks.querySelector('[data-auth="user"]');

    if (user) {
      // Check if user is banned or suspended
      try {
        const { db } = await import('./firebase-config.js');
        const { doc, getDoc, updateDoc } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
        const userDoc = await getDoc(doc(db, 'users', user.uid));
        if (userDoc.exists()) {
          const data = userDoc.data();
          const reason = data.banReason || 'Violation of Community Safety Rules';
          if (data.banned) {
            window.location.href = basePath + 'violation.html?strike=3&reason=' + encodeURIComponent(reason);
            return;
          }
          if (data.suspended && data.suspendedUntil) {
            const until = new Date(data.suspendedUntil.seconds ? data.suspendedUntil.seconds * 1000 : data.suspendedUntil);
            if (until > new Date()) {
              window.location.href = basePath + 'violation.html?strike=2&reason=' + encodeURIComponent(reason) + '&until=' + encodeURIComponent(until.toISOString());
              return;
            }
          }
          if (data.strikes >= 1 && data.unseenWarning) {
            try { await updateDoc(doc(db, 'users', user.uid), { unseenWarning: false }); } catch(e) {}
            window.location.href = basePath + 'violation.html?strike=1&reason=' + encodeURIComponent(reason);
            return;
          }
        }
      } catch(e) {}

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
          <img src="${basePath}assets/avatars/${userColor}.svg" alt="" style="width:28px; height:28px; border-radius:50%;">
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

function addTranslateWidget() {
  if (document.getElementById('translate-btn')) return;
  const navLinks = document.querySelector('.nav-links');
  if (!navLinks) return;

  // Translate button
  const btn = document.createElement('button');
  btn.id = 'translate-btn';
  btn.title = 'Translate';
  btn.setAttribute('aria-label', 'Translate page');
  btn.style.cssText = 'background:none; border:none; cursor:pointer; padding:4px 8px; font-size:1.2rem; color:var(--color-text-secondary); transition:color 0.2s; display:flex; align-items:center; gap:4px;';
  btn.innerHTML = '<span style="font-size:1.1rem;">&#127760;</span><span style="font-size:0.75rem; font-weight:600;">Translate</span>';

  // Dropdown — data-no-py is set on the wrapper (below) so it covers both
  // the button's own label and the dropdown's contents.
  const dropdown = document.createElement('div');
  dropdown.id = 'translate-dropdown';
  dropdown.style.cssText = 'display:none; position:absolute; top:100%; right:0; background:var(--color-white); border:1px solid var(--color-border); border-radius:var(--radius); box-shadow:var(--shadow-lg); z-index:999; min-width:240px; flex-direction:column;';

  // Mascot header — Lingo & Babel, your translation guides.
  // The lingo/babel SVGs may not exist in the repo yet; onerror hides them
  // and the gradient + text still convey the brand.
  const mascotHeader = document.createElement('div');
  mascotHeader.style.cssText = 'display:flex; align-items:center; gap:10px; padding:12px 14px 10px; background:linear-gradient(135deg,#1FA45C 0%,#FFD93D 50%,#FF6B6B 100%); color:#fff; border-radius:var(--radius) var(--radius) 0 0;';
  mascotHeader.innerHTML = `
    <div style="display:flex; gap:-8px;">
      <img src="/assets/characters/lingo.svg" alt="Lingo the Parrot" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15);" onerror="this.style.display='none'">
      <img src="/assets/characters/babel.svg" alt="Babel the Owl" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15); margin-left:-10px;" onerror="this.style.display='none'">
    </div>
    <div style="flex:1; min-width:0;">
      <div style="font-weight:800; font-size:0.85rem; line-height:1.2;">Lingo &amp; Babel</div>
      <div style="font-size:0.7rem; opacity:0.95; line-height:1.2;">Your translation guides — English or Python!</div>
    </div>`;
  dropdown.appendChild(mascotHeader);

  // Mode list
  const list = document.createElement('div');
  list.style.cssText = 'padding:6px 0;';
  dropdown.appendChild(list);

  function makeEntry(label, mode) {
    const item = document.createElement('button');
    item.style.cssText = 'display:block; width:100%; text-align:left; padding:10px 16px; border:none; background:none; cursor:pointer; font-size:0.9rem; font-family:inherit; color:var(--color-text); transition:background 0.15s;';
    item.textContent = label;
    item.addEventListener('mouseenter', () => { item.style.background = 'var(--color-bg)'; });
    item.addEventListener('mouseleave', () => { item.style.background = 'none'; });
    item.addEventListener('click', () => {
      setMode(mode);
      dropdown.style.display = 'none';
    });
    return item;
  }
  list.appendChild(makeEntry('English', 'en'));
  list.appendChild(makeEntry('🐍 Python', 'py'));

  // Wrapper for positioning. data-no-py protects the button label AND the
  // dropdown's contents from the engine's text rewriter.
  const wrapper = document.createElement('div');
  wrapper.setAttribute('data-no-py', '');
  wrapper.style.cssText = 'position:relative; display:flex; align-items:center;';
  wrapper.appendChild(btn);
  wrapper.appendChild(dropdown);

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = dropdown.style.display === 'flex';
    dropdown.style.display = isOpen ? 'none' : 'flex';
  });
  document.addEventListener('click', () => { dropdown.style.display = 'none'; });

  navLinks.insertBefore(wrapper, navLinks.firstChild);
}

async function setMode(mode) {
  if (mode === 'py') {
    localStorage.setItem('mathagram-mode', 'py');
    try {
      const m = await import('./python-translate.js');
      m.activate();
    } catch (err) {
      console.warn('python-translate import failed:', err);
    }
  } else {
    localStorage.removeItem('mathagram-mode');
    try {
      const m = await import('./python-translate.js');
      m.deactivate();
    } catch (err) {
      console.warn('python-translate import failed:', err);
    }
  }
}

function autoActivatePython() {
  import('./python-translate.js').then(m => m.activate()).catch(err => {
    console.warn('python-translate import failed:', err);
  });
}
