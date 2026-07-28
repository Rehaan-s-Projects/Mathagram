/**
 * Auth Gate — Requires sign-in to access a page.
 * Shows a sign-in overlay if user is not logged in.
 * Include this script on any page that requires authentication.
 *
 * Usage: <script type="module" src="../../js/auth-gate.js" data-base="../../"></script>
 * The data-base attribute sets the path to root (for login link).
 */

const script = document.currentScript || document.querySelector('script[src*="auth-gate"]');
const basePath = script?.getAttribute('data-base') || '';

// ─── Google Translate proxy detection ─────────────────────────────────
// When users open a page through translate.goog, the browser treats it as
// a *different origin* than mathagram.org. Firebase Auth, localStorage, and
// XP can't be read across origins — so the user normally looks logged-out
// on the translated copy. Workaround: when the user clicks Translate on
// mathagram.org, nav.js stamps their name/XP/color into the URL hash
// (#_mga_u=<base64(JSON)>). Here we read it back and display it in the
// nav so the translated page shows the SAME Mathagram identity.
if (/\.translate\.goog$/i.test(window.location.hostname)) {
  // Stamp from the URL hash (preserved across cross-origin redirects).
  // Also stash in sessionStorage so it survives intra-translate.goog
  // navigation (e.g., clicking a course tile drops the hash).
  let userInfo = null;
  let customToken = null;
  try {
    const hash = location.hash || '';
    const mU = hash.match(/_mga_u=([^&]+)/);
    const mT = hash.match(/_mga_t=([^&]+)/);
    if (mU) {
      userInfo = JSON.parse(decodeURIComponent(escape(atob(mU[1]))));
      sessionStorage.setItem('mga_translate_user', JSON.stringify(userInfo));
    } else {
      const cached = sessionStorage.getItem('mga_translate_user');
      if (cached) userInfo = JSON.parse(cached);
    }
    if (mT) {
      customToken = decodeURIComponent(mT[1]);
    }
    // Tidy the URL — remove the hash so it's not in subsequent links
    if (mU || mT) {
      try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
    }
  } catch (e) { userInfo = null; }

  // If we got a Firebase custom token, sign in for real with it. After this
  // succeeds, the page has the SAME account state on translate.goog as on
  // mathagram.org — same UID, same Firestore data, same XP, writes work.
  // (Requires `mathagram-org.translate.goog` to be in Firebase Auth's
  // authorized-domain list — set in Firebase Console.)
  if (customToken) {
    (async () => {
      try {
        const { auth } = await import('./firebase-config.js');
        const { signInWithCustomToken } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js');
        await signInWithCustomToken(auth, customToken);
        // Mark the session so we know SSO is active (vs. read-only display).
        try { sessionStorage.setItem('mga_translate_sso', '1'); } catch (e) {}
      } catch (e) {
        console.warn('Cross-origin sign-in failed; falling back to read-only display:', e);
      }
    })();
  }

  function applyTranslateUserChrome() {
    // 1. Replace the "Login" link with the user's name + XP badge
    const loginLink = document.querySelector('.nav-links a[data-auth="login"]');
    if (userInfo && loginLink) {
      const colorMap = { blue:'#3b82f6', green:'#22c55e', orange:'#f97316', purple:'#8b5cf6', cyan:'#06b6d4', pink:'#ec4899', gray:'#94a3b8' };
      const c = colorMap[userInfo.color] || colorMap.blue;
      const userBadge = document.createElement('a');
      userBadge.href = 'https://mathagram.org/profile.html';
      userBadge.target = '_top';
      userBadge.rel = 'noopener';
      userBadge.style.cssText = 'display:inline-flex;align-items:center;gap:8px;padding:4px 12px 4px 4px;background:rgba(255,255,255,0.95);border:1.5px solid '+c+';border-radius:999px;color:#1f1108;text-decoration:none;font-weight:700;font-size:0.85rem;';
      userBadge.innerHTML = `
        <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:${c};color:#fff;font-size:0.78rem;font-weight:800;">${(userInfo.name||'?').slice(0,1).toUpperCase()}</span>
        <span style="line-height:1.1;">
          <span style="display:block;">${userInfo.name||'Learner'}</span>
          <span style="display:block;font-size:0.68rem;color:${c};">⚡ ${(userInfo.xp||0).toLocaleString()} XP</span>
        </span>
      `;
      loginLink.replaceWith(userBadge);
    }
    // 2. Banner explaining the situation
    const banner = document.createElement('div');
    banner.id = 'translate-account-banner';
    banner.innerHTML = `
      <style>
        #translate-account-banner {
          position: fixed; bottom: 0; left: 0; right: 0; z-index: 9998;
          padding: 8px 16px;
          background: linear-gradient(90deg, #1FA45C, #FFD93D, #FF6B6B);
          color: #1f1108;
          font-family: inherit; font-size: 0.82rem; line-height: 1.35;
          text-align: center; font-weight: 700;
          box-shadow: 0 -2px 6px rgba(0,0,0,0.15);
        }
        #translate-account-banner a { color: #1e3a8a; text-decoration: underline; font-weight: 800; }
        #translate-account-banner button {
          background: rgba(0,0,0,0.12); color: #1f1108; border: none;
          padding: 3px 10px; border-radius: 999px; font-weight: 800;
          cursor: pointer; font-size: 0.74rem; margin-left: 10px;
        }
      </style>
      <span>${userInfo
        ? `🌐 Translated view of Mathagram — signed in as <strong>${userInfo.name||'Learner'}</strong>. Progress saving requires the original site: <a href="https://mathagram.org" target="_top" rel="noopener">mathagram.org</a>.`
        : `🌐 You're viewing the translated version of Mathagram. Your account &amp; XP live on <a href="https://mathagram.org" target="_top" rel="noopener">mathagram.org</a>.`}</span>
      <button type="button" onclick="document.getElementById('translate-account-banner').remove()">Dismiss</button>
    `;
    document.body.appendChild(banner);
  }

  if (document.body) applyTranslateUserChrome();
  else document.addEventListener('DOMContentLoaded', applyTranslateUserChrome);
  // Skip overlay + Firebase init below — no same-origin storage available.
}
const ON_TRANSLATE_GOOG = /\.translate\.goog$/i.test(window.location.hostname);

// Create overlay immediately (before page renders)
const overlay = document.createElement('div');
overlay.id = 'auth-gate-overlay';
overlay.innerHTML = `
  <style>
    #auth-gate-overlay {
      position: fixed; inset: 0; z-index: 9999;
      background: var(--color-bg, #f8f9fa);
      display: flex; align-items: center; justify-content: center;
      padding: 24px;
    }
    #auth-gate-overlay.hidden { display: none; }
    .auth-gate-card {
      background: var(--color-white, #fff);
      border: 1px solid var(--color-border, #e2e8f0);
      border-radius: 16px;
      max-width: 420px; width: 100%;
      padding: 48px 32px; text-align: center;
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08);
    }
    .auth-gate-card .gate-icon { font-size: 3rem; margin-bottom: 16px; }
    .auth-gate-card h2 { font-size: 1.5rem; font-weight: 800; margin-bottom: 8px; }
    .auth-gate-card p { font-size: 0.95rem; color: #64748b; line-height: 1.6; margin-bottom: 24px; }
    .auth-gate-card .gate-btn {
      display: inline-block; padding: 12px 32px;
      font-size: 1rem; font-weight: 700;
      background: #00e5c8; color: #fff;
      border-radius: 12px; text-decoration: none;
      transition: all 0.2s;
    }
    .auth-gate-card .gate-btn:hover { background: #00b89f; transform: translateY(-1px); }
    .auth-gate-card .gate-link {
      display: block; margin-top: 14px;
      font-size: 0.85rem; color: #64748b;
    }
    .auth-gate-card .gate-link a { color: #00b89f; text-decoration: underline; }
  </style>
  <div class="auth-gate-card">
    <div class="gate-icon">&#128274;</div>
    <h2>Sign in to continue</h2>
    <p>Create a free account or log in to access lessons, track your progress, and join the community.</p>
    <a href="${basePath}login.html" class="gate-btn">Sign In or Sign Up</a>
    <p class="gate-link">or <a href="${basePath}index.html">go back to home</a></p>
  </div>
`;
if (!ON_TRANSLATE_GOOG) {
  document.body.appendChild(overlay);
}

// Check auth state and ban status — skip entirely on Google Translate proxy
// (different origin → no Firebase Auth state available here)
if (!ON_TRANSLATE_GOOG) import('./firebase-config.js').then(({ auth, db }) => {
  Promise.all([
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js'),
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js')
  ]).then(([authMod, fireMod]) => {
    authMod.onAuthStateChanged(auth, async (user) => {
      if (user) {
        let userDoc = null;
        // Check if user is banned or suspended
        try {
          userDoc = await fireMod.getDoc(fireMod.doc(db, 'users', user.uid));
          if (userDoc.exists()) {
            const data = userDoc.data();
            const reason = data.banReason || 'Violation of Community Safety Rules';
            // Strike 3 — permanent ban
            if (data.banned) {
              window.location.href = basePath + 'violation.html?strike=3&reason=' + encodeURIComponent(reason);
              return;
            }
            // Strike 2 — suspended for 1 week
            if (data.suspended && data.suspendedUntil) {
              const until = new Date(data.suspendedUntil.seconds ? data.suspendedUntil.seconds * 1000 : data.suspendedUntil);
              if (until > new Date()) {
                window.location.href = basePath + 'violation.html?strike=2&reason=' + encodeURIComponent(reason) + '&until=' + encodeURIComponent(until.toISOString());
                return;
              }
            }
            // Strike 1 — check if user needs to see warning (unseenWarning flag)
            if (data.strikes >= 1 && data.unseenWarning) {
              window.location.href = basePath + 'violation.html?strike=1&reason=' + encodeURIComponent(reason);
              // Clear the unseen flag
              try { await fireMod.updateDoc(fireMod.doc(db, 'users', user.uid), { unseenWarning: false }); } catch(e) {}
              return;
            }
          }
        } catch(e) {}
        // ─── Require linked Google account + confirmed birthday ───────
        try {
          const data2 = (userDoc && userDoc.exists()) ? userDoc.data() : null;
          const hasGoogle = (user.providerData || []).some(p => p.providerId === 'google.com');
          const hasBirthday = !!(data2 && data2.birthday);
          if (!hasGoogle || !hasBirthday) {
            if (!/link-google\.html$/.test(location.pathname)) {
              window.location.href = basePath + 'link-google.html';
              return;
            }
          }
        } catch (e) { /* never lock the user out on a gate error */ }
        overlay.classList.add('hidden');
      } else {
        overlay.classList.remove('hidden');
      }
    });
  });
}).catch(() => {
  overlay.classList.remove('hidden');
});
