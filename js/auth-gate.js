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
document.body.appendChild(overlay);

// Check auth state and ban status
import('./firebase-config.js').then(({ auth, db }) => {
  Promise.all([
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js'),
    import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js')
  ]).then(([authMod, fireMod]) => {
    authMod.onAuthStateChanged(auth, async (user) => {
      if (user) {
        // Check if user is banned or suspended
        try {
          const userDoc = await fireMod.getDoc(fireMod.doc(db, 'users', user.uid));
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
        overlay.classList.add('hidden');
      } else {
        overlay.classList.remove('hidden');
      }
    });
  });
}).catch(() => {
  overlay.classList.remove('hidden');
});
