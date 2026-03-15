/**
 * Mathagram.org — Exercise Engine
 * Renders and manages all 6 interactive exercise types.
 */

import { sanitizeHTML, sanitizeAnswer } from "./sanitize.js";

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
    const btn = el("button", "mc-option", option);
    btn.type = "button";
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
    const leftItem = el("div", "match-item", pair.left);
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
    const rightItem = el("div", "match-item", right);
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
    const correct =
      raw.toLowerCase() === exercise.answer.trim().toLowerCase();
    input.classList.add(correct ? "correct" : "wrong");
    input.disabled = true;
    btn.disabled = true;
    if (!correct) {
      const reveal = el(
        "div",
        "fill-blank-reveal",
        "Correct answer: " + exercise.answer
      );
      container.appendChild(reveal);
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
      const label = el("span", "ordering-label", text);
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

  const question = el("div", "exercise-question");
  question.innerHTML = sanitizeHTML(exercise.question);
  container.appendChild(question);

  // Read the question aloud
  speakQuestion(exercise.question);

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
}

/**
 * Run through an array of exercises one at a time.
 * @param {HTMLElement} container
 * @param {object[]}   exercises
 * @param {function}    [onEachAnswer] — optional (isCorrect, index) callback
 * @returns {Promise<number>} resolves with score 0-100
 */
export function runExerciseSet(container, exercises, onEachAnswer) {
  return new Promise((resolve) => {
    let current = 0;
    let correctCount = 0;
    const total = exercises.length;

    function showExercise() {
      container.innerHTML = "";
      container.classList.add("exercise-container");

      // Progress indicator
      const progress = el(
        "div",
        "exercise-progress",
        "Question " + (current + 1) + " of " + total
      );
      container.appendChild(progress);

      const inner = el("div", "exercise-inner");
      container.appendChild(inner);

      renderExercise(inner, exercises[current], (isCorrect) => {
        if (isCorrect) correctCount++;
        if (typeof onEachAnswer === "function") {
          onEachAnswer(isCorrect, current);
        }

        const isLast = current === total - 1;
        const nextBtn = el(
          "button",
          "btn btn-primary exercise-next-btn",
          isLast ? "Finish" : "Next"
        );
        nextBtn.type = "button";
        nextBtn.addEventListener("click", () => {
          current++;
          if (current < total) {
            showExercise();
          } else {
            const score = Math.round((correctCount / total) * 100);
            resolve(score);
          }
        });
        container.appendChild(nextBtn);
      });
    }

    showExercise();
  });
}
