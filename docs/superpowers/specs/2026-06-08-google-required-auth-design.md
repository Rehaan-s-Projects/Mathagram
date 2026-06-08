# Google-Required Account Flow — Design Spec

**Date:** 2026-06-08
**Status:** Approved (design)
**Scope:** Consumer Mathagram auth (`login.html`, `js/auth-gate.js`, new `link-google.html`, `profile.html`). The separate Schools product (`school.html`, `school-google.html`) is explicitly out of scope.

## Goal

Make every Mathagram account a **Gmail-backed, Google-linked, age-verified** account:

1. Only `@gmail.com` addresses may sign up.
2. Every user must link a Google account whose email matches their signup Gmail.
3. Every user must confirm a date of birth and be **at least 13 years old**.
4. The requirement applies to **all users, including those who signed up before this change** — they are forced through a one-time setup the next time they use any gated page.
5. The profile page gains a Google-only **Switch account** button.

## Background — current state

- Auth is **Firebase Auth** (project `mathagram-cb526`), config in `js/firebase-config.js`.
- `login.html` is the real signup/signin page. It has its **own inline module script** (it does *not* use `js/auth.js`). It already supports:
  - email/password signup (display name 3–13 chars, email, password, avatar color);
  - email/password signin + password reset;
  - "Continue with Google" / "Sign up with Google" via `signInWithPopup(auth, new GoogleAuthProvider())`, both wired to the same `googleAuth()` handler.
- `js/auth-gate.js` is included on **1,204 pages**. It renders a lock overlay, then on `onAuthStateChanged`:
  - if no user → show overlay;
  - if user → fetch `users/{uid}`, enforce ban/suspension/strike redirects to `violation.html`, otherwise hide the overlay.
  This single file is the site-wide chokepoint and the right place to enforce the new requirement.
- Firestore profile doc `users/{uid}` currently holds: `displayName`, `email`, `color`, `xp`, (and via `auth.js`: `level`, `streak`, `lastActive`, `createdAt`).
- `js/auth.js` exists but is **not** the path login.html uses; `auth.js.signUp` is the only place currently calling `sendEmailVerification`. We will not rely on email-link verification (see Decisions).

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Where to enforce "Google + birthday required" | In `js/auth-gate.js` only | One file → all 1,204 pages and all existing users, no per-page edits |
| How to "link" Google to an email/password account | `linkWithPopup(currentUser, GoogleAuthProvider)` | Keeps the same Firebase UID, preserves XP/profile |
| Email verification | **None** (no email-link blocking) | The required Google link, with email-match, proves Gmail ownership |
| Birthday source | User types it on the setup step | Firebase Google sign-in does not return DOB without extra People-API scope most accounts won't grant |
| Minimum age | **13+**, under-13 blocked inline | Standard education/COPPA threshold; under-13 stays on `link-google.html` with a message, DOB not saved |
| Too-young / incomplete UX | Inline message on `link-google.html` | No separate blocked page needed |

## Components

### 1. Gmail-only enforcement — `login.html` (inline script)

- **Email signup handler:** before `createUserWithEmailAndPassword`, validate the (already-lowercased, trimmed) email ends with `@gmail.com`. On failure, show: *"Mathagram requires a Gmail address (@gmail.com). Please sign up with your Gmail."* and abort.
- **Google handler (`googleAuth`)** (used by both Google buttons): after `signInWithPopup`, if `user.email` does not end with `@gmail.com`, call `signOut(auth)` and show the same Gmail error; do not proceed.
- **Post-signup redirect:** after a successful **email** signup (account created + Firestore profile written), redirect to `link-google.html` instead of `profile.html`. (Google-button users already have Google linked, but still must pass the gate's birthday check — the gate will route them to `link-google.html` if `birthday` is missing.)
- Helper: a single `isGmail(email)` check, e.g. `/@gmail\.com$/i.test(email)`.

### 2. Required setup step — new `link-google.html`

A standalone page styled like `login.html` (reuse `.auth-card` patterns). It does **not** include `js/auth-gate.js` (would cause a redirect loop); it implements its own auth logic.

**On load:**
- `onAuthStateChanged`: if no user → redirect to `login.html`.
- If the user already has a `google.com` provider **and** a `birthday` in `users/{uid}` → redirect to `profile.html` (nothing to do).
- Otherwise render the setup form, showing only the missing requirement(s).

**Birthday section:**
- A date-of-birth input (`<input type="date">` or three selects; date input is simplest).
- Compute age from DOB vs. today. If `< 13`: show *"You must be at least 13 to use Mathagram."*, keep them on the page, do **not** save.
- Only a valid 13+ DOB is accepted.

**Link Google section:**
- Button "Link your Google account" → `linkWithPopup(auth.currentUser, new GoogleAuthProvider())`.
- After linking, read the linked Google identity's email from the result/`providerData`. If it does **not** equal the account's signup email (case-insensitive), reject: unlink is not required, but show *"Please link the same Gmail you signed up with ("+email+")."* and treat the step as incomplete. (Implementation note: compare against `auth.currentUser.email`; the Google provider email is in the `google.com` entry of `providerData` or the `linkWithPopup` result's `user.providerData`.)
- Known Firebase error to handle: `auth/credential-already-in-use` (that Google account is already attached to a different Mathagram user) → message *"That Google account is already linked to another Mathagram account."*; `auth/provider-already-linked` → treat as success.

**Completion:**
- The step completes only when the user has **both** a `google.com` provider and a valid 13+ DOB.
- On completion, write to `users/{uid}`: `birthday` (`"YYYY-MM-DD"`) and `birthdayConfirmedAt` (ISO string), then redirect to `profile.html`.
- Order is flexible (enter DOB, then link, or vice-versa); the page re-checks both conditions and only redirects when both hold.

### 3. The gate — `js/auth-gate.js`

Extend the existing `onAuthStateChanged(user)` branch, **after** the ban/suspension/strike checks pass and **before** `overlay.classList.add('hidden')`:

```
// (userDoc already fetched above for ban checks; reuse `data`)
const hasGoogle = (user.providerData || []).some(p => p.providerId === 'google.com');
const hasBirthday = !!(data && data.birthday);
if (!hasGoogle || !hasBirthday) {
  // avoid looping on the setup page itself
  if (!/link-google\.html$/.test(location.pathname)) {
    window.location.href = basePath + 'link-google.html';
    return;
  }
}
```

Notes:
- Reuse the `userDoc`/`data` already loaded for the ban check — **no extra Firestore read**.
- If `userDoc` does not exist yet (edge case), treat `hasBirthday` as false → routed to setup.
- `link-google.html` is excluded from the redirect (and does not load this script anyway), preventing loops.
- Translate.goog proxy path is unaffected (it already early-returns before the Firebase block).

### 4. Switch-account button — `profile.html`

- Add a **"Switch account"** button in the profile UI (near the existing logout/account controls).
- Handler: `const provider = new GoogleAuthProvider(); provider.setCustomParameters({ prompt: 'select_account' }); await signInWithPopup(auth, provider);`
  - Using `signInWithPopup` (not link) re-authenticates as the chosen Google account, effectively switching.
  - Apply the **Gmail-only** check: if the chosen account's email isn't `@gmail.com`, `signOut` + error.
  - After a successful switch, redirect to `profile.html` (reload) — an existing account lands on its profile; a brand-new account will be routed by the gate to `link-google.html` for birthday setup.
- Reuse the same Firestore "create profile if missing" logic already present in the Google sign-in handlers so a newly-chosen account gets a profile doc.

## Data model changes

`users/{uid}` gains:
- `birthday` — `string`, `"YYYY-MM-DD"`. Presence implies the user is 13+ (only stored when valid).
- `birthdayConfirmedAt` — `string`, ISO timestamp.

No Firestore-rules change is strictly required for these fields (owner already writes their own doc), but confirm existing rules allow the owner to update these keys.

## Data flow

**New email user:** signup (Gmail enforced) → profile doc created → redirect `link-google.html` → enter DOB (13+) + link Google (email match) → `birthday` saved → `profile.html`. Gate now passes everywhere.

**New Google user:** "Sign up with Google" (Gmail enforced) → profile doc created, Google already linked → redirect (gate) to `link-google.html` → enter DOB only → saved → `profile.html`.

**Existing user (pre-change):** visits any gated page → gate sees missing `google.com` provider and/or missing `birthday` → redirect `link-google.html` → completes missing requirement(s) → `profile.html`.

**Switch account:** profile → "Switch account" → Google chooser → (Gmail enforced) → existing account → profile; new account → gate → setup.

## Error handling

- Gmail violations: inline error, no account state changed beyond `signOut` for Google paths.
- `linkWithPopup`: handle `auth/credential-already-in-use`, `auth/provider-already-linked`, `auth/popup-closed-by-user`, `auth/cancelled-popup-request` with friendly messages (mirror the existing `friendly()` mapper in `login.html`).
- Email mismatch on link: friendly message, step stays incomplete.
- Firestore write failure on completion: show error, do not redirect; allow retry.

## Testing / verification

Manual (static site, Firebase live):
1. Email signup with non-Gmail → rejected.
2. Email signup with Gmail → lands on `link-google.html`.
3. Under-13 DOB → blocked inline, not saved.
4. Link a *different* Gmail than signup → rejected.
5. Link the matching Gmail + 13+ DOB → reaches profile; revisiting gated pages no longer redirects.
6. Existing account (no Google / no birthday) → forced through setup once.
7. "Sign up with Google" non-Gmail → rejected; Gmail → setup asks only for birthday.
8. Profile "Switch account" → chooser appears; non-Gmail rejected; switching to a new Gmail routes to setup.
9. No redirect loop on `link-google.html`.

## Out of scope

- `school.html` / `school-google.html` Schools product.
- Email-link (click-to-verify) enforcement.
- Pulling birthday automatically from Google.
- Retroactive deletion of existing non-Gmail accounts (they are funneled through Google linking instead).
