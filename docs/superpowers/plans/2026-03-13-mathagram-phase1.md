# Mathagram.org Phase 1 — Foundation & Core Platform

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the existing "Rehaan — Master Integrals" site into the Mathagram.org platform with light theme, lighthouse branding, global CSS, exercise engine, character system, Firebase auth, XP/levels, and one complete course (Calculus) as a template.

**Architecture:** Static HTML/CSS/JS frontend with Firebase for authentication and Firestore for user data. Shared JS modules handle exercises, characters, XP, and auth. Each course is a folder of HTML files that load shared modules.

**Tech Stack:** HTML5, CSS3, vanilla JS (ES modules), Firebase Auth, Firestore, KaTeX, SVG

**Spec:** `docs/superpowers/specs/2026-03-13-mathagram-design.md`

---

## File Structure

```
mathagram/                          (renamed from rehan-calculus/)
  index.html                        — Homepage with lighthouse hero + course catalog
  login.html                        — Login/signup page
  profile.html                      — User profile with XP/lighthouse/grades
  terms.html                        — Terms of Service
  privacy.html                      — Privacy Policy
  course/
    calculus/
      index.html                    — Calculus course overview
      lesson-1.html                 — What Are Integrals (content + exercises)
      lesson-2.html                 — Indefinite Integrals (content + exercises)
      lesson-3.html                 — Definite Integrals (content + exercises)
      lesson-4.html                 — U-Substitution (content + exercises)
  css/
    global.css                      — Light theme, layout, nav, footer, responsive
    exercises.css                   — All 6 exercise type styles
    lighthouse.css                  — Lighthouse loading + profile animations
    characters.css                  — Character buddy popup styles
  js/
    firebase-config.js              — Firebase app initialization
    auth.js                         — Sign up, sign in, sign out, auth state listener
    progress.js                     — XP calculation, grading, levels, Firestore CRUD
    exercises.js                    — Exercise engine: render, check, score all 6 types
    characters.js                   — Character data, buddy popup, encouragement messages
    lighthouse.js                   — Loading animation + profile lighthouse renderer
    sanitize.js                     — Input sanitization utility
  assets/
    characters/
      edam.svg                      — Bear character (3 expressions)
      steve.svg                     — Fox character (3 expressions)
      james.svg                     — Strong man character (3 expressions)
      diego.svg                     — Researcher character (3 expressions)
      rita.svg                      — Cat character (3 expressions)
      sam.svg                       — Kid character (3 expressions)
      william.svg                   — Old man character (3 expressions)
      gosia.svg                     — Girl character (3 expressions)
    lighthouse/
      logo.svg                      — Mathagram lighthouse logo
      loading.svg                   — Loading animation lighthouse
    icons/
      math.svg                      — Blue math category icon
      science.svg                   — Green science category icon
      data.svg                      — Red data analysis category icon
      logic.svg                     — Orange logic category icon
  firestore.rules                   — Firestore security rules
```

---

## Chunk 1: Global Styles, Lighthouse, & Homepage

### Task 1: Create global.css — Light theme foundation

**Files:**
- Create: `css/global.css`

- [ ] **Step 1: Create CSS file with design tokens and base styles**

```css
/* css/global.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  /* Brand */
  --primary: #00e5c8;
  --primary-light: #5effe0;
  --primary-dark: #00b89f;
  --primary-glow: rgba(0, 229, 200, 0.12);

  /* Category colors */
  --math-blue: #3b82f6;
  --math-blue-bg: #eff6ff;
  --science-green: #22c55e;
  --science-green-bg: #f0fdf4;
  --data-red: #ef4444;
  --data-red-bg: #fef2f2;
  --logic-orange: #f97316;
  --logic-orange-bg: #fff7ed;

  /* XP / Levels */
  --xp-gold: #eab308;
  --xp-gold-bg: #fefce8;

  /* Light theme */
  --bg: #f8f9fa;
  --bg-white: #ffffff;
  --text: #1a1a2e;
  --text-secondary: #64748b;
  --text-muted: #94a3b8;
  --border: #e2e8f0;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
  --radius: 12px;
  --radius-lg: 16px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  overflow-x: hidden;
}

a { color: var(--primary-dark); text-decoration: none; }
a:hover { color: var(--primary); }

/* Navigation */
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 2rem;
}

.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text);
  text-decoration: none;
}

.nav-logo img { height: 32px; width: auto; }

.nav-links {
  display: flex;
  gap: 0.25rem;
  list-style: none;
  align-items: center;
}

.nav-links a {
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.nav-links a:hover {
  color: var(--primary-dark);
  background: var(--primary-glow);
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 1.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-primary {
  background: var(--primary);
  color: #fff;
  box-shadow: 0 4px 16px rgba(0,229,200,0.3);
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(0,229,200,0.4);
  color: #fff;
}

.btn-outline {
  background: transparent;
  color: var(--text);
  border: 2px solid var(--border);
}

.btn-outline:hover {
  border-color: var(--primary);
  color: var(--primary-dark);
}

/* Footer */
.footer {
  text-align: center;
  padding: 3rem 2rem;
  border-top: 1px solid var(--border);
  margin-top: 4rem;
  background: var(--bg-white);
}

.footer-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 0.5rem;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin: 1rem 0;
  list-style: none;
}

.footer-links a {
  color: var(--text-muted);
  font-size: 0.85rem;
}

.footer-links a:hover { color: var(--primary-dark); }

.footer-copyright {
  color: var(--text-muted);
  font-size: 0.8rem;
  margin-top: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .nav { padding: 0 1rem; }
}

/* Content sections */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Category section backgrounds */
.category-section { padding: 4rem 0; }

.category-math { background: var(--math-blue-bg); }
.category-science { background: var(--science-green-bg); }
.category-data { background: var(--data-red-bg); }
.category-logic { background: var(--logic-orange-bg); }

.category-title {
  font-size: 1.8rem;
  font-weight: 800;
  margin-bottom: 2rem;
}

.category-math .category-title { color: var(--math-blue); }
.category-science .category-title { color: var(--science-green); }
.category-data .category-title { color: var(--data-red); }
.category-logic .category-title { color: var(--logic-orange); }

/* Course cards */
.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.course-card {
  background: var(--bg-white);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  transition: all 0.2s ease;
  text-decoration: none;
  color: var(--text);
  display: block;
}

.course-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
  color: var(--text);
}

.course-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.course-card p {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.5;
}
```

- [ ] **Step 2: Verify file is created**

Run: `ls -la css/global.css`
Expected: File exists with content

- [ ] **Step 3: Commit**

```bash
git add css/global.css
git commit -m "feat: add global.css with light theme and design tokens"
```

---

### Task 2: Create lighthouse assets and animations

**Files:**
- Create: `assets/lighthouse/logo.svg`
- Create: `assets/lighthouse/loading.svg`
- Create: `css/lighthouse.css`
- Create: `js/lighthouse.js`

- [ ] **Step 1: Create lighthouse logo SVG**

Create `assets/lighthouse/logo.svg` — a clean, minimal lighthouse icon with cyan beam. The beam subtly suggests the letter "M". Simple geometric shapes, suitable for favicon and nav bar.

- [ ] **Step 2: Create lighthouse loading SVG**

Create `assets/lighthouse/loading.svg` — a larger lighthouse used for the loading animation. Beam extends across the full width.

- [ ] **Step 3: Create lighthouse.css**

```css
/* css/lighthouse.css */

/* Loading screen overlay */
.lighthouse-loading {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: var(--bg-white);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  transition: opacity 0.6s ease;
}

.lighthouse-loading.fade-out {
  opacity: 0;
  pointer-events: none;
}

.lighthouse-loading .lighthouse-icon {
  width: 80px;
  height: auto;
}

.lighthouse-loading .beam {
  position: absolute;
  top: 35%;
  left: 50%;
  width: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary), transparent);
  border-radius: 4px;
  animation: beam-sweep 1.5s ease-out forwards;
}

@keyframes beam-sweep {
  0% { width: 0; opacity: 1; }
  70% { width: 60vw; opacity: 0.8; }
  100% { width: 100vw; opacity: 0; }
}

/* Profile lighthouse — glows based on level */
.lighthouse-profile {
  width: 120px;
  margin: 0 auto 2rem;
  position: relative;
}

.lighthouse-profile svg { width: 100%; height: auto; }

.lighthouse-profile .glow {
  position: absolute;
  top: 0; left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--xp-gold) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.5s ease;
}

/* Glow intensity based on level (set via JS) */
.lighthouse-profile[data-level="1"] .glow { opacity: 0.1; }
.lighthouse-profile[data-level="2"] .glow { opacity: 0.2; }
.lighthouse-profile[data-level="3"] .glow { opacity: 0.3; }
.lighthouse-profile[data-level="4"] .glow { opacity: 0.45; }
.lighthouse-profile[data-level="5"] .glow { opacity: 0.55; }
.lighthouse-profile[data-level="6"] .glow { opacity: 0.7; }
.lighthouse-profile[data-level="7"] .glow { opacity: 0.85; }
.lighthouse-profile[data-level="8"] .glow { opacity: 1.0; }
```

- [ ] **Step 4: Create lighthouse.js**

```js
// js/lighthouse.js

/**
 * Shows the lighthouse loading animation on first visit.
 * Stores a flag in sessionStorage so it only plays once per session.
 */
export function initLoadingAnimation() {
  if (sessionStorage.getItem('mathagram-loaded')) {
    const loader = document.getElementById('lighthouse-loading');
    if (loader) loader.remove();
    return;
  }

  const loader = document.getElementById('lighthouse-loading');
  if (!loader) return;

  setTimeout(() => {
    loader.classList.add('fade-out');
    setTimeout(() => {
      loader.remove();
      sessionStorage.setItem('mathagram-loaded', 'true');
    }, 600);
  }, 2000);
}

/**
 * Sets the lighthouse glow level on the profile page.
 * @param {number} level - User's current level (1-8)
 */
export function setLighthouseLevel(level) {
  const el = document.querySelector('.lighthouse-profile');
  if (el) {
    el.setAttribute('data-level', Math.min(Math.max(level, 1), 8));
  }
}
```

- [ ] **Step 5: Verify files exist**

Run: `ls -la assets/lighthouse/ css/lighthouse.css js/lighthouse.js`
Expected: All 4 files exist

- [ ] **Step 6: Commit**

```bash
git add assets/lighthouse/ css/lighthouse.css js/lighthouse.js
git commit -m "feat: add lighthouse logo, loading animation, and profile glow"
```

---

### Task 3: Create homepage (index.html)

**Files:**
- Create: `index.html` (overwrite existing)

- [ ] **Step 1: Build homepage with lighthouse loading, hero, course catalog**

The homepage includes:
- Lighthouse loading overlay (plays once per session)
- Nav bar with Mathagram logo, links (Courses, Login/Sign Up)
- Hero section: Mathagram logo + "Learn math & science, your way" + Get Started button
- Course catalog in 4 color-coded sections (Math=blue, Science=green, Data Analysis=red, Logic=orange)
- Each section shows course cards in a grid
- Footer with copyright (dynamic year), Terms, Privacy links, "Built by Rehaan Rashid"
- Includes: `css/global.css`, `css/lighthouse.css`
- Scripts: `js/lighthouse.js` (ES module)
- KaTeX CDN links
- Content Security Policy meta tag

Key HTML structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://cdn.jsdelivr.net https://www.gstatic.com https://apis.google.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; font-src https://fonts.gstatic.com; connect-src https://firestore.googleapis.com https://identitytoolkit.googleapis.com https://www.googleapis.com;">
  <title>Mathagram — Learn Math & Science, Your Way</title>
  <link rel="icon" href="assets/lighthouse/logo.svg">
  <link rel="stylesheet" href="css/global.css">
  <link rel="stylesheet" href="css/lighthouse.css">
</head>
<body>
  <!-- Loading -->
  <div id="lighthouse-loading" class="lighthouse-loading">
    <img src="assets/lighthouse/logo.svg" class="lighthouse-icon" alt="Mathagram">
    <div class="beam"></div>
  </div>

  <!-- Nav -->
  <nav class="nav">...</nav>

  <!-- Hero -->
  <section class="hero">...</section>

  <!-- Math (Blue) -->
  <section class="category-section category-math">
    <div class="container">
      <h2 class="category-title">Math</h2>
      <div class="course-grid">
        <!-- Course cards: Calculus, Algebra, Trigonometry, AP Statistics, Exponential Functions, Coordinate Transformations -->
      </div>
    </div>
  </section>

  <!-- Science (Green) -->
  <section class="category-section category-science">...</section>

  <!-- Data Analysis (Red) -->
  <section class="category-section category-data">...</section>

  <!-- Logic (Orange) -->
  <section class="category-section category-logic">...</section>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-logo"><img src="assets/lighthouse/logo.svg" alt="" height="24"> Mathagram</div>
    <ul class="footer-links">
      <li><a href="terms.html">Terms of Service</a></li>
      <li><a href="privacy.html">Privacy Policy</a></li>
      <li><a href="https://linktr.ee/Rehaan_rashid" target="_blank">Contact</a></li>
    </ul>
    <p class="footer-copyright">&copy; <span id="year"></span> Mathagram.org — All Rights Reserved. Built by Rehaan Rashid</p>
  </footer>

  <script type="module">
    import { initLoadingAnimation } from './js/lighthouse.js';
    initLoadingAnimation();
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
```

- [ ] **Step 2: Open in browser and verify**

Run: `open index.html`
Expected: Light theme, lighthouse loading plays, course catalog visible, footer with copyright

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add Mathagram homepage with lighthouse loading and course catalog"
```

---

## Chunk 2: Firebase Auth & Security

### Task 4: Set up Firebase configuration

**Files:**
- Create: `js/firebase-config.js`

- [ ] **Step 1: Create Firebase config module**

```js
// js/firebase-config.js
// Firebase SDK loaded via CDN in HTML files.
// This module initializes Firebase app and exports auth/db references.
//
// IMPORTANT: Replace the config values below with your actual Firebase project config.
// These are NOT secrets — Firebase config is public by design.
// Security is enforced via Firestore rules (see firestore.rules).

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js';
import { getAuth } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
import { getFirestore } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
```

- [ ] **Step 2: Commit**

```bash
git add js/firebase-config.js
git commit -m "feat: add Firebase configuration module (placeholder credentials)"
```

---

### Task 5: Create Firestore security rules

**Files:**
- Create: `firestore.rules`

- [ ] **Step 1: Write security rules**

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Users can only read/write their own profile
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;

      // User's course progress
      match /progress/{courseId} {
        allow read, write: if request.auth != null && request.auth.uid == userId;

        // User's lesson results
        match /lessons/{lessonId} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }

    // Deny everything else
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add firestore.rules
git commit -m "feat: add Firestore security rules — users can only access own data"
```

---

### Task 6: Create auth.js — Login/signup/logout

**Files:**
- Create: `js/auth.js`

- [ ] **Step 1: Create auth module**

```js
// js/auth.js
import { auth } from './firebase-config.js';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  sendEmailVerification
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
import { db } from './firebase-config.js';
import { doc, setDoc, getDoc } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

/**
 * Sign up a new user with email/password.
 * Creates a Firestore user doc with default values.
 * @param {string} email
 * @param {string} password
 * @param {string} displayName
 * @param {string} character - chosen character ID (e.g., 'edam')
 * @returns {Promise<object>} Firebase user object
 */
export async function signUp(email, password, displayName, character) {
  const cred = await createUserWithEmailAndPassword(auth, email, password);
  await sendEmailVerification(cred.user);

  // Create user document in Firestore
  await setDoc(doc(db, 'users', cred.user.uid), {
    displayName: sanitizeText(displayName),
    character: character,
    xp: 0,
    level: 1,
    streak: 0,
    lastActive: new Date().toISOString(),
    createdAt: new Date().toISOString()
  });

  return cred.user;
}

/**
 * Sign in existing user.
 * @param {string} email
 * @param {string} password
 * @returns {Promise<object>} Firebase user object
 */
export async function signIn(email, password) {
  const cred = await signInWithEmailAndPassword(auth, email, password);
  return cred.user;
}

/**
 * Sign out the current user.
 */
export async function logOut() {
  await signOut(auth);
}

/**
 * Listen for auth state changes.
 * @param {function} callback - receives user object or null
 */
export function onAuthChange(callback) {
  onAuthStateChanged(auth, callback);
}

/**
 * Get current user's Firestore profile.
 * @returns {Promise<object|null>}
 */
export async function getUserProfile() {
  const user = auth.currentUser;
  if (!user) return null;
  const snap = await getDoc(doc(db, 'users', user.uid));
  return snap.exists() ? snap.data() : null;
}

/**
 * Basic text sanitization to prevent XSS.
 */
function sanitizeText(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
```

- [ ] **Step 2: Commit**

```bash
git add js/auth.js
git commit -m "feat: add auth.js with signup, signin, signout, and profile creation"
```

---

### Task 7: Create login.html page

**Files:**
- Create: `login.html`

- [ ] **Step 1: Build login/signup page**

The page includes:
- Nav bar (same as homepage)
- Tabbed form: "Sign In" and "Sign Up" tabs
- Sign In: email + password fields + submit button
- Sign Up: display name + email + password + character picker (8 characters shown as selectable cards) + submit button
- Error message display area
- Redirect to profile.html on success
- Footer with copyright
- CSP meta tag
- Imports: `css/global.css`, `js/auth.js`, `js/characters.js`

- [ ] **Step 2: Verify in browser**

Run: `open login.html`
Expected: Clean light-themed login page with tabs, character picker visible on Sign Up tab

- [ ] **Step 3: Commit**

```bash
git add login.html
git commit -m "feat: add login/signup page with character picker"
```

---

### Task 8: Create sanitize.js utility

**Files:**
- Create: `js/sanitize.js`

- [ ] **Step 1: Create sanitization module**

```js
// js/sanitize.js

/**
 * Sanitize a string for safe HTML insertion.
 * Escapes HTML entities to prevent XSS.
 * @param {string} str - raw user input
 * @returns {string} sanitized string
 */
export function sanitizeHTML(str) {
  const div = document.createElement('div');
  div.textContent = String(str);
  return div.innerHTML;
}

/**
 * Validate that input matches expected patterns.
 * Used for fill-in-the-blank exercise answers.
 * @param {string} input - user answer
 * @param {number} maxLength - maximum allowed length
 * @returns {string} trimmed, length-limited input
 */
export function sanitizeAnswer(input, maxLength = 200) {
  return String(input).trim().slice(0, maxLength);
}
```

- [ ] **Step 2: Commit**

```bash
git add js/sanitize.js
git commit -m "feat: add input sanitization utility"
```

---

## Chunk 3: Characters & XP/Level System

### Task 9: Create character SVG assets

**Files:**
- Create: `assets/characters/edam.svg` (bear — 3 expressions encoded as CSS classes)
- Create: `assets/characters/steve.svg` (fox)
- Create: `assets/characters/james.svg` (strong man)
- Create: `assets/characters/diego.svg` (researcher)
- Create: `assets/characters/rita.svg` (cat)
- Create: `assets/characters/sam.svg` (kid)
- Create: `assets/characters/william.svg` (old man)
- Create: `assets/characters/gosia.svg` (girl)

- [ ] **Step 1: Create all 8 character SVGs**

Each SVG is a simple, clean, Duolingo-style character illustration. Each file contains 3 expression variants controlled by CSS classes:
- `.expression-happy` — big smile, shown on correct answer
- `.expression-thinking` — neutral/pondering, shown for hints
- `.expression-encouraging` — supportive look, shown on wrong answer

Style: Simple geometric shapes, rounded features, friendly. Small enough for bottom-right popup (roughly 80x80px display size).

- [ ] **Step 2: Verify all files exist**

Run: `ls assets/characters/`
Expected: edam.svg, steve.svg, james.svg, diego.svg, rita.svg, sam.svg, william.svg, gosia.svg

- [ ] **Step 3: Commit**

```bash
git add assets/characters/
git commit -m "feat: add 8 character SVGs with 3 expression variants each"
```

---

### Task 10: Create characters.js and characters.css

**Files:**
- Create: `js/characters.js`
- Create: `css/characters.css`

- [ ] **Step 1: Create characters.js**

```js
// js/characters.js

export const CHARACTERS = {
  edam:    { name: 'Edam',    type: 'Bear',       file: 'edam.svg',    messages: { correct: 'You got this! Great job!', wrong: 'No worries, try again!', hint: 'Think about it...', perfect: 'Absolutely perfect!' } },
  steve:   { name: 'Steve',   type: 'Fox',        file: 'steve.svg',   messages: { correct: 'Sly move, that\'s correct!', wrong: 'Tricky one! Give it another shot.', hint: 'Hmm, what if you tried...', perfect: 'Brilliant! Outsmarted it!' } },
  james:   { name: 'James',   type: 'Strong Man', file: 'james.svg',   messages: { correct: 'Crush it! Let\'s go!', wrong: 'Shake it off, try again!', hint: 'Power through this one...', perfect: 'BEAST MODE! Flawless!' } },
  diego:   { name: 'Diego',   type: 'Researcher', file: 'diego.svg',   messages: { correct: 'Fascinating! Correct!', wrong: 'Interesting... not quite. Retry?', hint: 'Consider the data...', perfect: 'Remarkable precision!' } },
  rita:    { name: 'Rita',    type: 'Cat',        file: 'rita.svg',    messages: { correct: 'Purrfect answer.', wrong: 'Nah, try again.', hint: 'Hmm, curious...', perfect: 'Purrfectly flawless!' } },
  sam:     { name: 'Sam',     type: 'Kid',        file: 'sam.svg',     messages: { correct: 'Woohoo! You nailed it!', wrong: 'Oops! One more try!', hint: 'Ooh, what about...', perfect: 'YESSS! Perfect score!' } },
  william: { name: 'William', type: 'Old Man',    file: 'william.svg', messages: { correct: 'Well done, young scholar.', wrong: 'Patience. Try once more.', hint: 'In my experience...', perfect: 'Exemplary work, truly.' } },
  gosia:   { name: 'Gosia',   type: 'Girl',       file: 'gosia.svg',   messages: { correct: 'Amazing work!', wrong: 'Almost! You\'ve got this!', hint: 'Here\'s a thought...', perfect: 'Absolutely stunning!' } }
};

/**
 * Show the character buddy popup with a message.
 * @param {string} characterId - key from CHARACTERS
 * @param {'correct'|'wrong'|'hint'|'perfect'} reaction
 */
export function showBuddy(characterId, reaction) {
  const char = CHARACTERS[characterId];
  if (!char) return;

  let popup = document.getElementById('character-buddy');
  if (!popup) {
    popup = document.createElement('div');
    popup.id = 'character-buddy';
    popup.className = 'character-buddy';
    popup.innerHTML = '<img class="buddy-img" alt=""><p class="buddy-msg"></p>';
    document.body.appendChild(popup);
  }

  const expressionMap = { correct: 'happy', wrong: 'encouraging', hint: 'thinking', perfect: 'happy' };

  popup.querySelector('.buddy-img').src = `assets/characters/${char.file}`;
  popup.querySelector('.buddy-img').alt = char.name;
  popup.querySelector('.buddy-msg').textContent = char.messages[reaction];
  popup.className = `character-buddy show expression-${expressionMap[reaction]}`;

  // Auto-hide after 3 seconds
  clearTimeout(popup._timer);
  popup._timer = setTimeout(() => {
    popup.classList.remove('show');
  }, 3000);
}

/**
 * Returns array of all characters for the picker UI.
 */
export function getAllCharacters() {
  return Object.entries(CHARACTERS).map(([id, data]) => ({ id, ...data }));
}
```

- [ ] **Step 2: Create characters.css**

```css
/* css/characters.css */

/* Character buddy popup */
.character-buddy {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: var(--bg-white);
  border: 2px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: var(--shadow-lg);
  transform: translateY(120%);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 200;
  max-width: 320px;
}

.character-buddy.show {
  transform: translateY(0);
}

.character-buddy.expression-happy { border-color: var(--science-green); }
.character-buddy.expression-thinking { border-color: var(--xp-gold); }
.character-buddy.expression-encouraging { border-color: var(--logic-orange); }

.buddy-img {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  flex-shrink: 0;
}

.buddy-msg {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text);
  line-height: 1.4;
}

/* Character picker (signup) */
.character-picker {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}

.character-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  border: 2px solid var(--border);
  border-radius: var(--radius);
  cursor: pointer;
  transition: all 0.2s ease;
  background: var(--bg-white);
}

.character-option:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
}

.character-option.selected {
  border-color: var(--primary);
  background: var(--primary-glow);
}

.character-option img {
  width: 48px;
  height: 48px;
}

.character-option .char-name {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.character-option .char-type {
  font-size: 0.65rem;
  color: var(--text-muted);
}

@media (max-width: 768px) {
  .character-picker { grid-template-columns: repeat(2, 1fr); }
  .character-buddy { bottom: 1rem; right: 1rem; left: 1rem; max-width: none; }
}
```

- [ ] **Step 3: Commit**

```bash
git add js/characters.js css/characters.css
git commit -m "feat: add character system with buddy popup and picker UI"
```

---

### Task 11: Create progress.js — XP, levels, grades

**Files:**
- Create: `js/progress.js`

- [ ] **Step 1: Create progress module**

```js
// js/progress.js
import { db, auth } from './firebase-config.js';
import { doc, getDoc, setDoc, updateDoc, increment } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

export const LEVELS = [
  { level: 1, xp: 0,    title: 'Spark' },
  { level: 2, xp: 50,   title: 'Beam' },
  { level: 3, xp: 150,  title: 'Glow' },
  { level: 4, xp: 300,  title: 'Flare' },
  { level: 5, xp: 500,  title: 'Radiance' },
  { level: 6, xp: 800,  title: 'Beacon' },
  { level: 7, xp: 1200, title: 'Lighthouse Keeper' },
  { level: 8, xp: 1800, title: 'Lighthouse Master' }
];

/**
 * Calculate level from XP.
 * @param {number} xp
 * @returns {object} { level, title, xpForNext, xpProgress }
 */
export function calculateLevel(xp) {
  let current = LEVELS[0];
  for (const l of LEVELS) {
    if (xp >= l.xp) current = l;
    else break;
  }
  const next = LEVELS[current.level] || null;
  return {
    level: current.level,
    title: current.title,
    xpForNext: next ? next.xp - xp : 0,
    xpProgress: next ? (xp - current.xp) / (next.xp - current.xp) : 1
  };
}

/**
 * Calculate grade from score percentage.
 * @param {number} score - 0 to 100
 * @returns {object} { grade, stars, passed }
 */
export function calculateGrade(score) {
  if (score >= 95) return { grade: 'A',  stars: 3, passed: true };
  if (score >= 90) return { grade: 'A-', stars: 3, passed: true };
  if (score >= 85) return { grade: 'B+', stars: 2, passed: true };
  if (score >= 80) return { grade: 'B',  stars: 2, passed: true };
  if (score >= 75) return { grade: 'B-', stars: 2, passed: true };
  if (score >= 70) return { grade: 'C+', stars: 1, passed: true };
  if (score >= 65) return { grade: 'C',  stars: 1, passed: true };
  if (score >= 60) return { grade: 'C-', stars: 1, passed: true };
  if (score >= 50) return { grade: 'D',  stars: 0, passed: false };
  return               { grade: 'F',  stars: 0, passed: false };
}

/**
 * Calculate XP earned for a lesson completion.
 * @param {number} score - 0 to 100
 * @returns {number} XP earned
 */
export function calculateXP(score) {
  const { passed } = calculateGrade(score);
  if (!passed) return 0;
  let xp = 10; // base
  if (score === 100) xp += 5; // perfect bonus
  return xp;
}

/**
 * Save lesson completion to Firestore.
 * @param {string} courseId
 * @param {string} lessonId
 * @param {number} score - 0 to 100
 */
export async function saveLessonResult(courseId, lessonId, score) {
  const user = auth.currentUser;
  if (!user) return;

  const { grade, stars } = calculateGrade(score);
  const xpEarned = calculateXP(score);

  // Save lesson result
  await setDoc(
    doc(db, 'users', user.uid, 'progress', courseId, 'lessons', lessonId),
    { score, grade, stars, xpEarned, completedAt: new Date().toISOString() }
  );

  // Update user's total XP
  if (xpEarned > 0) {
    const userRef = doc(db, 'users', user.uid);
    await updateDoc(userRef, {
      xp: increment(xpEarned),
      lastActive: new Date().toISOString()
    });

    // Recalculate level
    const snap = await getDoc(userRef);
    if (snap.exists()) {
      const { level } = calculateLevel(snap.data().xp);
      await updateDoc(userRef, { level });
    }
  }

  return { grade, stars, xpEarned };
}

/**
 * Get user's progress for a course.
 * @param {string} courseId
 * @returns {Promise<object>} map of lessonId -> { grade, stars, score }
 */
export async function getCourseProgress(courseId) {
  const user = auth.currentUser;
  if (!user) return {};

  const { getDocs, collection } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
  const snap = await getDocs(collection(db, 'users', user.uid, 'progress', courseId, 'lessons'));
  const progress = {};
  snap.forEach(doc => { progress[doc.id] = doc.data(); });
  return progress;
}
```

- [ ] **Step 2: Commit**

```bash
git add js/progress.js
git commit -m "feat: add progress system with XP, levels, grades, and Firestore persistence"
```

---

## Chunk 4: Exercise Engine

### Task 12: Create exercises.js — All 6 exercise types

**Files:**
- Create: `js/exercises.js`
- Create: `css/exercises.css`

- [ ] **Step 1: Create exercises.js**

```js
// js/exercises.js
import { sanitizeHTML, sanitizeAnswer } from './sanitize.js';

/**
 * Exercise engine that renders and scores all 6 exercise types.
 *
 * Exercise data format:
 * {
 *   type: 'multiple-choice' | 'matching' | 'fill-blank' | 'ordering' | 'true-false' | 'visual',
 *   question: string,
 *   ...type-specific fields
 * }
 */

/**
 * Render an exercise into a container element.
 * @param {HTMLElement} container
 * @param {object} exercise - exercise data object
 * @param {function} onAnswer - callback(isCorrect) when user submits
 */
export function renderExercise(container, exercise, onAnswer) {
  container.innerHTML = '';
  container.className = 'exercise-container';

  const questionEl = document.createElement('div');
  questionEl.className = 'exercise-question';
  questionEl.textContent = exercise.question;
  container.appendChild(questionEl);

  const bodyEl = document.createElement('div');
  bodyEl.className = 'exercise-body';
  container.appendChild(bodyEl);

  switch (exercise.type) {
    case 'multiple-choice': renderMultipleChoice(bodyEl, exercise, onAnswer); break;
    case 'matching':        renderMatching(bodyEl, exercise, onAnswer); break;
    case 'fill-blank':      renderFillBlank(bodyEl, exercise, onAnswer); break;
    case 'ordering':        renderOrdering(bodyEl, exercise, onAnswer); break;
    case 'true-false':      renderTrueFalse(bodyEl, exercise, onAnswer); break;
    case 'visual':          renderVisual(bodyEl, exercise, onAnswer); break;
  }
}

/** Multiple Choice — pick 1 of 4 options */
function renderMultipleChoice(container, exercise, onAnswer) {
  // exercise.options: string[], exercise.correctIndex: number
  const grid = document.createElement('div');
  grid.className = 'mc-options';

  exercise.options.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'mc-option';
    btn.textContent = opt;
    btn.addEventListener('click', () => {
      grid.querySelectorAll('.mc-option').forEach(b => b.disabled = true);
      const correct = i === exercise.correctIndex;
      btn.classList.add(correct ? 'correct' : 'wrong');
      if (!correct) grid.children[exercise.correctIndex].classList.add('correct');
      onAnswer(correct);
    });
    grid.appendChild(btn);
  });

  container.appendChild(grid);
}

/** Matching Pairs — click pairs to match */
function renderMatching(container, exercise, onAnswer) {
  // exercise.pairs: [{left, right}], shuffled for display
  const pairs = exercise.pairs;
  const leftItems = pairs.map(p => p.left);
  const rightItems = [...pairs.map(p => p.right)].sort(() => Math.random() - 0.5);

  const matchArea = document.createElement('div');
  matchArea.className = 'match-area';

  const leftCol = document.createElement('div');
  leftCol.className = 'match-col';
  const rightCol = document.createElement('div');
  rightCol.className = 'match-col';

  let selectedLeft = null;
  let matched = 0;
  let mistakes = 0;

  leftItems.forEach((item, i) => {
    const btn = document.createElement('button');
    btn.className = 'match-item match-left';
    btn.textContent = item;
    btn.dataset.index = i;
    btn.addEventListener('click', () => {
      leftCol.querySelectorAll('.match-item').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedLeft = i;
    });
    leftCol.appendChild(btn);
  });

  rightItems.forEach((item) => {
    const btn = document.createElement('button');
    btn.className = 'match-item match-right';
    btn.textContent = item;
    btn.addEventListener('click', () => {
      if (selectedLeft === null) return;
      const correctRight = pairs[selectedLeft].right;
      if (item === correctRight) {
        btn.classList.add('matched');
        leftCol.children[selectedLeft].classList.add('matched');
        btn.disabled = true;
        leftCol.children[selectedLeft].disabled = true;
        matched++;
        if (matched === pairs.length) onAnswer(mistakes === 0);
      } else {
        btn.classList.add('wrong-flash');
        mistakes++;
        setTimeout(() => btn.classList.remove('wrong-flash'), 500);
      }
      selectedLeft = null;
      leftCol.querySelectorAll('.match-item').forEach(b => b.classList.remove('selected'));
    });
    rightCol.appendChild(btn);
  });

  matchArea.appendChild(leftCol);
  matchArea.appendChild(rightCol);
  container.appendChild(matchArea);
}

/** Fill in the Blank */
function renderFillBlank(container, exercise, onAnswer) {
  // exercise.answer: string (correct answer)
  const form = document.createElement('div');
  form.className = 'fill-blank-form';

  const input = document.createElement('input');
  input.type = 'text';
  input.className = 'fill-blank-input';
  input.placeholder = 'Type your answer...';
  input.setAttribute('autocomplete', 'off');

  const btn = document.createElement('button');
  btn.className = 'btn btn-primary';
  btn.textContent = 'Check';
  btn.addEventListener('click', () => {
    const userAnswer = sanitizeAnswer(input.value);
    const correct = userAnswer.toLowerCase() === exercise.answer.toLowerCase();
    input.classList.add(correct ? 'correct' : 'wrong');
    input.disabled = true;
    btn.disabled = true;
    if (!correct) {
      const reveal = document.createElement('p');
      reveal.className = 'correct-answer';
      reveal.textContent = `Correct answer: ${exercise.answer}`;
      form.appendChild(reveal);
    }
    onAnswer(correct);
  });

  // Allow Enter key to submit
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') btn.click();
  });

  form.appendChild(input);
  form.appendChild(btn);
  container.appendChild(form);
}

/** Ordering — drag to reorder steps */
function renderOrdering(container, exercise, onAnswer) {
  // exercise.correctOrder: string[] (correct sequence)
  // exercise.shuffled: string[] (randomized)
  const list = document.createElement('div');
  list.className = 'ordering-list';

  const items = [...exercise.shuffled];

  function renderList() {
    list.innerHTML = '';
    items.forEach((item, i) => {
      const row = document.createElement('div');
      row.className = 'ordering-item';
      row.draggable = true;
      row.dataset.index = i;

      const num = document.createElement('span');
      num.className = 'ordering-num';
      num.textContent = i + 1;

      const text = document.createElement('span');
      text.textContent = item;

      const arrows = document.createElement('div');
      arrows.className = 'ordering-arrows';

      const upBtn = document.createElement('button');
      upBtn.textContent = '\u25B2';
      upBtn.className = 'arrow-btn';
      upBtn.disabled = i === 0;
      upBtn.addEventListener('click', () => { [items[i], items[i-1]] = [items[i-1], items[i]]; renderList(); });

      const downBtn = document.createElement('button');
      downBtn.textContent = '\u25BC';
      downBtn.className = 'arrow-btn';
      downBtn.disabled = i === items.length - 1;
      downBtn.addEventListener('click', () => { [items[i], items[i+1]] = [items[i+1], items[i]]; renderList(); });

      arrows.appendChild(upBtn);
      arrows.appendChild(downBtn);

      row.appendChild(num);
      row.appendChild(text);
      row.appendChild(arrows);
      list.appendChild(row);
    });
  }

  renderList();

  const btn = document.createElement('button');
  btn.className = 'btn btn-primary';
  btn.textContent = 'Check Order';
  btn.addEventListener('click', () => {
    const correct = items.every((item, i) => item === exercise.correctOrder[i]);
    list.querySelectorAll('.ordering-item').forEach((el, i) => {
      el.classList.add(items[i] === exercise.correctOrder[i] ? 'correct' : 'wrong');
    });
    btn.disabled = true;
    list.querySelectorAll('.arrow-btn').forEach(b => b.disabled = true);
    onAnswer(correct);
  });

  container.appendChild(list);
  container.appendChild(btn);
}

/** True or False */
function renderTrueFalse(container, exercise, onAnswer) {
  // exercise.correctAnswer: boolean
  const btns = document.createElement('div');
  btns.className = 'tf-buttons';

  [true, false].forEach(val => {
    const btn = document.createElement('button');
    btn.className = 'tf-btn';
    btn.textContent = val ? 'True' : 'False';
    btn.addEventListener('click', () => {
      btns.querySelectorAll('.tf-btn').forEach(b => b.disabled = true);
      const correct = val === exercise.correctAnswer;
      btn.classList.add(correct ? 'correct' : 'wrong');
      if (!correct) {
        btns.querySelector(`.tf-btn:${exercise.correctAnswer ? 'first' : 'last'}-child`).classList.add('correct');
      }
      onAnswer(correct);
    });
    btns.appendChild(btn);
  });

  container.appendChild(btns);
}

/** Visual Interactive — placeholder for custom per-lesson visuals */
function renderVisual(container, exercise, onAnswer) {
  // exercise.visualType: string, exercise-specific rendering
  // For now, render as a guided multiple-choice with an image/diagram
  const visual = document.createElement('div');
  visual.className = 'visual-exercise';

  if (exercise.imageHTML) {
    const imgArea = document.createElement('div');
    imgArea.className = 'visual-diagram';
    imgArea.innerHTML = exercise.imageHTML; // Pre-sanitized content from lesson data
    visual.appendChild(imgArea);
  }

  // Fall back to multiple choice for the answer
  renderMultipleChoice(visual, exercise, onAnswer);
  container.appendChild(visual);
}

/**
 * Run a full exercise set and return the score.
 * @param {HTMLElement} container - element to render exercises into
 * @param {object[]} exercises - array of exercise data objects
 * @param {function} onEachAnswer - callback(exerciseIndex, isCorrect) per answer
 * @returns {Promise<number>} score as percentage 0-100
 */
export function runExerciseSet(container, exercises, onEachAnswer) {
  return new Promise((resolve) => {
    let current = 0;
    let correctCount = 0;

    function showNext() {
      if (current >= exercises.length) {
        const score = Math.round((correctCount / exercises.length) * 100);
        resolve(score);
        return;
      }

      const progressText = document.createElement('div');
      progressText.className = 'exercise-progress';
      progressText.textContent = `Question ${current + 1} of ${exercises.length}`;

      container.innerHTML = '';
      container.appendChild(progressText);

      const exerciseArea = document.createElement('div');
      container.appendChild(exerciseArea);

      renderExercise(exerciseArea, exercises[current], (isCorrect) => {
        if (isCorrect) correctCount++;
        if (onEachAnswer) onEachAnswer(current, isCorrect);

        // Show next button after answering
        const nextBtn = document.createElement('button');
        nextBtn.className = 'btn btn-primary exercise-next-btn';
        nextBtn.textContent = current < exercises.length - 1 ? 'Next' : 'Finish';
        nextBtn.addEventListener('click', () => {
          current++;
          showNext();
        });
        container.appendChild(nextBtn);
      });
    }

    showNext();
  });
}
```

- [ ] **Step 2: Create exercises.css**

```css
/* css/exercises.css */

.exercise-container {
  max-width: 700px;
  margin: 2rem auto;
}

.exercise-progress {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 1rem;
}

.exercise-question {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.exercise-next-btn {
  margin-top: 1.5rem;
  width: 100%;
}

/* Multiple Choice */
.mc-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}

.mc-option {
  padding: 1rem;
  background: var(--bg-white);
  border: 2px solid var(--border);
  border-radius: var(--radius);
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  color: var(--text);
}

.mc-option:hover:not(:disabled) {
  border-color: var(--primary);
  background: var(--primary-glow);
}

.mc-option.correct {
  border-color: var(--science-green);
  background: var(--science-green-bg);
  color: #166534;
}

.mc-option.wrong {
  border-color: var(--data-red);
  background: var(--data-red-bg);
  color: #991b1b;
}

/* Matching */
.match-area {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.match-col {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.match-item {
  padding: 0.75rem 1rem;
  background: var(--bg-white);
  border: 2px solid var(--border);
  border-radius: var(--radius);
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: var(--text);
}

.match-item.selected {
  border-color: var(--primary);
  background: var(--primary-glow);
}

.match-item.matched {
  border-color: var(--science-green);
  background: var(--science-green-bg);
  opacity: 0.7;
}

.match-item.wrong-flash {
  border-color: var(--data-red);
  background: var(--data-red-bg);
  animation: shake 0.3s ease;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

/* Fill in Blank */
.fill-blank-form {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.fill-blank-input {
  flex: 1;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 2px solid var(--border);
  border-radius: var(--radius);
  font-family: 'JetBrains Mono', monospace;
  background: var(--bg-white);
  color: var(--text);
  outline: none;
  transition: border-color 0.2s;
}

.fill-blank-input:focus { border-color: var(--primary); }
.fill-blank-input.correct { border-color: var(--science-green); background: var(--science-green-bg); }
.fill-blank-input.wrong { border-color: var(--data-red); background: var(--data-red-bg); }

.correct-answer {
  margin-top: 0.75rem;
  font-size: 0.9rem;
  color: var(--science-green);
  font-weight: 600;
}

/* Ordering */
.ordering-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.ordering-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 1rem;
  background: var(--bg-white);
  border: 2px solid var(--border);
  border-radius: var(--radius);
  transition: all 0.2s;
}

.ordering-item.correct { border-color: var(--science-green); background: var(--science-green-bg); }
.ordering-item.wrong { border-color: var(--data-red); background: var(--data-red-bg); }

.ordering-num {
  font-weight: 700;
  color: var(--text-muted);
  min-width: 1.5rem;
}

.ordering-arrows {
  margin-left: auto;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.arrow-btn {
  background: none;
  border: 1px solid var(--border);
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.6rem;
  padding: 2px 6px;
  color: var(--text-secondary);
}

.arrow-btn:hover:not(:disabled) { border-color: var(--primary); color: var(--primary); }
.arrow-btn:disabled { opacity: 0.3; cursor: default; }

/* True/False */
.tf-buttons {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.tf-btn {
  padding: 1.25rem;
  font-size: 1.1rem;
  font-weight: 700;
  border: 2px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-white);
  cursor: pointer;
  transition: all 0.2s ease;
  color: var(--text);
}

.tf-btn:hover:not(:disabled) { border-color: var(--primary); }
.tf-btn.correct { border-color: var(--science-green); background: var(--science-green-bg); color: #166534; }
.tf-btn.wrong { border-color: var(--data-red); background: var(--data-red-bg); color: #991b1b; }

/* Visual */
.visual-exercise { text-align: center; }
.visual-diagram {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: var(--bg-white);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}

/* Lesson completion screen */
.lesson-complete {
  text-align: center;
  padding: 3rem 2rem;
  background: var(--bg-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  max-width: 500px;
  margin: 2rem auto;
}

.lesson-complete .grade {
  font-size: 4rem;
  font-weight: 900;
  margin-bottom: 0.5rem;
}

.lesson-complete .grade-a { color: var(--science-green); }
.lesson-complete .grade-b { color: var(--primary-dark); }
.lesson-complete .grade-c { color: var(--xp-gold); }
.lesson-complete .grade-d { color: var(--logic-orange); }
.lesson-complete .grade-f { color: var(--data-red); }

.lesson-complete .stars {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.lesson-complete .xp-earned {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--xp-gold);
  margin-bottom: 1.5rem;
}

@media (max-width: 768px) {
  .mc-options { grid-template-columns: 1fr; }
  .tf-buttons { grid-template-columns: 1fr; }
  .fill-blank-form { flex-direction: column; }
  .match-area { grid-template-columns: 1fr; gap: 1rem; }
}
```

- [ ] **Step 3: Commit**

```bash
git add js/exercises.js css/exercises.css
git commit -m "feat: add exercise engine with all 6 types and responsive styles"
```

---

## Chunk 5: First Complete Course (Calculus) & Remaining Pages

### Task 13: Create Calculus course overview page

**Files:**
- Create: `course/calculus/index.html`

- [ ] **Step 1: Build course overview page**

Page includes:
- Nav bar
- Course header: "Calculus" title, blue Math badge, course description
- Lesson list showing all 4 lessons with title, description, and progress indicators (stars/grade — populated from Firestore if logged in, empty if not)
- All lessons are clickable (open access, no locks)
- Footer with copyright
- Imports: `css/global.css`, `js/auth.js`, `js/progress.js`

- [ ] **Step 2: Verify in browser**

Run: `open course/calculus/index.html`
Expected: Clean course page with 4 lesson cards

- [ ] **Step 3: Commit**

```bash
git add course/calculus/index.html
git commit -m "feat: add Calculus course overview page with lesson list"
```

---

### Task 14: Create Calculus Lesson 1 — What Are Integrals

**Files:**
- Create: `course/calculus/lesson-1.html`

- [ ] **Step 1: Build lesson page with content + exercises**

Migrate content from the existing `index.html` "What Are Integrals?" section. Add 6 exercises after the teaching content:

1. **Multiple Choice:** "What does an integral measure?" → Accumulation of quantities
2. **True/False:** "The integral symbol was introduced by Newton." → False (Leibniz)
3. **Fill in Blank:** "The function being integrated is called the ___." → integrand
4. **Matching:** Match terms: integral↔area under curve, derivative↔rate of change, dx↔with respect to x, integrand↔f(x)
5. **Ordering:** Order the parts of integral notation: integral sign, function f(x), dx
6. **Multiple Choice:** "What does dx indicate?" → Integrating with respect to x

Page structure:
- Nav bar
- Progress bar at top
- Teaching content (KaTeX rendered)
- Exercise section (rendered by exercises.js)
- Completion screen (grade, stars, XP) shown after finishing
- Character buddy appears for feedback
- Footer
- Imports: all CSS files, `js/exercises.js`, `js/characters.js`, `js/progress.js`, `js/auth.js`, `js/lighthouse.js`

- [ ] **Step 2: Verify in browser**

Run: `open course/calculus/lesson-1.html`
Expected: Teaching content displays with KaTeX, exercises work, completion screen shows grade

- [ ] **Step 3: Commit**

```bash
git add course/calculus/lesson-1.html
git commit -m "feat: add Calculus Lesson 1 — What Are Integrals with 6 exercises"
```

---

### Task 15: Create Calculus Lessons 2-4

**Files:**
- Create: `course/calculus/lesson-2.html` — Indefinite Integrals
- Create: `course/calculus/lesson-3.html` — Definite Integrals
- Create: `course/calculus/lesson-4.html` — U-Substitution

- [ ] **Step 1: Build Lesson 2 — Indefinite Integrals**

Migrate content from existing index.html. Add 6 exercises:
1. MC: What is an antiderivative?
2. Fill blank: integral of x^3 dx = ___
3. True/False: The constant C is needed because derivative of any constant is zero → True
4. Matching: functions to their antiderivatives
5. Ordering: Steps to integrate (3x^2 + 2x - 5)
6. MC: Why do we add + C?

- [ ] **Step 2: Build Lesson 3 — Definite Integrals**

Migrate content. Add 6 exercises:
1. MC: What does a definite integral compute?
2. Fill blank: integral from 1 to 3 of 2x dx = ___
3. True/False: Definite integrals always give positive area → False
4. Matching: Match concepts to descriptions (FTC, net area, etc.)
5. Ordering: Steps to evaluate a definite integral
6. MC: What does F(b) - F(a) represent?

- [ ] **Step 3: Build Lesson 4 — U-Substitution**

Migrate content. Add 6 exercises:
1. MC: U-sub is the reverse of which rule?
2. Fill blank: If u = x^2, then du = ___
3. True/False: After integrating with u, you must substitute back → True
4. Matching: Match u choices to integrals
5. Ordering: Steps of u-substitution
6. MC: integral of 2x * e^(x^2) dx = ?

- [ ] **Step 4: Verify all lessons in browser**

Run: `open course/calculus/lesson-2.html course/calculus/lesson-3.html course/calculus/lesson-4.html`
Expected: All 3 lessons display content and exercises correctly

- [ ] **Step 5: Commit**

```bash
git add course/calculus/lesson-2.html course/calculus/lesson-3.html course/calculus/lesson-4.html
git commit -m "feat: add Calculus Lessons 2-4 with exercises"
```

---

### Task 16: Create profile page

**Files:**
- Create: `profile.html`

- [ ] **Step 1: Build profile page**

Page includes:
- Nav bar
- Lighthouse visualization at top (glow based on level)
- User's chosen character avatar (large display)
- Display name
- Level title and number (e.g., "Level 3 — Glow")
- XP progress bar to next level
- Total XP count
- Daily streak count
- Grid of completed courses with grades and stars per lesson
- "Change Character" button (opens character picker modal)
- "Sign Out" button
- Redirects to login.html if not authenticated
- Footer with copyright

- [ ] **Step 2: Verify in browser**

Run: `open profile.html`
Expected: Redirects to login if not signed in. Shows profile data if signed in.

- [ ] **Step 3: Commit**

```bash
git add profile.html
git commit -m "feat: add profile page with lighthouse, XP, levels, and course grades"
```

---

### Task 17: Create Terms and Privacy pages

**Files:**
- Create: `terms.html`
- Create: `privacy.html`

- [ ] **Step 1: Create Terms of Service page**

Standard terms page with:
- Nav bar, footer with copyright
- Sections: Acceptance of Terms, User Accounts, Intellectual Property, User Conduct, Disclaimer, Contact
- Simple, clear language
- Last updated: dynamic year

- [ ] **Step 2: Create Privacy Policy page**

Standard privacy page with:
- Nav bar, footer with copyright
- Sections: Information We Collect (email, usage data), How We Use It, Firebase/Google services disclosure, Data Security, Contact
- References Firebase Auth and Firestore data storage
- Last updated: dynamic year

- [ ] **Step 3: Commit**

```bash
git add terms.html privacy.html
git commit -m "feat: add Terms of Service and Privacy Policy pages"
```

---

### Task 18: Create category icons

**Files:**
- Create: `assets/icons/math.svg` — blue calculator/sigma icon
- Create: `assets/icons/science.svg` — green atom/flask icon
- Create: `assets/icons/data.svg` — red chart/graph icon
- Create: `assets/icons/logic.svg` — orange brain/puzzle icon

- [ ] **Step 1: Create all 4 category icon SVGs**

Simple, clean geometric icons matching the category colors.

- [ ] **Step 2: Commit**

```bash
git add assets/icons/
git commit -m "feat: add category icons for math, science, data, logic"
```

---

### Task 19: Clean up old files

**Files:**
- Delete: old `index.html` (replaced by new one)
- Delete: old `game/index.html` (replaced by lesson exercises)

- [ ] **Step 1: Remove old files**

The old files have been replaced by the new Mathagram structure. The calculus content has been migrated to `course/calculus/lesson-*.html` and the quiz game is replaced by the exercise engine.

```bash
rm -rf game/
```

- [ ] **Step 2: Verify project structure**

Run: `find . -name "*.html" -o -name "*.css" -o -name "*.js" -o -name "*.svg" -o -name "*.rules" | sort`
Expected: All new Mathagram files listed, no old game/ directory

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "chore: remove old game directory, replaced by exercise engine"
```

---

### Task 20: Final integration test

- [ ] **Step 1: Open homepage and verify full flow**

Run: `open index.html`
Verify:
1. Lighthouse loading animation plays
2. Light theme with correct category colors
3. All course cards link correctly
4. Nav links work
5. Footer shows dynamic year and copyright

- [ ] **Step 2: Test Calculus course flow**

1. Click Calculus card → course overview page
2. Click Lesson 1 → teaching content shows with KaTeX
3. Complete exercises → character buddy appears with feedback
4. Completion screen shows grade, stars, XP

- [ ] **Step 3: Test login flow (requires Firebase project)**

1. Open login.html
2. Sign up with email + character selection
3. Complete a lesson → progress saved
4. Open profile.html → XP, level, lighthouse displayed

- [ ] **Step 4: Verify security headers**

Check that CSP meta tag is present in all HTML files.
Check that Firestore rules file is ready to deploy.

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: Mathagram.org Phase 1 complete — homepage, auth, calculus course, exercises, characters, XP system"
```
