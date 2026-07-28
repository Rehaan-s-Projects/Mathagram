/* ============================================================================
   lesson-engine.js — a small, data-driven Brilliant-style lesson runner.

   Usage (from a lesson page):
     import { renderLesson } from '../../js/lesson-engine.js';
     renderLesson(document.getElementById('lesson'), STEPS, {
       courseId: 'dice', lessonId: 'dice-1', backHref: 'index.html',
       title: 'What Is a Die?'
     });

   A lesson is an array of STEP objects. Supported step types:
     { type:'concept',     eyebrow, title, html, visual }      // Continue
     { type:'interactive', variant:'roll-die', eyebrow, title, html }  // Continue
     { type:'question',    eyebrow, title, html?, options:[...], answer:<idx>, explain }

   `visual` may be a die spec like 'die:6' (renders a static face) or omitted.
   Completion writes to the SAME place learning-path.js reads from
   (users/{uid}/progress/{courseId}/lessons/{lessonId}) plus sessionStorage,
   so the course path reflects it — the old field-based write did not.
   ========================================================================== */

import { markLessonLocalComplete } from './learning-path.js';

/* -- SVG die face (pip layouts 1..6) --------------------------------------- */
const PIPS = {
  1: [[50, 50]],
  2: [[30, 30], [70, 70]],
  3: [[30, 30], [50, 50], [70, 70]],
  4: [[30, 30], [70, 30], [30, 70], [70, 70]],
  5: [[30, 30], [70, 30], [50, 50], [30, 70], [70, 70]],
  6: [[30, 28], [70, 28], [30, 50], [70, 50], [30, 72], [70, 72]],
};
function dieSVG(n, cls) {
  const pips = (PIPS[n] || PIPS[1])
    .map(([x, y]) => `<circle cx="${x}" cy="${y}" r="8.4" fill="#dc2626"/>`)
    .join('');
  return `<svg class="le-die ${cls || ''}" viewBox="0 0 100 100" role="img" aria-label="Die showing ${n}">
    <rect x="4" y="4" width="92" height="92" rx="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="4" y="4" width="92" height="92" rx="20" fill="url(#leDieG)"/>
    <defs><linearGradient id="leDieG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef2f7"/>
    </linearGradient></defs>
    ${pips}
  </svg>`;
}

/* -- Polyhedral die (d4..d100): a labelled gem shape with a value ---------- */
function polygonPoints(cx, cy, r, sides, rot) {
  const rot0 = rot == null ? -Math.PI / 2 : rot;
  const pts = [];
  for (let k = 0; k < sides; k++) {
    const a = rot0 + (k * 2 * Math.PI) / sides;
    pts.push((cx + r * Math.cos(a)).toFixed(1) + ',' + (cy + r * Math.sin(a)).toFixed(1));
  }
  return pts.join(' ');
}
// Shape is decorative (varies per die for character); the dN label + value carry the meaning.
const POLY_SIDES = { 4: 3, 6: 4, 8: 6, 10: 7, 12: 5, 20: 6, 100: 12 };
function polyDie(faces, value, cls) {
  const sides = POLY_SIDES[faces] || 6;
  const pts = polygonPoints(50, 54, 40, sides);
  const gid = 'lePoly' + faces;
  return `<svg class="le-die ${cls || ''}" viewBox="0 0 100 108" role="img" aria-label="d${faces} showing ${value == null ? faces : value}">
    <defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#60a5fa"/><stop offset="1" stop-color="#2563eb"/>
    </linearGradient></defs>
    <polygon points="${pts}" fill="url(#${gid})" stroke="#1d4ed8" stroke-width="2.5" stroke-linejoin="round"/>
    <text x="50" y="58" text-anchor="middle" font-size="26" font-weight="800" fill="#fff">${value == null ? faces : value}</text>
    <text x="50" y="102" text-anchor="middle" font-size="12" font-weight="800" fill="#1d4ed8" letter-spacing="0.5">d${faces}</text>
  </svg>`;
}

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

/* -- Completion write ------------------------------------------------------ */
async function writeCompletion(courseId, lessonId) {
  markLessonLocalComplete(courseId, lessonId);          // incognito / no-login
  try {
    const { auth, db } = await import('./firebase-config.js');
    const { doc, setDoc, serverTimestamp } =
      await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const u = auth.currentUser;
    if (!u) return;
    // Subcollection doc — this is what getCompletedLessons() reads.
    await setDoc(
      doc(db, 'users', u.uid, 'progress', courseId, 'lessons', lessonId),
      { completed: true, at: serverTimestamp() },
      { merge: true }
    );
    setDoc(
      doc(db, 'users', u.uid, 'progress', courseId),
      { courseId, lastViewedAt: new Date().toISOString() },
      { merge: true }
    ).catch(() => {});
  } catch (e) { /* offline / blocked — local completion still stands */ }
}

/* -- Main ------------------------------------------------------------------ */
export function renderLesson(root, steps, opts) {
  const { courseId, lessonId, backHref = 'index.html' } = opts || {};
  const total = steps.length;
  let i = 0;
  const graded = new Array(total).fill(false); // question steps that are answered correctly

  root.innerHTML = `
    <div class="le-app">
      <header class="le-top">
        <a class="le-close" href="${esc(backHref)}" aria-label="Close lesson and return to course">&times;</a>
        <div class="le-progress"><div class="le-progress__fill" id="leFill"></div></div>
        <span class="le-count" id="leCount"></span>
      </header>
      <main class="le-stage"><div id="leStep" class="le-step"></div></main>
      <div class="le-actions"><button class="le-btn" id="leBtn" type="button"></button></div>
    </div>`;

  const stepEl = root.querySelector('#leStep');
  const fillEl = root.querySelector('#leFill');
  const countEl = root.querySelector('#leCount');
  const btn = root.querySelector('#leBtn');

  function setProgress(done) {
    fillEl.style.width = Math.round((done / total) * 100) + '%';
    countEl.textContent = Math.min(done + 1, total) + ' / ' + total;
  }

  function visualHTML(visual) {
    if (!visual) return '';
    const m = /^die:(\d)$/.exec(visual);
    if (m) return `<div class="le-visual">${dieSVG(+m[1])}<p class="le-caption">A standard six-sided die (d6)</p></div>`;
    return '';
  }

  function header(step) {
    return `${step.eyebrow ? `<p class="le-eyebrow">${esc(step.eyebrow)}</p>` : ''}
            ${step.title ? `<h1 class="le-title">${esc(step.title)}</h1>` : ''}`;
  }

  /* ---- render one step --------------------------------------------------- */
  function render() {
    setProgress(i);
    const step = steps[i];
    const isLast = i === total - 1;
    stepEl.style.animation = 'none';
    // force reflow so the entry animation replays each step
    void stepEl.offsetWidth;
    stepEl.style.animation = '';

    if (step.type === 'question') return renderQuestion(step, isLast);
    if (step.type === 'interactive') return renderInteractive(step, isLast);
    return renderConcept(step, isLast);
  }

  function primeContinueButton(isLast) {
    btn.disabled = false;
    btn.className = 'le-btn' + (isLast ? ' is-finish' : '');
    btn.textContent = isLast ? 'Complete lesson →' : 'Continue';
    btn.onclick = advance;
  }

  function renderConcept(step, isLast) {
    stepEl.innerHTML = header(step) +
      `<div class="le-prose">${step.html || ''}</div>` + visualHTML(step.visual);
    primeContinueButton(isLast);
  }

  function renderInteractive(step, isLast) {
    stepEl.innerHTML = header(step) + `<div class="le-prose">${step.html || ''}</div>`;
    if (step.variant === 'roll-die') {
      const counts = [0, 0, 0, 0, 0, 0];
      const wrap = document.createElement('div');
      wrap.className = 'le-visual';
      wrap.innerHTML = `<div id="leDieHost">${dieSVG(6)}</div>
        <button class="le-roll-btn" type="button" id="leRoll">🎲 Roll the die</button>
        <div class="le-tally" id="leTally"></div>`;
      stepEl.appendChild(wrap);
      const host = wrap.querySelector('#leDieHost');
      const tally = wrap.querySelector('#leTally');
      const rollBtn = wrap.querySelector('#leRoll');
      let rolls = 0;
      const drawTally = () => {
        tally.innerHTML = counts.map((c, k) =>
          `<div class="le-tally__cell">${k + 1}<b>${c}</b></div>`).join('');
      };
      rollBtn.addEventListener('click', () => {
        const n = 1 + Math.floor(Math.random() * 6);
        counts[n - 1]++; rolls++;
        host.innerHTML = dieSVG(n, 'is-rolling');
        drawTally();
        if (rolls === 1) primeContinueButton(isLast); // encourage at least one roll
      });
      drawTally();
    }
    if (step.variant === 'dice-roller') {
      const DICE = [4, 6, 8, 10, 12, 20, 100];
      let cur = 20, rolled = null;
      const wrap = document.createElement('div');
      wrap.className = 'le-visual';
      wrap.innerHTML = `<div class="le-chips" id="leChips"></div>
        <div id="lePolyHost">${polyDie(cur, null)}</div>
        <button class="le-roll-btn" type="button" id="leRoll">🎲 Roll the <b id="leRollLbl">d${cur}</b></button>
        <p class="le-caption" id="leRollOut">Pick a die above, then roll it.</p>`;
      stepEl.appendChild(wrap);
      const chips = wrap.querySelector('#leChips');
      const host = wrap.querySelector('#lePolyHost');
      const rollLbl = wrap.querySelector('#leRollLbl');
      const out = wrap.querySelector('#leRollOut');
      let rolls = 0;
      const drawChips = () => {
        chips.innerHTML = DICE.map(d =>
          `<button type="button" class="le-chip${d === cur ? ' is-on' : ''}" data-d="${d}">d${d}</button>`).join('');
      };
      chips.addEventListener('click', (e) => {
        const b = e.target.closest('.le-chip'); if (!b) return;
        cur = +b.dataset.d; rolled = null;
        host.innerHTML = polyDie(cur, null);
        rollLbl.textContent = 'd' + cur;
        out.textContent = `A d${cur} has ${cur} equally likely faces. Roll it!`;
        drawChips();
      });
      wrap.querySelector('#leRoll').addEventListener('click', () => {
        rolled = 1 + Math.floor(Math.random() * cur);
        rolls++;
        host.innerHTML = polyDie(cur, rolled, 'is-rolling');
        out.innerHTML = `You rolled <strong>${rolled}</strong> &mdash; one of ${cur} equally likely results (1&ndash;${cur}).`;
        if (rolls === 1) primeContinueButton(isLast);
      });
      drawChips();
    }
    // Let them continue even without rolling, but nudge via the roll handler.
    primeContinueButton(isLast);
  }

  function renderQuestion(step, isLast) {
    let selected = -1;
    let locked = graded[i]; // if returning to an already-answered step
    stepEl.innerHTML = header(step) +
      (step.html ? `<div class="le-prose">${step.html}</div>` : '') +
      `<ul class="le-options" id="leOpts"></ul><div id="leFb"></div>`;
    const list = stepEl.querySelector('#leOpts');
    const fb = stepEl.querySelector('#leFb');
    const keys = ['A', 'B', 'C', 'D', 'E', 'F'];

    step.options.forEach((opt, idx) => {
      const li = document.createElement('button');
      li.type = 'button';
      li.className = 'le-opt';
      li.style.setProperty('--oi', idx);
      li.innerHTML = `<span class="le-opt__key">${keys[idx]}</span><span>${opt}</span>`;
      li.addEventListener('click', () => {
        if (locked) return;
        selected = idx;
        list.querySelectorAll('.le-opt').forEach(o => o.classList.remove('is-selected'));
        li.classList.add('is-selected');
        btn.disabled = false;
      });
      list.appendChild(li);
    });

    function showFeedback(correct) {
      fb.innerHTML = `<div class="le-feedback ${correct ? 'is-good' : 'is-bad'}">
        <div class="le-feedback__head">${correct ? '✓ Correct' : '✗ Not quite'}</div>
        <div>${step.explain || ''}</div></div>`;
    }

    function grade() {
      const nodes = list.querySelectorAll('.le-opt');
      const correct = selected === step.answer;
      if (correct) {
        locked = true; graded[i] = true;
        nodes.forEach((o, k) => { o.disabled = true; if (k !== step.answer) o.classList.add('is-dim'); });
        nodes[step.answer].classList.remove('is-dim');
        nodes[step.answer].classList.add('is-correct');
        showFeedback(true);
        primeContinueButton(isLast);
      } else {
        // Brilliant-style: mark wrong, reveal the answer, let them move on.
        nodes[selected].classList.add('is-wrong');
        nodes[step.answer].classList.add('is-correct');
        nodes.forEach(o => { o.disabled = true; });
        locked = true; graded[i] = true;
        showFeedback(false);
        primeContinueButton(isLast);
      }
    }

    if (locked) {
      // already answered earlier — re-show the resolved state
      const nodes = list.querySelectorAll('.le-opt');
      nodes.forEach(o => o.disabled = true);
      nodes[step.answer].classList.add('is-correct');
      showFeedback(true);
      primeContinueButton(isLast);
    } else {
      btn.disabled = true;
      btn.className = 'le-btn';
      btn.textContent = 'Check';
      btn.onclick = () => { if (selected >= 0) grade(); };
    }
  }

  /* ---- navigation -------------------------------------------------------- */
  function advance() {
    if (i < total - 1) { i++; render(); window.scrollTo({ top: 0, behavior: 'smooth' }); }
    else finish();
  }

  async function finish() {
    setProgress(total);
    btn.disabled = true;
    btn.textContent = 'Saving…';
    await writeCompletion(courseId, lessonId);
    stepEl.innerHTML = `<div class="le-done">
      <div class="le-done__badge">🎉</div>
      <h1 class="le-title">Lesson complete!</h1>
      <div class="le-prose"><p>Nice work — you've unlocked the next step on your
      <strong>Dice &amp; Probability</strong> path.</p></div>
    </div>`;
    btn.disabled = false;
    btn.className = 'le-btn is-good';
    btn.textContent = 'Back to course →';
    btn.onclick = () => { window.location.href = backHref; };
  }

  render();
}
