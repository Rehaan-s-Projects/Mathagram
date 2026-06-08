# Google-Required Account Flow — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every Mathagram account Gmail-only, Google-linked, and age-verified (13+), enforced site-wide for all users, plus a Google-only "Switch account" button on the profile.

**Architecture:** Pure static site on Firebase Auth + Firestore. Enforcement happens at one shared chokepoint (`js/auth-gate.js`, included on 1,204 pages). A new `link-google.html` collects the missing requirements (Google link + birthday). `login.html` enforces Gmail-only at signup. `profile.html` gains the switch-account control.

**Tech Stack:** Vanilla HTML/ES-module JS, Firebase Auth v10.12.0 (`linkWithPopup`, `signInWithPopup`, `GoogleAuthProvider`), Firestore.

**No automated test harness exists** (no `package.json`/test runner). Each task's verification is a concrete manual browser check against live Firebase. Treat the "Verify" steps as the equivalent of running a test: do them before committing.

**Concurrency note:** Another process committed to `login.html` and the Firebase CSP mid-design (commits `62e0c81`, `61914c7`). **Before editing `login.html`, re-Read it** — line numbers/handlers below reflect the version at design time and may have shifted. The logic to add is unchanged; locate the current signup-submit handler and `googleAuth()` function and apply the edits there.

---

## Helper used in multiple tasks

A single Gmail check, defined inline where needed (do not create a shared module — the existing code uses inline helpers):

```js
const isGmail = (email) => /@gmail\.com$/i.test((email || '').trim());
```

---

## Task 1: Gmail-only enforcement + post-signup redirect (`login.html`)

**Files:**
- Modify: `login.html` (inline `<script type="module">` — signup-submit handler and `googleAuth()`)

- [ ] **Step 1: Re-Read `login.html`** to get current line numbers (concurrency note above).

Run: open `login.html`, locate (a) the `signupForm.addEventListener('submit', ...)` handler and (b) the `async function googleAuth()`.

- [ ] **Step 2: Add the Gmail guard to the email signup handler**

In the signup-submit handler, immediately after the existing display-name validation (the `if (!/^[A-Za-z0-9]{3,13}$/.test(name)) { ... return; }` block) and before `signupBtn.disabled = true;`, insert:

```js
      if (!/@gmail\.com$/i.test(email)) {
        signupError.textContent = 'Mathagram requires a Gmail address (@gmail.com). Please sign up with your Gmail.';
        signupError.classList.add('show'); return;
      }
```

- [ ] **Step 3: Redirect new email signups to the setup step**

In the same handler's `try` block, change the post-signup redirect from the profile to the setup page. Replace:

```js
        window.location.assign('/profile.html');
```

(the one inside the `signupForm` submit handler, after `setDoc(...)`) with:

```js
        window.location.assign('/link-google.html');
```

- [ ] **Step 4: Enforce Gmail on the Google buttons**

In `async function googleAuth()`, after `const { user } = await signInWithPopup(auth, provider);` and before the Firestore profile block, insert:

```js
        if (!/@gmail\.com$/i.test(user.email || '')) {
          const { signOut } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js');
          await signOut(auth);
          signinError.textContent = 'Mathagram requires a Gmail address. Please choose a @gmail.com Google account.';
          signinError.classList.add('show');
          return;
        }
```

(Reuse `signinError` — it is the shared error element already referenced inside `googleAuth`.)

- [ ] **Step 5: Verify**

Serve the site locally (e.g. `python3 -m http.server 8000`) and open `http://localhost:8000/login.html`.
- Sign Up tab → enter a non-Gmail email (e.g. `a@yahoo.com`), valid name + password → submit. Expected: red error "Mathagram requires a Gmail address…", no account created.
- Repeat with a real `@gmail.com` you control → submit. Expected: account created and browser navigates to `/link-google.html` (will 404 until Task 2 — that is expected here).
- "Continue with Google" with a non-Gmail Google account (if available) → expected: signed out + Gmail error. (If no non-Gmail account handy, note this as covered by code review.)

- [ ] **Step 6: Commit**

```bash
git add login.html
git commit -m "Enforce Gmail-only signup and route new signups to setup step"
```

---

## Task 2: Required setup step (`link-google.html`)

**Files:**
- Create: `link-google.html`

This page mirrors `login.html`'s styling (`css/global.css`, `.auth-card`). It does **not** include `js/auth-gate.js`. It shows whichever requirements are missing (birthday and/or Google link) and only redirects to the profile when **both** a `google.com` provider and a stored `birthday` exist.

- [ ] **Step 1: Create `link-google.html` with full contents**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Finish Setup — Mathagram</title>
  <link rel="icon" href="assets/lighthouse/logo.svg">
  <link rel="stylesheet" href="css/global.css">
  <style>
    .auth-container { max-width: 480px; margin: 48px auto; padding: 0 24px; }
    .auth-card {
      background: var(--color-white); border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg); padding: 40px 32px;
    }
    .auth-card h1 { text-align:center; font-size:1.6rem; font-weight:800; margin-bottom:8px; color:var(--color-primary-dark); }
    .auth-card .sub { text-align:center; color:var(--color-text-secondary); font-size:0.92rem; margin-bottom:24px; }
    .setup-block { border:2px solid var(--color-border); border-radius:var(--radius); padding:18px; margin-bottom:18px; }
    .setup-block.done { border-color:#22c55e; background:#f0fdf4; }
    .setup-block h2 { font-size:1rem; font-weight:700; margin:0 0 10px; display:flex; align-items:center; gap:8px; }
    .setup-block label { display:block; font-size:0.85rem; font-weight:600; margin-bottom:6px; }
    .setup-block input[type=date] {
      width:100%; padding:10px 14px; font:0.95rem var(--font-sans);
      border:2px solid var(--color-border); border-radius:var(--radius);
      background:var(--color-bg); box-sizing:border-box;
    }
    .google-btn {
      width:100%; padding:10px 14px; display:flex; align-items:center; justify-content:center; gap:10px;
      background:var(--color-white); color:var(--color-text);
      border:2px solid var(--color-border); border-radius:var(--radius);
      font:600 0.95rem var(--font-sans); cursor:pointer;
    }
    .google-btn:hover { background:var(--color-bg); border-color:var(--color-primary); }
    .google-btn svg { width:18px; height:18px; }
    .error-msg { display:none; color:#ef4444; font-size:0.85rem; margin-top:10px; text-align:center; line-height:1.45; }
    .error-msg.show { display:block; }
    .ok-tag { font-size:0.78rem; color:#166534; font-weight:700; }
    #finish-btn { width:100%; padding:12px; font-size:1rem; margin-top:8px; }
    #finish-btn[disabled] { opacity:0.55; cursor:not-allowed; }
  </style>
</head>
<body>
  <nav class="nav">
    <div class="container">
      <a href="/" class="nav-logo">
        <img src="assets/lighthouse/logo.svg" alt="" width="32" height="32">
        <span>Mathagram</span>
      </a>
    </div>
  </nav>

  <div class="auth-container">
    <div class="auth-card">
      <h1>Finish setting up your account</h1>
      <p class="sub">Mathagram requires a linked Google account and your birthday before you continue.</p>

      <!-- Birthday -->
      <div class="setup-block" id="dob-block">
        <h2>1. Confirm your birthday</h2>
        <label for="dob">Date of birth</label>
        <input type="date" id="dob">
        <p class="error-msg" id="dob-error"></p>
        <p class="ok-tag" id="dob-ok" style="display:none;">✓ Birthday confirmed</p>
      </div>

      <!-- Google link -->
      <div class="setup-block" id="google-block">
        <h2>2. Link your Google account</h2>
        <button type="button" class="google-btn" id="link-google-btn">
          <svg viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
          Link Google account
        </button>
        <p class="error-msg" id="google-error"></p>
        <p class="ok-tag" id="google-ok" style="display:none;">✓ Google linked</p>
      </div>

      <button type="button" class="btn btn-primary" id="finish-btn" disabled>Continue to Mathagram</button>
      <p class="error-msg" id="finish-error"></p>
    </div>
  </div>

  <script type="module">
    import { initNav } from './js/nav.js';
    initNav('');
    import {
      onAuthStateChanged, linkWithPopup, GoogleAuthProvider, signOut
    } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
    import { doc, getDoc, updateDoc } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';
    import { auth, db } from './js/firebase-config.js';

    const isGmail = (e) => /@gmail\.com$/i.test((e || '').trim());

    const dobInput   = document.getElementById('dob');
    const dobError   = document.getElementById('dob-error');
    const dobOk      = document.getElementById('dob-ok');
    const dobBlock   = document.getElementById('dob-block');
    const googleBtn  = document.getElementById('link-google-btn');
    const googleErr  = document.getElementById('google-error');
    const googleOk   = document.getElementById('google-ok');
    const googleBlk  = document.getElementById('google-block');
    const finishBtn  = document.getElementById('finish-btn');
    const finishErr  = document.getElementById('finish-error');

    let currentUser = null;
    let dobValid = false;       // 13+ entered this session
    let dobValue = '';          // "YYYY-MM-DD"

    function showErr(el, msg) { el.textContent = msg; el.classList.add('show'); }
    function clearErr(el) { el.textContent = ''; el.classList.remove('show'); }

    function ageFrom(isoDate) {
      // isoDate "YYYY-MM-DD"; compute whole years as of today.
      const [y, m, d] = isoDate.split('-').map(Number);
      const today = new Date();
      let age = today.getFullYear() - y;
      const beforeBirthday =
        (today.getMonth() + 1) < m ||
        ((today.getMonth() + 1) === m && today.getDate() < d);
      if (beforeBirthday) age -= 1;
      return age;
    }

    function hasGoogle() {
      return (currentUser?.providerData || []).some(p => p.providerId === 'google.com');
    }

    function refreshUI() {
      // Birthday block
      if (dobValid) { dobBlock.classList.add('done'); dobOk.style.display = 'block'; }
      else { dobBlock.classList.remove('done'); dobOk.style.display = 'none'; }
      // Google block
      if (hasGoogle()) {
        googleBlk.classList.add('done'); googleOk.style.display = 'block';
        googleBtn.disabled = true; googleBtn.style.display = 'none';
      }
      // Finish button
      finishBtn.disabled = !(dobValid && hasGoogle());
    }

    // ─── DOB validation ───────────────────────────────────────────────
    dobInput.addEventListener('change', () => {
      clearErr(dobError);
      const v = dobInput.value;
      if (!v) { dobValid = false; refreshUI(); return; }
      const age = ageFrom(v);
      if (age < 13) {
        dobValid = false; dobValue = '';
        showErr(dobError, 'You must be at least 13 years old to use Mathagram.');
      } else if (age > 120) {
        dobValid = false; dobValue = '';
        showErr(dobError, 'Please enter a valid date of birth.');
      } else {
        dobValid = true; dobValue = v;
      }
      refreshUI();
    });

    // ─── Link Google ──────────────────────────────────────────────────
    googleBtn.addEventListener('click', async () => {
      clearErr(googleErr);
      if (!currentUser) { showErr(googleErr, 'Please sign in again.'); return; }
      try {
        const provider = new GoogleAuthProvider();
        const result = await linkWithPopup(currentUser, provider);
        const linked = (result.user.providerData || []).find(p => p.providerId === 'google.com');
        const linkedEmail = (linked && linked.email) || result.user.email || '';
        if (!isGmail(linkedEmail)) {
          showErr(googleErr, 'Please link a @gmail.com Google account.');
          return;
        }
        if (currentUser.email && linkedEmail.toLowerCase() !== currentUser.email.toLowerCase()) {
          showErr(googleErr, 'Please link the same Gmail you signed up with (' + currentUser.email + ').');
          return;
        }
        currentUser = result.user;
        refreshUI();
      } catch (err) {
        const c = String(err?.code || '');
        if (/provider-already-linked/.test(c)) { refreshUI(); return; }
        if (/credential-already-in-use|email-already-in-use/.test(c))
          showErr(googleErr, 'That Google account is already linked to another Mathagram account.');
        else if (/popup-closed-by-user|cancelled-popup-request/.test(c))
          showErr(googleErr, 'Sign-in cancelled. Try again when ready.');
        else
          showErr(googleErr, (err?.message || 'Could not link Google account.').replace(/^Firebase:\s*/, ''));
      }
    });

    // ─── Finish ───────────────────────────────────────────────────────
    finishBtn.addEventListener('click', async () => {
      clearErr(finishErr);
      if (!(dobValid && hasGoogle())) return;
      finishBtn.disabled = true;
      const orig = finishBtn.textContent;
      finishBtn.textContent = 'Saving…';
      try {
        await updateDoc(doc(db, 'users', currentUser.uid), {
          birthday: dobValue,
          birthdayConfirmedAt: new Date().toISOString()
        });
        window.location.assign('/profile.html');
      } catch (err) {
        showErr(finishErr, 'Could not save. Please try again.');
        finishBtn.disabled = false;
        finishBtn.textContent = orig;
      }
    });

    // ─── Boot: require login, skip if already complete ────────────────
    onAuthStateChanged(auth, async (user) => {
      if (!user) { window.location.assign('/login.html'); return; }
      currentUser = user;
      try {
        const snap = await getDoc(doc(db, 'users', user.uid));
        const data = snap.exists() ? snap.data() : null;
        if (data && data.birthday) { dobValid = true; dobValue = data.birthday; }
        if (data && data.birthday && hasGoogle()) {
          window.location.assign('/profile.html'); return;
        }
      } catch (e) { /* fall through to show form */ }
      refreshUI();
    });
  </script>
</body>
</html>
```

- [ ] **Step 2: Verify (birthday + age)**

Open `http://localhost:8000/link-google.html` while signed in (sign in first via `login.html`). 
- Enter a DOB under 13 → expected: red "You must be at least 13…", birthday block not marked done, Continue stays disabled.
- Enter a DOB of 13+ → expected: birthday block turns green "✓ Birthday confirmed".

- [ ] **Step 3: Verify (link + match)**

- Click "Link Google account", pick a Google account whose email **differs** from your signup Gmail → expected: "Please link the same Gmail you signed up with (…)".
- Click again, pick the **matching** Gmail → expected: Google block turns green, button hides, and with a valid DOB the "Continue to Mathagram" button enables.
- Click Continue → expected: navigates to `/profile.html`; `users/{uid}` now has `birthday` + `birthdayConfirmedAt` (check Firebase console).
- Reload `link-google.html` → expected: immediate redirect to `/profile.html` (already complete).

- [ ] **Step 4: Commit**

```bash
git add link-google.html
git commit -m "Add required setup step: link Google (email match) + confirm 13+ birthday"
```

---

## Task 3: Site-wide gate (`js/auth-gate.js`)

**Files:**
- Modify: `js/auth-gate.js` (inside the `onAuthStateChanged` success branch, after ban checks, before `overlay.classList.add('hidden')`)

- [ ] **Step 1: Add the Google + birthday requirement**

In `js/auth-gate.js`, locate the end of the ban/suspension/strike block — specifically the line `overlay.classList.add('hidden');` inside the `if (user) { ... }` branch (currently ~line 207). Immediately **before** that line, insert:

```js
        // ─── Require linked Google account + confirmed birthday ───────
        // (reuse `userDoc`/`data` already fetched above for ban checks)
        try {
          const data2 = (typeof userDoc !== 'undefined' && userDoc.exists()) ? userDoc.data() : null;
          const hasGoogle = (user.providerData || []).some(p => p.providerId === 'google.com');
          const hasBirthday = !!(data2 && data2.birthday);
          if (!hasGoogle || !hasBirthday) {
            if (!/link-google\.html$/.test(location.pathname)) {
              window.location.href = basePath + 'link-google.html';
              return;
            }
          }
        } catch (e) { /* if anything fails, do not lock the user out of nothing */ }
```

> Note: the existing ban block declares `const userDoc = await fireMod.getDoc(...)` and `const data = userDoc.data()` **inside** a nested `try`, so `data` may be out of scope here. The snippet above re-derives `data2` from `userDoc`. If `userDoc` is also out of scope at the insertion point, instead hoist it: change the ban block's `const userDoc =` to assign to a variable declared with `let userDoc;` at the top of the `if (user)` branch, then reuse it here (no second Firestore read). Confirm scope when editing.

- [ ] **Step 2: Verify (new/incomplete user is gated)**

- Create a fresh email/password account via `login.html` but do **not** finish setup (close the tab at `link-google.html`). Then open any lesson page, e.g. `http://localhost:8000/courses/albanian/lesson-1.html`. Expected: redirected to `link-google.html`.
- Complete setup, then revisit the same lesson page. Expected: page loads normally, no redirect.

- [ ] **Step 3: Verify (no redirect loop)**

- While incomplete, confirm `link-google.html` itself loads (is not redirected onto itself).

- [ ] **Step 4: Verify (existing user is gated)**

- In Firebase console, pick a pre-existing user doc with no `birthday` (or use one). Sign in as them, open a gated page. Expected: routed to `link-google.html`.

- [ ] **Step 5: Commit**

```bash
git add js/auth-gate.js
git commit -m "Gate all pages on linked Google account + confirmed birthday"
```

---

## Task 4: Switch-account button (`profile.html`)

**Files:**
- Modify: `profile.html` (markup ~line 538; module script imports ~line 557; new handler near the sign-out handler ~line 970)

- [ ] **Step 1: Add the button markup**

In the `.profile-actions` block (currently lines 537–539), change:

```html
      <div class="profile-actions">
        <button id="btn-signout" class="btn btn-outline">Sign Out</button>
      </div>
```

to:

```html
      <div class="profile-actions">
        <button id="btn-switch-account" class="btn btn-outline">Switch Google account</button>
        <button id="btn-signout" class="btn btn-outline">Sign Out</button>
        <p id="switch-error" style="display:none;color:#ef4444;font-size:0.85rem;margin-top:10px;"></p>
      </div>
```

- [ ] **Step 2: Import the needed Firebase Auth functions**

The module script already imports `auth as fbAuth` from `firebase-config.js` (line ~557). Add an auth-SDK import directly below that line:

```js
    import { GoogleAuthProvider, signInWithPopup, signOut } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
    import { doc as fdoc, getDoc as fgetDoc, setDoc as fsetDoc, serverTimestamp } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';
```

(`doc`/`setDoc` are already imported under their plain names at line 556; the aliased names above avoid any collision for the new handler.)

- [ ] **Step 3: Add the switch-account handler**

Immediately after the existing sign-out handler (currently lines 970–973), add:

```js
    // Switch Google account
    document.getElementById('btn-switch-account').addEventListener('click', async () => {
      const errEl = document.getElementById('switch-error');
      errEl.style.display = 'none'; errEl.textContent = '';
      try {
        const provider = new GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });
        const { user } = await signInWithPopup(fbAuth, provider);
        if (!/@gmail\.com$/i.test(user.email || '')) {
          await signOut(fbAuth);
          errEl.textContent = 'Mathagram requires a @gmail.com Google account.';
          errEl.style.display = 'block';
          return;
        }
        // Ensure a profile doc exists for the switched-to account
        const ref = fdoc(db, 'users', user.uid);
        const snap = await fgetDoc(ref);
        if (!snap.exists()) {
          await fsetDoc(ref, {
            displayName: user.displayName || 'New Learner',
            email: user.email, color: 'blue', xp: 0, createdAt: serverTimestamp()
          });
        }
        // Reload profile; the gate will route to setup if birthday is missing.
        window.location.assign('/profile.html');
      } catch (err) {
        const c = String(err?.code || '');
        if (/popup-closed-by-user|cancelled-popup-request/.test(c)) return;
        errEl.textContent = (err?.message || 'Could not switch account.').replace(/^Firebase:\s*/, '');
        errEl.style.display = 'block';
      }
    });
```

- [ ] **Step 4: Verify**

Open `http://localhost:8000/profile.html` while signed in.
- Click "Switch Google account" → expected: Google chooser appears (because of `prompt: 'select_account'`).
- Pick a different `@gmail.com` account → expected: profile reloads as that account (a brand-new account is then routed to `link-google.html` by the gate from Task 3).
- If a non-Gmail Google account is selected → expected: signed out + inline Gmail error.

- [ ] **Step 5: Commit**

```bash
git add profile.html
git commit -m "Add Google-only Switch account button to profile"
```

---

## Final verification (end-to-end)

- [ ] New Gmail email signup → setup step → enter 13+ DOB → link matching Gmail → reach profile → revisit a lesson with no redirect.
- [ ] New "Sign up with Google" (Gmail) → setup step shows only birthday → complete → profile.
- [ ] Non-Gmail rejected on both email signup and Google buttons.
- [ ] Under-13 blocked inline on `link-google.html`.
- [ ] Existing user with no birthday is forced through setup once.
- [ ] Switch-account chooser works and respects Gmail-only.
- [ ] No redirect loop on `link-google.html`.

## Deploy

This is the consumer site. Deploy via the project's established Netlify direct-upload procedure (per project memory: a git push does **not** publish mathagram.org; a full-clean direct Netlify deploy is required). Deploy only after the user approves the implemented changes.

## Notes / risks

- **Firestore rules:** confirm the owner may write `birthday` / `birthdayConfirmedAt` on their own `users/{uid}` doc (existing rules already allow owner writes to that doc).
- **Firebase "one account per email":** `linkWithPopup` with a matching Gmail attaches Google to the same UID; with a different existing account it throws `credential-already-in-use` (handled).
- **Concurrency:** re-Read `login.html` before Task 1 (another process modified it during design).
- **translate.goog:** the gate's proxy branch early-returns before the Firebase block, so the new requirement does not run on translated copies — intended.
