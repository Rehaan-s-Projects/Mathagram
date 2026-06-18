/**
 * Mathagram.org — Exercise Engine
 * Renders and manages all 6 interactive exercise types.
 */

import { sanitizeHTML, sanitizeAnswer } from "./sanitize.js";
import { speakAsync } from "./characters.js";

/**
 * Show Brilliant-style lesson completion screen.
 * Works in Incognito — shows sign-up prompt instead of XP when not logged in.
 *
 * @param {HTMLElement} exerciseContainer - the exercises div (will be hidden)
 * @param {HTMLElement} completionDiv     - the completion div (will be shown)
 * @param {number}      score             - 0-100
 * @param {object}      options
 * @param {string}      options.courseId   - e.g. 'calculus'
 * @param {string}      options.lessonId  - e.g. 'lesson-5'
 * @param {string}      options.nextHref  - href for next lesson button
 * @param {string}      options.backHref  - href for back to course (default 'index.html')
 * @param {string}      options.basePath  - relative path to root (default '../../')
 */
export async function showLessonComplete(exerciseContainer, completionDiv, score, options = {}) {
  const { courseId, lessonId, nextHref, backHref = 'index.html', basePath = '../../', xp } = options;

  // Calculate stars (5-star system)
  let stars;
  if (score >= 95) { stars = 5; }
  else if (score >= 80) { stars = 4; }
  else if (score >= 60) { stars = 3; }
  else if (score >= 40) { stars = 2; }
  else if (score >= 20) { stars = 1; }
  else { stars = 0; }

  // Use XP from quiz if provided, otherwise calculate
  const xpEarned = xp || Math.max(25, Math.round(25 + (score / 100) * 25));
  const starStr = '\u2B50'.repeat(stars) + '\u2606'.repeat(5 - stars);
  const starLabels = ['', 'Good', 'Sweet', 'Excellent Job', 'Fantastic Job', 'Intelligent'];
  const starLabel = starLabels[stars] || '';
  const starLabelHTML = starLabel ? `<div class="star-label" style="font-size:1.1rem; font-weight:800; color:var(--color-primary); margin:-4px 0 12px;">${starLabel}!</div>` : '';

  // Always mark locally so next lesson unlocks (works in Incognito)
  if (courseId && lessonId) {
    try {
      const { markLessonLocalComplete } = await import('./learning-path.js');
      markLessonLocalComplete(courseId, lessonId);
    } catch(e) {}
  }

  // Check if user is logged in
  let isLoggedIn = false;
  try {
    const { auth } = await import('./firebase-config.js');
    isLoggedIn = !!auth.currentUser;
  } catch(e) {}

  exerciseContainer.style.display = 'none';
  completionDiv.style.display = 'block';

  if (isLoggedIn) {
    // Logged in — show full results with XP
    completionDiv.innerHTML = `
      <div class="lesson-complete">
        <h2>Lesson Complete!</h2>
        <div class="stars" style="font-size:2.5rem; letter-spacing:6px; margin:16px 0;">${starStr}</div>
        ${starLabelHTML}
        <div class="xp-earned">+${xpEarned} XP</div>
        <p class="score-text">You scored ${score}%</p>
        <p style="font-size:0.75rem; color:var(--color-text-muted); margin-bottom:16px;">Correct = 10 XP (double) | Past mistakes = 5 XP</p>
        <div class="lesson-nav">
          <a href="${sanitizeHTML(backHref)}" class="btn btn-outline">Back to Course</a>
          ${nextHref ? `<a href="${sanitizeHTML(nextHref)}" class="btn btn-primary">Next Lesson</a>` : ''}
        </div>
      </div>`;
    // Save progress
    try {
      const { saveLessonResult } = await import('./progress.js');
      await saveLessonResult(courseId, lessonId, score, xpEarned);
    } catch(e) {}
  } else {
    // Incognito / not logged in — Brilliant-style prompt
    completionDiv.innerHTML = `
      <div class="lesson-complete">
        <h2>Lesson Complete!</h2>
        <div class="stars" style="font-size:2.5rem; letter-spacing:6px; margin:16px 0;">${starStr}</div>
        ${starLabelHTML}
        <p class="score-text">You scored ${score}%</p>
        <div style="background:linear-gradient(135deg,#f0fdf4,#ecfdf5); border:1px solid #bbf7d0; border-radius:12px; padding:20px; margin:20px 0; text-align:center;">
          <p style="font-size:1rem; font-weight:700; color:#166534; margin-bottom:4px;">Sign up to save your progress!</p>
          <p style="font-size:0.85rem; color:#15803d; margin-bottom:14px;">Create a free account to earn XP, track your level, and continue where you left off.</p>
          <a href="${basePath}login.html" class="btn btn-primary" style="display:inline-block; padding:10px 28px;">Sign Up Free</a>
        </div>
        <div class="lesson-nav">
          <a href="${sanitizeHTML(backHref)}" class="btn btn-outline">Back to Course</a>
          ${nextHref ? `<a href="${sanitizeHTML(nextHref)}" class="btn btn-primary">Next Lesson</a>` : ''}
        </div>
      </div>`;
  }
}

/**
 * Show a "Past Mistakes" review card after a lesson finishes.
 * Renders below the completion screen. Each missed exercise pairs a
 * sad character (red border, ✖) showing the question with a happy
 * character (green border, ✔) showing the correct answer.
 *
 * @param {HTMLElement} exerciseContainer - the exercises div (its parent receives the review)
 * @param {object[]}    missedExercises   - exercise objects the user missed on first attempt
 * @param {object}      [options]
 * @param {string}      [options.basePath] - relative path to root (default '../../')
 */
export function showMistakesReview(exerciseContainer, missedExercises, options = {}) {
  if (!missedExercises || missedExercises.length === 0) return;
  const basePath = options.basePath || '../../';

  const wrongChars = ['diego', 'steve', 'james', 'william'];
  const rightChars = ['edam', 'rita', 'sam', 'gosia'];
  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];

  const review = el('div', 'mistakes-review');
  review.style.cssText = 'max-width:700px;margin:32px auto 0;padding:24px;background:#fff;border:1px solid var(--color-border);border-radius:16px;box-shadow:var(--shadow-md);';

  let html = '<h3 style="font-size:1.2rem;font-weight:800;margin-bottom:8px;text-align:center;">' +
             '<span style="font-size:1.4rem;">📝</span> Past Mistakes Review</h3>' +
             '<p style="font-size:0.85rem;color:var(--color-text-secondary);text-align:center;margin-bottom:20px;">' +
             'Characters Right ✔ and Wrong ✖ — review what you missed.</p>';

  missedExercises.forEach((ex) => {
    const correct = deriveCorrectAnswer(ex);
    const question = ex.question || ex.spokenText || 'Question';
    const wrongChar = pick(wrongChars);
    const rightChar = pick(rightChars);
    html +=
      '<div class="mistake-card" style="border:1px solid var(--color-border);border-radius:12px;padding:14px 16px;margin-bottom:12px;background:#f8f9fa;">' +
        '<div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:10px;">' +
          '<img src="' + basePath + 'assets/characters/' + wrongChar + '.svg" alt="" style="width:44px;height:44px;border-radius:50%;border:3px solid #ef4444;background:#fff;flex-shrink:0;" />' +
          '<div style="flex:1;min-width:0;">' +
            '<div style="font-size:0.72rem;font-weight:700;color:#ef4444;letter-spacing:0.04em;text-transform:uppercase;margin-bottom:4px;">✖ Wrong</div>' +
            '<div style="font-size:0.95rem;color:var(--color-text);line-height:1.5;">' + sanitizeHTML(question) + '</div>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;align-items:flex-start;gap:12px;">' +
          '<img src="' + basePath + 'assets/characters/' + rightChar + '.svg" alt="" style="width:44px;height:44px;border-radius:50%;border:3px solid #22c55e;background:#fff;flex-shrink:0;" />' +
          '<div style="flex:1;min-width:0;">' +
            '<div style="font-size:0.72rem;font-weight:700;color:#22c55e;letter-spacing:0.04em;text-transform:uppercase;margin-bottom:4px;">✔ Right</div>' +
            '<div style="font-size:0.95rem;color:var(--color-text);line-height:1.5;font-weight:700;">' + sanitizeHTML(correct) + '</div>' +
          '</div>' +
        '</div>' +
      '</div>';
  });

  review.innerHTML = html;
  const parent = exerciseContainer.parentNode;
  if (parent) parent.appendChild(review);
  renderMath(review);
}

function deriveCorrectAnswer(ex) {
  switch (ex.type) {
    case 'multiple-choice':
      return (ex.options && ex.options[ex.correctIndex]) || '';
    case 'fill-blank':
      return ex.answer || '';
    case 'true-false':
      return ex.correctAnswer ? 'True' : 'False';
    case 'matching':
      if (!ex.pairs) return '';
      return ex.pairs.map((p) => p.left + ' → ' + p.right).join('; ');
    case 'listening':
      if (ex.answerType === 'fill-blank') return ex.answer || '';
      if (ex.answerType === 'true-false') return ex.correctAnswer ? 'True' : 'False';
      return (ex.options && ex.options[ex.correctIndex]) || '';
    default:
      return '';
  }
}

/**
 * Speak text aloud using Web Speech API (for question read-aloud).
 * Uses a neutral voice for questions (not character-specific).
 */
function speakQuestion(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  // Strip KaTeX/math notation for cleaner speech
  const clean = text.replace(/\\\(.*?\\\)/g, 'math expression')
                     .replace(/\$\$.*?\$\$/g, 'math expression')
                     .replace(/\\displaystyle/g, '')
                     .replace(/\\[a-zA-Z]+/g, '')
                     .replace(/[{}]/g, '')
                     .replace(/\s+/g, ' ')
                     .trim();
  if (!clean) return;
  const utterance = new SpeechSynthesisUtterance(clean);
  utterance.rate = 0.95;
  utterance.pitch = 1.0;
  utterance.volume = 0.7;
  window.speechSynthesis.speak(utterance);
}

/**
 * Show Brilliant-style feedback banner after answering.
 * @param {HTMLElement} container - exercise container
 * @param {boolean} isCorrect
 * @param {string} [correctAnswer] - shown when wrong
 */
function showFeedbackBanner(container, isCorrect, correctAnswer) {
  // Remove any existing banner
  const old = container.querySelector('.feedback-banner');
  if (old) old.remove();

  const banner = el('div', `feedback-banner ${isCorrect ? 'feedback-correct' : 'feedback-wrong'}`);

  const icon = el('span', 'feedback-icon', isCorrect ? '\u2714' : '\u2718');
  const msg = el('div', 'feedback-msg');

  if (isCorrect) {
    msg.innerHTML = '<strong>Correct!</strong> Great work.';
  } else {
    msg.innerHTML = '<strong>Incorrect.</strong>' + (correctAnswer ? ' The answer is <strong>' + sanitizeHTML(correctAnswer) + '</strong>.' : ' Try to remember this for next time.');
  }

  banner.appendChild(icon);
  banner.appendChild(msg);
  container.appendChild(banner);
  renderMath(banner);
}

/* ============================================================
   Utility helpers
   ============================================================ */

/** Create an element with optional className and textContent. */
function el(tag, className, text) {
  const e = document.createElement(tag);
  if (className) e.className = className;
  if (text !== undefined) e.textContent = text;
  return e;
}

/** Create an element with innerHTML (for content that may contain math). */
function elHtml(tag, className, html) {
  const e = document.createElement(tag);
  if (className) e.className = className;
  if (html !== undefined) e.innerHTML = html;
  return e;
}

/** Render KaTeX math in a container (call after dynamic content is added). */
function renderMath(container) {
  if (typeof renderMathInElement === 'function') {
    try {
      renderMathInElement(container, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true }
        ],
        throwOnError: false
      });
    } catch(e) {}
  }
}

/* ============================================================
   Type-specific renderers
   ============================================================ */

/**
 * 1. Multiple Choice
 * exercise.options: string[], exercise.correctIndex: number
 */
function renderMultipleChoice(container, exercise, onAnswer) {
  const grid = el("div", "mc-options");
  exercise.options.forEach((option, i) => {
    const btn = elHtml("button", "mc-option", sanitizeHTML(option));
    btn.type = "button";
    // Opt-in: if this option is a lesson with a real page, add a "↗" opener.
    // It opens the lesson in a new tab without selecting the answer.
    const lessonHref = exercise.optionLinks && exercise.optionLinks[i];
    if (lessonHref) {
      const link = el("span", "mc-option-link", "↗");
      link.setAttribute("role", "link");
      link.title = "Open this lesson";
      link.addEventListener("click", (e) => {
        e.stopPropagation();
        window.open(lessonHref, "_blank", "noopener");
      });
      btn.appendChild(link);
    }
    btn.addEventListener("click", () => {
      // Disable all buttons
      grid.querySelectorAll(".mc-option").forEach((b) => {
        b.disabled = true;
      });
      const correct = i === exercise.correctIndex;
      btn.classList.add(correct ? "correct" : "wrong");
      // Always reveal the correct answer
      if (!correct) {
        grid.querySelectorAll(".mc-option")[exercise.correctIndex].classList.add(
          "correct"
        );
      }
      onAnswer(correct);
    });
    grid.appendChild(btn);
  });
  container.appendChild(grid);
}

/**
 * 2. Matching
 * exercise.pairs: [{left, right}]
 */
function renderMatching(container, exercise, onAnswer) {
  const area = el("div", "match-area");
  const leftCol = el("div", "match-col match-left");
  const rightCol = el("div", "match-col match-right");

  let selectedLeft = null;
  let mistakes = 0;
  let matched = 0;
  const total = exercise.pairs.length;

  // Shuffle right side
  const shuffledRight = [...exercise.pairs]
    .map((p) => p.right)
    .sort(() => Math.random() - 0.5);

  exercise.pairs.forEach((pair, i) => {
    const leftItem = elHtml("div", "match-item", sanitizeHTML(pair.left));
    leftItem.dataset.index = i;
    leftItem.addEventListener("click", () => {
      if (leftItem.classList.contains("matched")) return;
      // Deselect previous
      if (selectedLeft) selectedLeft.classList.remove("selected");
      selectedLeft = leftItem;
      leftItem.classList.add("selected");
    });
    leftCol.appendChild(leftItem);
  });

  shuffledRight.forEach((right) => {
    const rightItem = elHtml("div", "match-item", sanitizeHTML(right));
    rightItem.addEventListener("click", () => {
      if (!selectedLeft || rightItem.classList.contains("matched")) return;
      const leftIdx = Number(selectedLeft.dataset.index);
      const correctRight = exercise.pairs[leftIdx].right;
      if (right === correctRight) {
        selectedLeft.classList.remove("selected");
        selectedLeft.classList.add("matched");
        rightItem.classList.add("matched");
        selectedLeft = null;
        matched++;
        if (matched === total) {
          onAnswer(mistakes === 0);
        }
      } else {
        mistakes++;
        rightItem.classList.add("wrong-flash");
        setTimeout(() => rightItem.classList.remove("wrong-flash"), 600);
      }
    });
    rightCol.appendChild(rightItem);
  });

  area.appendChild(leftCol);
  area.appendChild(rightCol);
  container.appendChild(area);
}

/**
 * 3. Fill in the Blank
 * exercise.answer: string
 */
function renderFillBlank(container, exercise, onAnswer) {
  const form = el("div", "fill-blank-form");
  const input = el("input", "fill-blank-input");
  input.type = "text";
  input.placeholder = "Type your answer…";
  input.autocomplete = "off";

  const btn = el("button", "btn btn-primary fill-blank-btn", "Check");
  btn.type = "button";

  function check() {
    const raw = sanitizeAnswer(input.value);
    // Normalize "pi" → "π" so users can type either, strip spaces
    const normalize = (s) => s.trim().toLowerCase().replace(/\s+/g, '').replace(/pi/g, 'π');
    const correct =
      normalize(raw) === normalize(exercise.answer);
    input.classList.add(correct ? "correct" : "wrong");
    input.disabled = true;
    btn.disabled = true;
    if (!correct) {
      const reveal = elHtml(
        "div",
        "fill-blank-reveal",
        "Correct answer: " + sanitizeHTML(exercise.answer)
      );
      container.appendChild(reveal);
      renderMath(reveal);
    }
    onAnswer(correct);
  }

  btn.addEventListener("click", check);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      check();
    }
  });

  form.appendChild(input);
  form.appendChild(btn);
  container.appendChild(form);
}

/**
 * 4. Ordering
 * exercise.correctOrder: string[], exercise.shuffled: string[]
 */
function renderOrdering(container, exercise, onAnswer) {
  const items = [...exercise.shuffled];
  const list = el("div", "ordering-list");

  function rebuild() {
    list.innerHTML = "";
    items.forEach((text, i) => {
      const row = el("div", "ordering-item");
      const num = el("span", "ordering-num", String(i + 1));
      const label = elHtml("span", "ordering-label", sanitizeHTML(text));
      const arrows = el("span", "ordering-arrows");

      const up = el("button", "ordering-arrow", "\u25B2");
      up.type = "button";
      up.disabled = i === 0;
      up.addEventListener("click", () => {
        [items[i - 1], items[i]] = [items[i], items[i - 1]];
        rebuild();
      });

      const down = el("button", "ordering-arrow", "\u25BC");
      down.type = "button";
      down.disabled = i === items.length - 1;
      down.addEventListener("click", () => {
        [items[i], items[i + 1]] = [items[i + 1], items[i]];
        rebuild();
      });

      arrows.appendChild(up);
      arrows.appendChild(down);
      row.appendChild(num);
      row.appendChild(label);
      row.appendChild(arrows);
      list.appendChild(row);
    });
    renderMath(list);
  }

  rebuild();
  container.appendChild(list);

  const checkBtn = el("button", "btn btn-primary ordering-check-btn", "Check Order");
  checkBtn.type = "button";
  checkBtn.addEventListener("click", () => {
    checkBtn.disabled = true;
    // Disable arrows
    list.querySelectorAll(".ordering-arrow").forEach((b) => (b.disabled = true));
    let allCorrect = true;
    const rows = list.querySelectorAll(".ordering-item");
    items.forEach((text, i) => {
      const correct = text === exercise.correctOrder[i];
      rows[i].classList.add(correct ? "correct" : "wrong");
      if (!correct) allCorrect = false;
    });
    onAnswer(allCorrect);
  });
  container.appendChild(checkBtn);
}

/**
 * 5. True / False
 * exercise.correctAnswer: boolean
 */
function renderTrueFalse(container, exercise, onAnswer) {
  const wrap = el("div", "tf-buttons");

  [true, false].forEach((value) => {
    const btn = el("button", "tf-btn", value ? "True" : "False");
    btn.type = "button";
    btn.addEventListener("click", () => {
      wrap.querySelectorAll(".tf-btn").forEach((b) => (b.disabled = true));
      const correct = value === exercise.correctAnswer;
      btn.classList.add(correct ? "correct" : "wrong");
      if (!correct) {
        // Highlight the correct one
        const idx = exercise.correctAnswer ? 0 : 1;
        wrap.querySelectorAll(".tf-btn")[idx].classList.add("correct");
      }
      onAnswer(correct);
    });
    wrap.appendChild(btn);
  });

  container.appendChild(wrap);
}

/**
 * 6. Visual
 * exercise.imageHTML: string (optional pre-sanitized diagram)
 * Falls back to multiple choice for the answer portion.
 */
function renderVisual(container, exercise, onAnswer) {
  if (exercise.imageHTML) {
    const diagram = el("div", "visual-diagram");
    diagram.innerHTML = exercise.imageHTML;
    container.appendChild(diagram);
  }
  // Delegate answer to multiple choice
  renderMultipleChoice(container, exercise, onAnswer);
}

/**
 * 7. Listening (Duolingo-style)
 * Question is spoken aloud automatically — student answers without reading.
 * Just a volume button to replay, no character avatar.
 * exercise.spokenText: string (what is spoken aloud)
 * exercise.options: string[] (answer choices)
 * exercise.correctIndex: number
 * Optional: exercise.answerType: 'fill-blank' | 'true-false' (defaults to multiple-choice)
 */
function renderListening(container, exercise, onAnswer) {
  const listenArea = document.createElement('div');
  listenArea.className = 'listening-area';

  const volBtn = document.createElement('button');
  volBtn.type = 'button';
  volBtn.className = 'listening-volume-btn';
  volBtn.title = 'Tap to replay';
  volBtn.innerHTML = '<span class="volume-icon">&#128264;</span>';

  const hint = document.createElement('p');
  hint.className = 'listening-hint';
  hint.textContent = 'Listen and answer below';

  listenArea.appendChild(volBtn);
  listenArea.appendChild(hint);
  container.appendChild(listenArea);

  const spokenText = exercise.spokenText || exercise.question;

  function speakNow() {
    if (!('speechSynthesis' in window)) {
      hint.textContent = 'Speech not supported — question: ' + spokenText;
      return;
    }
    window.speechSynthesis.cancel();
    const clean = spokenText
      .replace(/\\\(.*?\\\)/g, 'math expression')
      .replace(/\$\$.*?\$\$/g, 'math expression')
      .replace(/\\displaystyle/g, '')
      .replace(/\\[a-zA-Z]+/g, '')
      .replace(/[{}]/g, '')
      .replace(/\s+/g, ' ')
      .trim();
    if (!clean) return;

    volBtn.classList.add('active');
    volBtn.querySelector('.volume-icon').innerHTML = '&#128266;';
    hint.textContent = 'Speaking...';

    const done = () => {
      volBtn.classList.remove('active');
      volBtn.querySelector('.volume-icon').innerHTML = '&#128264;';
      hint.textContent = 'Tap speaker to hear again';
    };

    // When the lesson assigns a Mathagram character to this exercise
    // (e.g. exercise.character = 'edam'), read the question aloud in that
    // character's voice via the shared character-voice engine. This is what
    // makes "Edam & Diego read each question" actually use their voices.
    if (exercise.character) {
      speakAsync(clean, exercise.character).then(done);
      return;
    }

    // Neutral fallback: listening exercises with no assigned character.
    const utterance = new SpeechSynthesisUtterance(clean);
    utterance.pitch = 1.0;
    utterance.rate = 0.85;
    utterance.volume = 1.0;

    // Get voices — handle async loading
    let voices = window.speechSynthesis.getVoices();
    if (voices.length > 0) {
      const pref = voices.find(v => v.lang.startsWith('en') && v.name.includes('Google')) ||
                   voices.find(v => v.lang.startsWith('en')) || voices[0];
      if (pref) utterance.voice = pref;
    }

    utterance.onend = done;
    utterance.onerror = (e) => {
      volBtn.classList.remove('active');
      volBtn.querySelector('.volume-icon').innerHTML = '&#128264;';
      hint.textContent = 'Tap speaker to try again';
    };

    window.speechSynthesis.speak(utterance);
  }

  // Wait for voices to load, then auto-play
  if ('speechSynthesis' in window) {
    const trySpeak = () => {
      const voices = window.speechSynthesis.getVoices();
      if (voices.length > 0) {
        setTimeout(speakNow, 300);
      } else {
        // Voices not loaded yet — wait for event
        window.speechSynthesis.addEventListener('voiceschanged', () => {
          setTimeout(speakNow, 300);
        }, { once: true });
        // Fallback — try anyway after 1s
        setTimeout(speakNow, 1000);
      }
    };
    trySpeak();
  }

  // Replay button
  volBtn.addEventListener('click', speakNow);

  // Render answer options
  const answerType = exercise.answerType || 'multiple-choice';
  if (answerType === 'fill-blank') {
    renderFillBlank(container, exercise, onAnswer);
  } else if (answerType === 'true-false') {
    renderTrueFalse(container, exercise, onAnswer);
  } else {
    renderMultipleChoice(container, exercise, onAnswer);
  }
}

/* ============================================================
   Renderer dispatch
   ============================================================ */

const renderers = {
  "multiple-choice": renderMultipleChoice,
  matching: renderMatching,
  "fill-blank": renderFillBlank,
  ordering: renderOrdering,
  "true-false": renderTrueFalse,
  visual: renderVisual,
  listening: renderListening,
};

/* ============================================================
   Public API
   ============================================================ */

/**
 * Render a single exercise into a container.
 * @param {HTMLElement} container
 * @param {object}      exercise  — must have .type and .question
 * @param {function}    onAnswer  — called with (isCorrect: boolean)
 */
export function renderExercise(container, exercise, onAnswer) {
  container.innerHTML = "";
  container.classList.add("exercise-container");

  // For listening exercises, hide the question text — student must listen
  if (exercise.type !== 'listening') {
    const question = el("div", "exercise-question");
    // questionHTML is an opt-in, trusted-HTML prompt (e.g. reading.html builds
    // it with escaped text + a safe lesson <a>). Falls back to escaped text.
    question.innerHTML = exercise.questionHTML || sanitizeHTML(exercise.question);
    container.appendChild(question);
    // Normal lessons: no auto-speech (only listening exercises speak)
  }

  const render = renderers[exercise.type];
  if (render) {
    // Wrap onAnswer to add feedback banner
    const wrappedOnAnswer = (isCorrect) => {
      let correctAnswer = null;
      if (!isCorrect) {
        if (exercise.type === 'multiple-choice' && exercise.options) {
          correctAnswer = exercise.options[exercise.correctIndex];
        } else if (exercise.type === 'fill-blank') {
          correctAnswer = exercise.answer;
        } else if (exercise.type === 'true-false') {
          correctAnswer = exercise.correctAnswer ? 'True' : 'False';
        }
      }
      showFeedbackBanner(container, isCorrect, correctAnswer);
      onAnswer(isCorrect);
    };
    render(container, exercise, wrappedOnAnswer);
  } else {
    container.appendChild(
      el("p", "exercise-error", "Unknown exercise type: " + exercise.type)
    );
  }

  // Render KaTeX math in all dynamic content
  renderMath(container);
}

/**
 * Run through an array of exercises one at a time.
 * Wrong answers get re-queued to appear again later (Duolingo-style).
 * Works in Incognito — no login needed, all state is in-memory.
 *
 * @param {HTMLElement} container
 * @param {object[]}   exercises
 * @param {function}    [onEachAnswer] — optional (isCorrect, index) callback
 * @returns {Promise<{score:number, xp:number}>} resolves with score 0-100 and XP earned
 */
export function runExerciseSet(container, exercises, onEachAnswer) {
  return new Promise((resolve) => {
    // Build a queue: all original exercises + wrong ones get re-added
    const queue = [...exercises];
    const originalTotal = exercises.length;
    let pos = 0;            // position in queue
    let correctOnFirst = 0; // correct on first attempt (for scoring)
    let answered = 0;       // how many original questions answered so far
    let xpEarned = 0;       // total XP (double for first correct, normal for retry correct)

    // Progress bar element
    function buildProgressBar() {
      const wrap = el('div', 'exercise-progress-bar-wrap');
      const barBg = el('div', 'exercise-progress-bar-bg');
      const barFill = el('div', 'exercise-progress-bar-fill');
      const pct = Math.min(100, Math.round((answered / originalTotal) * 100));
      barFill.style.width = pct + '%';
      barBg.appendChild(barFill);

      const label = el('div', 'exercise-progress-label');
      const isRetry = pos >= originalTotal;
      if (isRetry) {
        label.innerHTML = '<span style="color:#ef4444;font-weight:700;">Past Mistakes</span> — Keep going!';
      } else {
        label.textContent = 'Question ' + (answered + 1) + ' of ' + originalTotal;
      }

      wrap.appendChild(label);
      wrap.appendChild(barBg);
      return wrap;
    }

    function showExercise() {
      if (pos >= queue.length) {
        // All done — score based on first-attempt correct
        const score = Math.round((correctOnFirst / originalTotal) * 100);
        // Minimum 25 XP even if all wrong
        xpEarned = Math.max(25, xpEarned);
        resolve({ score, xp: xpEarned });
        return;
      }

      container.innerHTML = '';
      container.classList.add('exercise-container');

      const exercise = queue[pos];
      const isRetry = pos >= originalTotal;

      // Progress
      container.appendChild(buildProgressBar());

      // Retry badge
      if (isRetry) {
        const badge = el('div', 'exercise-retry-badge');
        badge.innerHTML = '&#128260; You got this wrong before — try again!';
        container.appendChild(badge);
      }

      const inner = el('div', 'exercise-inner');
      container.appendChild(inner);

      renderExercise(inner, exercise, (isCorrect) => {
        if (!isRetry) {
          answered++;
          if (isCorrect) {
            correctOnFirst++;
            xpEarned += 10; // Double XP for first-attempt correct
          } else {
            // Re-queue this exercise to appear again later
            queue.push(exercise);
          }
        } else {
          // Retry attempt
          if (isCorrect) {
            xpEarned += 5; // Normal XP for retry correct
          } else {
            // Still wrong — re-queue again
            queue.push(exercise);
          }
        }

        if (typeof onEachAnswer === 'function') {
          onEachAnswer(isCorrect, isRetry ? -1 : pos);
        }

        // Next button
        const remaining = queue.length - pos - 1;
        const nextLabel = remaining === 0 ? 'Finish' : 'Continue';
        const nextBtn = el('button', 'btn btn-primary exercise-next-btn', nextLabel);
        nextBtn.type = 'button';
        nextBtn.addEventListener('click', () => {
          pos++;
          showExercise();
        });
        container.appendChild(nextBtn);
      });
    }

    showExercise();
  });
}
