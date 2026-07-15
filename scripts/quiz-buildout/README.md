# Quiz Build-Out Campaign

Goal: every placeholder (`href:'#'`) lesson across all knowledge courses becomes a
reachable URL backed by a working multiple-choice quiz.

## Per-course recipe (proven; reference = courses/astronomy/)
1. Read `courses/<slug>/index.html` → extract `units` array (names + per-unit lesson counts),
   id prefix, progress slug, the `lessons.push({...})` loop var names.
2. Generate `courses/<slug>/quizzes.js`: `export const QUIZ_BANK = {1:[...],...}`, one key per unit,
   exactly 8 `{q,choices:[4],correct,why}` each. Correct answer real + teaching `why`;
   3 distractors Duolingo-absurd. VARY the correct index position.
3. Write `courses/<slug>/quiz.html` = copy of astronomy/quiz.html with title, back-links,
   badge emoji, and config block (TOTAL_UNITS, LESSONS_PER_UNIT, COURSE_SLUG, ID_PREFIX, UNIT_NAMES).
   If unit lesson-counts vary, use a per-unit offset so globalNum matches the index's sequential `n`.
4. Edit index: placeholder `href:'#'` → `href: 'quiz.html?unit='+<u>+'&lesson='+(<i>+1)`.
   Keep a `lessons[0].href='lesson-1.html'` override only if that file exists.
5. Verify: node-parse quizzes.js (units==N, 0 bad); grep index for quiz.html?unit; quiz.html exists.

## Deploy (per repo memory — NOT git push)
Full-clean 5-path purge then `netlify deploy --prod --dir=<abs repo path>`. Verify with curl 200s.

## Excluded from quiz treatment (games/skills — need playable engines, not quizzes)
See excluded-games.txt.

## Status: see done.txt / remaining.txt
