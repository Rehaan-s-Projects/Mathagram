# Mathagram

Free interactive learning platform for math, science, languages, and more. ~200 courses with AI voice characters, lesson-by-lesson progression, and a global leaderboard.

Live at **[mathagram.org](https://mathagram.org)**.

## Stack

Static HTML/CSS/JS — no build step. Firebase (Firestore + Auth) handles user accounts, progress, and leaderboard data. Hosted on Netlify.

## Repo layout

```
index.html              Landing page
courses.html            Course catalog
learning-post.html      Posts/feed
leaderboard.html        Global leaderboard
login.html              Auth (Firebase)
practice.html           Standalone practice mode
profile.html            User profile

course/                 ~200 course directories, each with index.html + lessons
css/                    Global + feature stylesheets
js/                     Auth, Firebase, lesson loader, progress, characters, etc.
assets/                 Images, logos, character art
learning-post/          Posts SPA (uses _redirects fallback)
docs/                   Internal docs

_redirects              Netlify redirects (course renames, SPA routing,
                        slur-trap → strike-system warnings)
_headers                Netlify response headers
firebase.json           Firestore config
firestore.rules         Firestore security rules
manifest.json           PWA manifest
sw.js                   Service worker
```

## Local development

It's a static site — open `index.html` in a browser, or serve the directory:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Firebase Auth and Firestore calls hit production from localhost.

## Deploy

> **Important:** `git push` updates GitHub but does **not** publish the site. Mathagram is deployed by uploading the working tree directly to Netlify.

```bash
netlify deploy --prod
```

GitHub and the live site are not kept in automatic sync. Always run a direct Netlify deploy after merging changes you want live.

## Course content

Each course lives in `course/<slug>/` with an `index.html` (learning path) and individual `lesson-N.html` files. Course renames are handled via `_redirects` (e.g. `/course/difficult-colors` → `/course/colour`) so old links keep working.
