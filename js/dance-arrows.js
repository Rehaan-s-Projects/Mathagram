/**
 * Dance Arrows — DDR-style arrow practice for the Dance Training course.
 *
 * Mounts into a container with id="dance-arrows" and reads two attributes:
 *   data-lesson  — the lesson number (1..2430), used to scale difficulty
 *   data-title   — the lesson title (shown above the play area)
 *
 * Controls: ArrowUp / ArrowDown / ArrowLeft / ArrowRight (also W/A/S/D).
 * Arrows scroll bottom→top; press the matching key when an arrow lands
 * inside the receptor zone at the top.
 */
(function () {
  const ROOT_ID = 'dance-arrows';

  const KEYMAP = {
    ArrowLeft: 'L',  KeyA: 'L',
    ArrowDown: 'D',  KeyS: 'D',
    ArrowUp:   'U',  KeyW: 'U',
    ArrowRight:'R',  KeyD: 'R',
  };

  // Difficulty curve: returns BPM, number of notes, and the set of allowed
  // directions for a given lesson number, normalized over the course's max.
  function difficultyFor(lessonNum, maxLesson) {
    const M = Math.max(1, maxLesson | 0);
    const N = Math.max(1, Math.min(M, lessonNum | 0));
    const t = M > 1 ? (N - 1) / (M - 1) : 0; // 0..1
    const bpm = Math.round(70 + t * 130); // 70..200
    const notes = Math.round(16 + t * 64);// 16..80
    let dirs;
    if      (t < 0.15) dirs = ['U', 'D'];                       // very easy
    else if (t < 0.30) dirs = ['U', 'D', 'L'];                  // easy
    else if (t < 0.45) dirs = ['U', 'D', 'L', 'R'];             // medium
    else if (t < 0.65) dirs = ['U', 'D', 'L', 'R'];             // medium-hard
    else               dirs = ['U', 'D', 'L', 'R'];             // hard (denser)
    // Doubles (two-arrow chords) only appear past lesson ~1100
    const doublesProb = Math.max(0, (t - 0.45)) * 0.7;
    const tier =
      t < 0.15 ? 'Beginner' :
      t < 0.30 ? 'Easy' :
      t < 0.45 ? 'Medium' :
      t < 0.65 ? 'Hard' :
      t < 0.85 ? 'Expert' : 'Challenge';
    return { N, t, bpm, notes, dirs, doublesProb, tier };
  }

  function buildChart(diff, seed) {
    // Deterministic chart based on lessonNum so each lesson has its own pattern.
    let s = (seed * 9301 + 49297) % 233280;
    const rand = () => { s = (s * 9301 + 49297) % 233280; return s / 233280; };

    const beatMs = 60000 / diff.bpm;
    const chart = [];
    let lastDir = null;
    for (let i = 0; i < diff.notes; i++) {
      const t = (i + 2) * beatMs; // 2-beat lead-in
      // Avoid immediate repeats so it feels musical
      let dir;
      do { dir = diff.dirs[Math.floor(rand() * diff.dirs.length)]; }
      while (dir === lastDir && diff.dirs.length > 1 && rand() < 0.6);
      lastDir = dir;

      const notes = [dir];
      if (rand() < diff.doublesProb) {
        // Add a second simultaneous arrow that isn't the same direction
        const others = diff.dirs.filter(d => d !== dir);
        if (others.length) notes.push(others[Math.floor(rand() * others.length)]);
      }
      chart.push({ t, notes });
    }
    return chart;
  }

  function init() {
    const root = document.getElementById(ROOT_ID);
    if (!root) return;
    const lessonNum = parseInt(root.dataset.lesson || '1', 10);
    const maxLesson = parseInt(root.dataset.maxLesson || '2430', 10);
    const lessonTitle = root.dataset.title || 'Dance Arrows Practice';
    const diff = difficultyFor(lessonNum, maxLesson);
    // data-dirs override (e.g. "LR", "UD", "UDLR") restricts which arrows
    // appear in this lesson — useful for arrow-family practice lessons.
    const dirsOverride = (root.dataset.dirs || '').toUpperCase();
    if (dirsOverride) {
      const allowed = ['U','D','L','R'].filter(d => dirsOverride.includes(d));
      if (allowed.length) {
        diff.dirs = allowed;
        // Doubles need ≥2 directions to make sense
        if (allowed.length < 2) diff.doublesProb = 0;
      }
    }
    // data-bpm overrides spawn density. data-notes overrides note count.
    const bpmOverride = parseInt(root.dataset.bpm || '0', 10);
    if (bpmOverride > 0) diff.bpm = bpmOverride;
    const notesOverride = parseInt(root.dataset.notes || '0', 10);
    if (notesOverride > 0) diff.notes = notesOverride;
    // data-travel-ms overrides how long arrows take to travel from bottom
    // to the receptor zone — bigger = more reaction time = "slower" feel.
    const travelOverride = parseInt(root.dataset.travelMs || '0', 10);
    const TRAVEL_MS_OVERRIDE = travelOverride > 0 ? travelOverride : null;
    const chart = buildChart(diff, lessonNum);

    root.innerHTML = `
      <style>
        #dance-arrows { color: #f1f5f9; }
        .da-header { text-align: center; margin-bottom: 14px; }
        .da-header h2 { font-size: 1.45rem; font-weight: 800; margin: 0 0 4px;
          background: linear-gradient(90deg, #fb7185, #c4b5fd);
          -webkit-background-clip: text; background-clip: text; color: transparent; }
        .da-header p { color: #cbd5e1; font-size: 0.9rem; margin: 2px auto; max-width: 540px; line-height: 1.5; }
        .da-meta { display: inline-flex; gap: 10px; margin-top: 8px; flex-wrap: wrap; justify-content: center; }
        .da-pill { background: rgba(139,92,246,0.18); border: 1px solid rgba(139,92,246,0.4);
          padding: 4px 12px; border-radius: 999px; font-size: 0.78rem; font-weight: 700;
          text-transform: uppercase; letter-spacing: 0.06em; color: #ddd6fe; }
        .da-stage {
          position: relative; width: 100%; max-width: 480px; height: 520px; margin: 0 auto;
          background: linear-gradient(180deg, #0f0a2c 0%, #1a0a3a 100%);
          border: 2px solid rgba(139,92,246,0.45); border-radius: 18px; overflow: hidden;
          box-shadow: 0 10px 40px rgba(139,92,246,0.18); }
        .da-lanes { position: absolute; inset: 0; display: grid; grid-template-columns: repeat(4, 1fr); }
        .da-lane { position: relative; border-right: 1px dashed rgba(255,255,255,0.06); }
        .da-lane:last-child { border-right: none; }
        .da-receptor-row { position: absolute; top: 24px; left: 0; right: 0; height: 64px;
          display: grid; grid-template-columns: repeat(4, 1fr); pointer-events: none; z-index: 5; }
        .da-receptor { display: flex; align-items: center; justify-content: center;
          font-size: 2rem; color: rgba(255,255,255,0.18); transition: color 0.08s, transform 0.08s; }
        .da-receptor.hit-perfect { color: #fde047; transform: scale(1.25); }
        .da-receptor.hit-good { color: #22c55e; transform: scale(1.18); }
        .da-receptor.hit-miss { color: #ef4444; transform: scale(0.9); }
        .da-arrow { position: absolute; left: 50%; transform: translateX(-50%);
          font-size: 2rem; line-height: 1; pointer-events: none; transition: opacity 0.15s;
          text-shadow: 0 0 14px rgba(255,255,255,0.35); }
        .da-arrow.fading { opacity: 0; }
        .da-hud { position: absolute; bottom: 8px; left: 8px; right: 8px;
          display: flex; justify-content: space-between; align-items: end; pointer-events: none; }
        .da-hud .item { background: rgba(0,0,0,0.45); padding: 6px 12px; border-radius: 10px;
          font-size: 0.8rem; font-weight: 700; color: #fff; }
        .da-hud .item .v { font-size: 1.05rem; color: #fde047; }
        .da-toast { position: absolute; left: 50%; top: 100px; transform: translateX(-50%);
          padding: 6px 16px; border-radius: 10px; font-weight: 800; font-size: 1rem;
          opacity: 0; transition: opacity 0.15s, transform 0.3s; pointer-events: none; z-index: 10; }
        .da-toast.show { opacity: 1; transform: translate(-50%, 6px); }
        .da-toast.perfect { background: #fde047; color: #1a1a1a; box-shadow: 0 0 20px #fde047; }
        .da-toast.good    { background: #22c55e; color: #fff; }
        .da-toast.miss    { background: #ef4444; color: #fff; }
        .da-controls { display: flex; gap: 8px; justify-content: center; margin-top: 14px; flex-wrap: wrap; }
        .da-btn { padding: 9px 20px; border-radius: 10px; font-weight: 800; font-size: 0.92rem;
          cursor: pointer; border: none; font-family: inherit; transition: transform 0.1s; color: #fff; }
        .da-btn:hover { transform: translateY(-1px); }
        .da-btn.primary { background: linear-gradient(90deg, #ec4899, #8b5cf6); }
        .da-btn.secondary { background: rgba(255,255,255,0.08); }
        .da-btn:disabled { opacity: 0.45; cursor: not-allowed; }
        .da-touch { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;
          max-width: 480px; margin: 12px auto 0; }
        .da-touch button { padding: 18px 0; font-size: 1.6rem; font-weight: 800;
          background: rgba(139,92,246,0.18); border: 2px solid rgba(139,92,246,0.4);
          border-radius: 14px; color: #fff; cursor: pointer; }
        .da-touch button:active { background: rgba(236,72,153,0.35); }
        .da-final { margin-top: 14px; text-align: center; color: #cbd5e1; font-size: 0.92rem; min-height: 1.4em; }
        .da-final.win { color: #fde047; font-size: 1.1rem; font-weight: 800; }
      </style>

      <div class="da-header">
        <h2>🎯 Dance Arrows — ${escapeHtml(lessonTitle)}</h2>
        <p>Press <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> (or WASD / the on-screen buttons) when each arrow lands inside the glowing zone at the top.</p>
        <div class="da-meta">
          <span class="da-pill">Lesson ${diff.N}</span>
          <span class="da-pill">${diff.tier}</span>
          <span class="da-pill">${diff.bpm} BPM</span>
          <span class="da-pill">${diff.notes} arrows</span>
        </div>
      </div>

      <div class="da-stage" id="da-stage">
        <div class="da-lanes">
          <div class="da-lane" data-dir="L"></div>
          <div class="da-lane" data-dir="D"></div>
          <div class="da-lane" data-dir="U"></div>
          <div class="da-lane" data-dir="R"></div>
        </div>
        <div class="da-receptor-row">
          <div class="da-receptor" data-dir="L">⬅</div>
          <div class="da-receptor" data-dir="D">⬇</div>
          <div class="da-receptor" data-dir="U">⬆</div>
          <div class="da-receptor" data-dir="R">➡</div>
        </div>
        <div class="da-toast" id="da-toast"></div>
        <div class="da-hud">
          <div class="item">SCORE <span class="v" id="da-score">0</span></div>
          <div class="item">COMBO <span class="v" id="da-combo">0</span></div>
          <div class="item">ACC <span class="v" id="da-acc">—</span></div>
        </div>
      </div>

      <div class="da-controls">
        <button class="da-btn primary" id="da-start">▶ Start Practice</button>
        <button class="da-btn secondary" id="da-reset">↻ Reset</button>
      </div>

      <div class="da-touch" aria-label="Touch controls">
        <button data-touch="L">⬅</button>
        <button data-touch="D">⬇</button>
        <button data-touch="U">⬆</button>
        <button data-touch="R">➡</button>
      </div>

      <div class="da-final" id="da-final">Press <strong>Start Practice</strong> when you're ready.</div>
    `;

    const stage = root.querySelector('#da-stage');
    const lanes = {};
    root.querySelectorAll('.da-lane').forEach(el => { lanes[el.dataset.dir] = el; });
    const receptors = {};
    root.querySelectorAll('.da-receptor').forEach(el => { receptors[el.dataset.dir] = el; });
    const elScore = root.querySelector('#da-score');
    const elCombo = root.querySelector('#da-combo');
    const elAcc   = root.querySelector('#da-acc');
    const elToast = root.querySelector('#da-toast');
    const elFinal = root.querySelector('#da-final');
    const btnStart = root.querySelector('#da-start');
    const btnReset = root.querySelector('#da-reset');

    const ARROW_GLYPH = { U: '⬆', D: '⬇', L: '⬅', R: '➡' };
    const TRAVEL_MS = TRAVEL_MS_OVERRIDE || 1500; // time an arrow takes to travel from bottom to receptor
    const RECEPTOR_TOP = 24 + 32; // receptor zone center (top + half height)
    const STAGE_HEIGHT = 520;

    let playing = false;
    let startedAt = 0;
    let scheduled = []; // arrow DOM elements with target time + dir + state
    let chartIdx = 0;
    let score = 0, combo = 0, hits = 0, attempts = 0, finishedAt = null;
    let rafHandle = null;

    function reset() {
      stop();
      stage.querySelectorAll('.da-arrow').forEach(a => a.remove());
      scheduled = [];
      chartIdx = 0;
      score = 0; combo = 0; hits = 0; attempts = 0; finishedAt = null;
      elScore.textContent = '0';
      elCombo.textContent = '0';
      elAcc.textContent = '—';
      elFinal.textContent = `Press Start Practice when you're ready.`;
      elFinal.classList.remove('win');
      btnStart.disabled = false;
      btnStart.textContent = '▶ Start Practice';
    }

    function start() {
      if (playing) { stop(); return; }
      reset();
      playing = true;
      startedAt = performance.now();
      btnStart.textContent = '⏸ Stop';
      elFinal.textContent = 'Hit the arrows as they cross the glowing zone!';
      tick();
    }

    function stop() {
      playing = false;
      if (rafHandle) cancelAnimationFrame(rafHandle);
      rafHandle = null;
      btnStart.textContent = '▶ Start Practice';
    }

    function spawnArrow(dir, hitTime) {
      const a = document.createElement('div');
      a.className = 'da-arrow';
      a.textContent = ARROW_GLYPH[dir];
      a.style.top = STAGE_HEIGHT + 'px';
      lanes[dir].appendChild(a);
      scheduled.push({ el: a, dir, hitTime, hit: false });
    }

    function tick() {
      if (!playing) return;
      const now = performance.now() - startedAt;

      // Spawn arrows TRAVEL_MS before their hitTime
      while (chartIdx < chart.length && chart[chartIdx].t <= now + TRAVEL_MS) {
        const beat = chart[chartIdx];
        beat.notes.forEach(d => spawnArrow(d, chart[chartIdx].t));
        chartIdx++;
      }

      // Move arrows
      const ARROW_HEIGHT = 32;
      scheduled.forEach(s => {
        if (s.hit) return;
        const remaining = s.hitTime - now; // ms until receptor
        // Position interpolates from STAGE_HEIGHT (bottom) to RECEPTOR_TOP (target)
        const progress = 1 - (remaining / TRAVEL_MS);
        const y = STAGE_HEIGHT - progress * (STAGE_HEIGHT - RECEPTOR_TOP);
        s.el.style.top = y + 'px';
        // Auto-miss when arrow passes receptor by >120ms
        if (remaining < -120) {
          markResult(s, 'miss', null);
        }
      });

      rafHandle = requestAnimationFrame(tick);

      // End condition: all arrows resolved + scheduling done
      if (chartIdx >= chart.length && scheduled.every(s => s.hit)) {
        finish();
      }
    }

    function markResult(s, kind, recDir) {
      if (s.hit) return;
      s.hit = true;
      attempts++;
      let pts = 0;
      if (kind === 'perfect') { pts = 100; hits++; combo++; }
      else if (kind === 'good') { pts = 60; hits++; combo++; }
      else { pts = 0; combo = 0; }
      score += pts + (combo >= 8 ? 20 : 0);
      elScore.textContent = score;
      elCombo.textContent = combo;
      elAcc.textContent = Math.round((hits / attempts) * 100) + '%';

      // Visual feedback on the receptor
      const target = receptors[recDir || s.dir];
      if (target) {
        target.classList.remove('hit-perfect','hit-good','hit-miss');
        target.classList.add('hit-' + kind);
        setTimeout(() => target.classList.remove('hit-' + kind), 140);
      }
      // Toast
      elToast.className = 'da-toast show ' + kind;
      elToast.textContent = kind === 'perfect' ? 'PERFECT' : kind === 'good' ? 'GOOD' : 'MISS';
      setTimeout(() => elToast.classList.remove('show'), 350);

      // Fade arrow
      s.el.classList.add('fading');
      setTimeout(() => s.el.remove(), 200);
    }

    function pressDir(dir) {
      if (!playing) return;
      const now = performance.now() - startedAt;
      // Find the closest unhit arrow in this lane within ±200ms
      let best = null, bestAbs = Infinity;
      scheduled.forEach(s => {
        if (s.hit || s.dir !== dir) return;
        const delta = Math.abs(now - s.hitTime);
        if (delta < bestAbs && delta <= 200) { best = s; bestAbs = delta; }
      });
      // Also pulse the receptor briefly even if no hit, for feedback
      const r = receptors[dir];
      if (r) {
        r.style.color = '#fff';
        setTimeout(() => { r.style.color = ''; }, 80);
      }
      if (!best) return; // ignored "ghost tap"
      const kind = bestAbs <= 70 ? 'perfect' : bestAbs <= 130 ? 'good' : 'miss';
      markResult(best, kind, dir);
    }

    function finish() {
      stop();
      const max = chart.reduce((a, c) => a + c.notes.length, 0) * 100;
      const pct = max ? Math.round((score / max) * 100) : 0;
      const grade = pct >= 95 ? 'AAA' : pct >= 85 ? 'AA' : pct >= 70 ? 'A' : pct >= 55 ? 'B' : pct >= 40 ? 'C' : 'D';
      elFinal.textContent = `Done! Score ${score} / ${max} • ${pct}% • Grade ${grade} • Combo high ${combo}`;
      elFinal.classList.add('win');
      btnStart.textContent = '▶ Start Practice';
      btnStart.disabled = false;
    }

    document.addEventListener('keydown', (e) => {
      const d = KEYMAP[e.code];
      if (!d) return;
      e.preventDefault();
      pressDir(d);
    });
    root.querySelectorAll('.da-touch button').forEach(b => {
      b.addEventListener('click', () => pressDir(b.dataset.touch));
    });
    btnStart.addEventListener('click', () => start());
    btnReset.addEventListener('click', reset);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
