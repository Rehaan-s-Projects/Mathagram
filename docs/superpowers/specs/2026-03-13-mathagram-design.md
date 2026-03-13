# Mathagram.org — Design Specification

## Overview

Mathagram.org is a Duolingo-style learning platform for math and science. It transforms the existing "Rehaan — Master Integrals" static site into a full interactive learning platform with multiple courses, user accounts, XP/level progression, and 8 mascot characters.

**Tech Stack:** Static HTML/CSS/JS frontend + Firebase (Auth + Firestore)

---

## 1. Brand & Visual Identity

- **Name:** Mathagram.org
- **Logo:** Lighthouse icon — beam forms subtle "M" or shines over a math symbol
- **Loading Animation:** Lighthouse beam sweeps left-to-right across screen, then content fades in
- **Theme:** Light background
  - Background: Clean white/light gray (#f8f9fa)
  - Cards: White with subtle shadows
  - Text: Dark gray/near-black
  - Primary accent: Cyan/teal (#00e5c8)
  - XP elements: Warm gold/amber
- **Typography:** Inter font family
- **Category Colors:**
  - Math — Blue
  - Science — Green
  - Data Analysis — Red
  - Logic — Orange
  - Advanced Topics — Blue (grouped with Math)

---

## 2. Site Structure & Pages

### Homepage (/)
- Lighthouse loading animation on first visit
- Hero section with Mathagram logo + tagline
- Course catalog grid showing all categories with colored section backgrounds
- "Get Started" / "Sign In" buttons

### Course Categories

**Math (Blue):**
- Calculus (existing content, expanded)
- Algebra
- Trigonometry
- AP Statistics
- Exponential Functions
- Coordinate Transformations

**Science (Green):**
- Circuits
- Digital Circuits
- Scientific Thinking
- Kurzgesagt-style Science Puzzles
- Quantum Computing
- Gears/Mechanics

**Data Analysis (Red):**
- Exploring Data Visually
- Probability in Data
- Clustering & Classification
- Regression
- Predicting with Probability

**Logic (Orange):**
- Logical Reasoning (short course)

**Advanced Topics (Blue/Math):**
- Special Relativity
- Math History

### Course Page (/course/{course-name})
- Course overview with description
- List of all lessons (open access, no locking)
- Stars, grade, and XP shown per lesson
- Character buddy pops in with encouragement

### Lesson Page (/course/{course-name}/lesson-{n})
- Teaching content (explanations, formulas with KaTeX)
- 5-10 exercises mixing all 6 types
- Character buddy appears with feedback
- Earn XP on completion
- Grade (A-F) and stars shown on completion

### Profile Page (/profile)
- Chosen avatar character
- Total XP and level
- Lighthouse visualization that glows brighter with more XP
- Completed courses/lessons with grades

### Login/Signup Page
- Email + password via Firebase Auth

---

## 3. Characters System

8 characters serve as encouragement buddies (appear during exercises) and selectable user avatars.

| Character | Type | Encouragement Style |
|-----------|------|-------------------|
| Edam | Bear | Warm, supportive ("You got this!") |
| Steve | Fox | Clever, witty ("Sly move, that's correct!") |
| James | Buff/strong man | Motivational ("Crush it! Let's go!") |
| Diego | Researcher | Nerdy, curious ("Fascinating! Correct!") |
| Rita | Cat | Chill, cool ("Purrfect answer.") |
| Sam | Kid | Excited, energetic ("Woohoo! You nailed it!") |
| William | Old man | Wise, calm ("Well done, young scholar.") |
| Gosia | Beautiful girl | Friendly, encouraging ("Amazing work!") |

**Behavior:**
- Small character illustration pops up in bottom-right during exercises
- Different expressions: happy (correct), thinking (hint), encouraging (wrong answer)
- Users pick character on signup, can change in profile
- Art style: Simple, clean SVG illustrations (Duolingo-style simplicity)

---

## 4. Level System & XP

### XP Earning
- Complete a lesson: +10 XP
- Perfect score (no mistakes): +5 bonus XP
- Complete a full course: +50 bonus XP
- Daily streak (login + complete 1 lesson): +5 XP

### Levels (Lighthouse-themed)
| Level | XP Required | Title |
|-------|------------|-------|
| 1 | 0 | Spark |
| 2 | 50 | Beam |
| 3 | 150 | Glow |
| 4 | 300 | Flare |
| 5 | 500 | Radiance |
| 6 | 800 | Beacon |
| 7 | 1200 | Lighthouse Keeper |
| 8 | 1800 | Lighthouse Master |

The lighthouse on the profile page lights up more sections as you level up (Level 1 = base only, Level 8 = full lighthouse glowing).

### Grading (A-F per lesson)
| Score | Grade | Stars |
|-------|-------|-------|
| 95-100% | A | 3 stars |
| 90-94% | A- | 3 stars |
| 85-89% | B+ | 2 stars |
| 80-84% | B | 2 stars |
| 75-79% | B- | 2 stars |
| 70-74% | C+ | 1 star |
| 65-69% | C | 1 star |
| 60-64% | C- | 1 star |
| 50-59% | D | 0 stars (retry) |
| Below 50% | F | 0 stars (retry) |

Grade shows on lesson completion screen alongside stars and XP. Character reacts based on grade. Grades visible on course page next to each lesson.

### Stars
Each lesson awards 0-3 stars based on grade. Stars are visible on the course page.

---

## 5. Exercise Types

Each lesson has teaching content first, then 5-10 exercises mixing these types:

1. **Multiple Choice** — Pick the correct answer from 4 options
2. **Matching Pairs** — Drag/tap to connect related items (e.g., function to derivative)
3. **Fill in the Blank** — Type the missing value or term
4. **Ordering** — Arrange steps in correct sequence (e.g., solving an equation)
5. **True or False** — Quick knowledge checks
6. **Visual Interactive** — Drag points on graphs, connect circuit components, etc.

Each exercise shows instant feedback with character buddy reacting.

---

## 6. Technical Architecture

### Frontend
- Static HTML/CSS/JS (no framework)
- KaTeX for math rendering
- SVG character illustrations
- CSS animations for lighthouse loading
- Responsive design (mobile-friendly)

### Backend (Firebase)
- **Firebase Auth:** Email/password authentication
- **Firestore Database:**
  - `users/{uid}` — profile, chosen character, total XP, level, streak
  - `users/{uid}/progress/{courseId}` — per-course progress
  - `users/{uid}/progress/{courseId}/lessons/{lessonId}` — grade, stars, XP earned, completion date

### Data Flow
1. User signs up with email → Firebase Auth creates account
2. User picks avatar character → saved to Firestore user doc
3. User completes lesson → score calculated client-side → grade/stars/XP written to Firestore
4. Profile page reads Firestore to display XP, level, lighthouse state, grades

---

## 7. File Structure

```
mathagram/
  index.html              — Homepage with course catalog
  login.html              — Login/signup page
  profile.html            — User profile with XP/lighthouse
  course/
    calculus/
      index.html           — Course overview
      lesson-1.html        — Lesson with content + exercises
      lesson-2.html
      ...
    algebra/
      index.html
      ...
    (other courses...)
  css/
    global.css             — Shared styles, light theme
    exercises.css          — Exercise component styles
  js/
    firebase-config.js     — Firebase initialization
    auth.js                — Login/signup/logout logic
    progress.js            — XP, levels, grades, Firestore read/write
    exercises.js           — Exercise engine (all 6 types)
    characters.js          — Character buddy display + messages
    lighthouse.js          — Lighthouse animations (loading + profile)
  assets/
    characters/            — SVG files for all 8 characters
    lighthouse/            — Lighthouse SVG/animation assets
    icons/                 — Category icons
```

---

## 8. Security

- **Firebase Security Rules:** Firestore rules ensure users can only read/write their own data (`users/{uid}` — only accessible by that uid)
- **Authentication:** Firebase Auth handles password hashing, session tokens, and email verification — no custom auth code
- **Input Sanitization:** All user text inputs (fill-in-blank answers, profile names) are sanitized before rendering to prevent XSS
- **No secrets in client code:** Firebase config is public (by design), but security rules enforce access control server-side
- **HTTPS only:** Site served over HTTPS (enforced by hosting provider)
- **Content Security Policy:** Meta tags restrict script sources to the site domain, Firebase SDK, KaTeX CDN, and Google Fonts only
- **Rate limiting:** Firebase Auth has built-in brute-force protection on login attempts

---

## 9. Copyright & Legal

- **Footer copyright:** `© 2026 Mathagram.org — All Rights Reserved. Built by Rehaan Rashid`
- Year updates dynamically via JavaScript (`new Date().getFullYear()`)
- **Terms of Service** and **Privacy Policy** pages (linked in footer)
- All course content is original — no copyrighted material from Brilliant, Duolingo, or Kurzgesagt is reproduced (inspired by, not copied)
- Character illustrations are original SVG artwork owned by Mathagram

---

## 10. Creator

Built by **Rehaan Rashid** (rashidrehaan6@gmail.com)
