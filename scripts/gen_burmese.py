#!/usr/bin/env python3
"""Generate Burmese course lesson HTML files.

Each per-unit Python file (scripts/burmese_units/unit_NN.py) imports
`render_unit` from this module and calls it with the unit's data.
"""
import json
import os
import sys
import textwrap

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
COURSE_DIR = os.path.join(REPO_ROOT, "course", "burmese")

TOTAL_LESSONS = 810

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc} — Mathagram</title>
  <link rel="icon" href="../../assets/lighthouse/logo.svg">
  <link rel="stylesheet" href="../../css/global.css">
  <link rel="stylesheet" href="../../css/exercises.css">
  <link rel="stylesheet" href="../../css/characters.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <style>
    .lesson-content {{ max-width: 700px; margin: 0 auto; padding: 48px 24px 32px; }}
    .lesson-content .chapter-label {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-primary); margin-bottom: 8px; }}
    .lesson-content h1 {{ font-size: 2rem; font-weight: 800; margin-bottom: 24px; }}
    .lesson-content p {{ font-size: 1.05rem; line-height: 1.75; color: var(--color-text-secondary); margin-bottom: 16px; }}
    .lesson-content .math-block {{ text-align: center; margin: 24px 0; font-size: 1.3rem; }}
    .lesson-content ul {{ margin: 12px 0 20px 20px; color: var(--color-text-secondary); line-height: 1.75; }}
    .exercise-section {{ max-width: 700px; margin: 0 auto; padding: 0 24px 48px; }}
    .exercise-section h2 {{ font-size: 1.3rem; font-weight: 700; margin-bottom: 20px; }}
    .lesson-complete {{ text-align: center; padding: 40px 24px; background: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-lg); max-width: 480px; margin: 32px auto; box-shadow: var(--shadow-md); }}
    .lesson-complete h2 {{ font-size: 1.5rem; font-weight: 800; margin-bottom: 8px; }}
    .lesson-complete .grade-display {{ font-size: 4rem; font-weight: 800; line-height: 1; margin: 16px 0; }}
    .lesson-complete .stars {{ font-size: 2rem; letter-spacing: 4px; margin-bottom: 12px; }}
    .lesson-complete .xp-earned {{ display: inline-flex; align-items: center; gap: 6px; padding: 8px 20px; font-size: 1rem; font-weight: 700; color: var(--color-xp); background: rgba(234,179,8,0.1); border-radius: var(--radius); margin-bottom: 16px; }}
    .lesson-complete .score-text {{ font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 24px; }}
    .lesson-nav {{ display: flex; gap: 12px; justify-content: center; margin-top: 16px; }}
  </style>
  <link rel="stylesheet" href="../../css/calculator.css">
</head>
<body>
  <script type="module" src="../../js/lesson-loader.js"></script>
  <script type="module" src="../../js/auth-gate.js" data-base="../../"></script>
  <nav class="nav">
    <div class="container">
      <a href="../../index.html" class="nav-logo">
        <img src="../../assets/lighthouse/logo.svg" alt="" width="32" height="32">
        <span>Mathagram</span>
      </a>
      <div class="nav-links">
        <a href="index.html">Burmese</a>
        <a href="../../learning-post.html">Posts</a>
        <a href="../../login.html" data-auth="login">Login</a>
      </div>
    </div>
  </nav>
"""

BODY = """
  <section class="lesson-content">
    <div class="chapter-label">Unit {unit_num} &mdash; {unit_name_esc}</div>
    <h1>{title_esc}</h1>
{body_html}
  </section>

  <section class="exercise-section">
    <h2>Practice Exercises</h2>
    <div id="exercises"></div>
    <div id="completion" style="display:none;"></div>
  </section>

  <footer class="footer">
    <div class="container">
      <p class="footer-copy">&copy; <span id="year"></span> Mathagram.org — All Rights Reserved.</p>
    </div>
  </footer>
"""

SCRIPT_TMPL = """
  <script type="module">
    import {{ initNav }} from '../../js/nav.js';
    import {{ initRitaChat }} from '../../js/rita-chat.js';
    initNav('../../');
    initRitaChat('../../');
    import {{ runExerciseSet, showLessonComplete }} from '../../js/exercises.js';
    import {{ showBuddy, randomCharacterId, initSideCharacter }} from '../../js/characters.js';

    (function renderMath() {{
      if (typeof renderMathInElement !== 'undefined') {{
        renderMathInElement(document.body, {{
          delimiters: [{{ left: "$$", right: "$$", display: true }}, {{ left: "\\\\(", right: "\\\\)", display: false }}],
          throwOnError: false
        }});
      }} else {{ setTimeout(renderMath, 80); }}
    }})();
    document.getElementById('year').textContent = new Date().getFullYear();
    initSideCharacter(randomCharacterId(), '../../');

    const exercises = {exercises_json};

    const container = document.getElementById('exercises');
    const completionDiv = document.getElementById('completion');
    const chars = ['diego','rita','sam','steve','william','gosia','james'];
    const {{ score, xp }} = await runExerciseSet(container, exercises, (isCorrect, index) => {{
      const c = chars[index % chars.length];
      initSideCharacter(c, '../../');
      showBuddy(c, isCorrect ? 'correct' : 'wrong');
    }});
    await showLessonComplete(container, completionDiv, score, {{ xp,
      courseId: 'burmese', lessonId: 'lesson-{lesson_num}', nextHref: '{next_href}', backHref: 'index.html'
    }});
    import {{ createCalculator }} from "../../js/calculator.js"; createCalculator();
  </script>
</body>
</html>
"""


def html_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))


def render_lesson(unit_num, unit_name, lesson_num, title, body_html, exercises):
    next_num = lesson_num + 1
    next_href = f"lesson-{next_num}.html" if next_num <= TOTAL_LESSONS else "index.html"
    head = HEAD.format(title_esc=html_escape(title))
    body = BODY.format(
        unit_num=unit_num,
        unit_name_esc=html_escape(unit_name),
        title_esc=html_escape(title),
        body_html=textwrap.indent(body_html.strip(), "    "),
    )
    script = SCRIPT_TMPL.format(
        exercises_json=json.dumps(exercises, ensure_ascii=False, indent=2),
        lesson_num=lesson_num,
        next_href=next_href,
    )
    return head + body + script


def render_unit(unit_num, unit_name, start_lesson, lessons):
    """Render all lesson HTML files for a unit and print the index snippet."""
    titles = []
    for i, lesson in enumerate(lessons):
        n = start_lesson + i
        html = render_lesson(unit_num, unit_name, n, lesson["title"],
                              lesson["body_html"], lesson["exercises"])
        out_path = os.path.join(COURSE_DIR, f"lesson-{n}.html")
        with open(out_path, "w") as fh:
            fh.write(html)
        titles.append(lesson["title"])
        print(f"  wrote lesson-{n}.html — {lesson['title']}", file=sys.stderr)
    titles_js = ",".join(json.dumps(t, ensure_ascii=False) for t in titles)
    snippet = f'      [{unit_num},{json.dumps(unit_name, ensure_ascii=False)},[{titles_js}]],'
    print(snippet)
    return snippet
