// js/learning-path.js
// Renders Duolingo-style learning paths with side-by-side nodes,
// practice sessions, and reading skill nodes.

// Firebase imports moved into getCompletedLessons() so renderPath works even if Firebase fails

let currentLessons = [];

/**
 * Render a learning path into a container.
 * Lessons are displayed in zigzag rows of 3 with practice & reading nodes.
 */
export function renderPath(container, lessons, completedIds = new Set()) {
  currentLessons = lessons;
  container.innerHTML = '';

  // Progress bar
  const completedCount = lessons.filter(l => completedIds.has(l.id)).length;
  const totalCount = lessons.length;
  const pct = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0;

  const progress = document.createElement('div');
  progress.className = 'path-progress';
  progress.innerHTML = `
    <div class="path-progress-bar"><div class="path-progress-fill" style="width:${pct}%"></div></div>
    <span class="path-progress-text">${completedCount}/${totalCount}</span>
  `;
  container.appendChild(progress);

  // Inject practice & reading nodes into the lesson list
  const enriched = injectSkillNodes(lessons);

  let currentUnit = null;
  let foundCurrent = false;
  let prevRealLessonState = null;
  let lessonNumInUnit = 0;
  let rowBuffer = [];
  let rowIndex = 0;

  enriched.forEach((lesson, i) => {
    // Unit header
    if (lesson.unit !== currentUnit && lesson.type !== 'practice' && lesson.type !== 'reading') {
      // Flush any remaining row
      if (rowBuffer.length > 0) {
        flushRow(container, rowBuffer, rowIndex++);
        rowBuffer = [];
      }
      currentUnit = lesson.unit;
      lessonNumInUnit = 0;
      const categoryLabels = { math: 'Math', science: 'Science', data: 'Data Analysis', logic: 'Logic', language: 'Language', others: 'Others' };
      const categoryLabel = categoryLabels[lesson.category] || lesson.category || '';
      const header = document.createElement('div');
      header.className = 'path-unit-header';
      header.innerHTML = `
        <span class="path-unit-badge ${lesson.category || ''}">${categoryLabel}</span>
        <div class="path-unit-name">Unit ${lesson.unit}: ${lesson.unitName || ''}</div>
      `;
      container.appendChild(header);
    }

    let state;
    if (lesson.type === 'practice' || lesson.type === 'reading') {
      // Optional side activity — unlocked only if the preceding real lesson is completed.
      // Never consumes the "current" slot, so the next real lesson remains reachable in order.
      state = prevRealLessonState === 'completed' ? 'current' : 'locked';
    } else {
      // Determine state — check by lesson id, href filename, or lesson-N pattern
      const hrefName = lesson.href && lesson.href !== '#' ? lesson.href.replace('.html','') : '';
      const isCompleted = completedIds.has(lesson.id) || (hrefName && completedIds.has(hrefName));
      let isCurrent = false;
      let isLocked = false;

      if (!isCompleted && !foundCurrent) {
        isCurrent = true;
        foundCurrent = true;
      } else if (!isCompleted) {
        isLocked = true;
      }

      state = isCompleted ? 'completed' : isCurrent ? 'current' : 'locked';
      prevRealLessonState = state;
      lessonNumInUnit++;
    }

    const displayIndex = (lesson.type === 'practice' || lesson.type === 'reading')
      ? i
      : lessonNumInUnit - 1;
    rowBuffer.push({ ...lesson, state, index: displayIndex });

    // Flush row when we have 3 nodes
    if (rowBuffer.length >= 3) {
      flushRow(container, rowBuffer, rowIndex++);
      rowBuffer = [];
    }
  });

  // Flush remaining
  if (rowBuffer.length > 0) {
    flushRow(container, rowBuffer, rowIndex++);
  }
}

/**
 * Flush a row of 1-3 nodes into the container.
 */
function flushRow(container, nodes, rowIndex) {
  // Add connector
  if (rowIndex > 0) {
    const connector = document.createElement('div');
    connector.className = 'path-connector';
    const firstState = nodes[0]?.state || 'locked';
    if (firstState === 'completed') connector.classList.add('completed');
    else if (firstState === 'current') connector.classList.add('current');
    container.appendChild(connector);
  }

  const row = document.createElement('div');
  row.className = 'path-row';

  nodes.forEach(n => {
    const nodeEl = document.createElement('div');
    nodeEl.className = `path-node ${n.state}`;

    const typeClass = n.type === 'practice' ? ' practice' : n.type === 'reading' ? ' reading' : '';
    const checkpointClass = n.checkpoint ? ' checkpoint' : '';
    const classes = `path-circle ${n.state}${typeClass}${checkpointClass}`;

    let icon = '';
    if (n.state === 'locked') {
      icon = n.type === 'practice' ? '🎧' : n.type === 'reading' ? '📖' : '🔒';
    } else if (n.state === 'current') {
      icon = n.type === 'practice' ? '🎧' : n.type === 'reading' ? '📖' : n.checkpoint ? '⭐' : String(n.index + 1);
    } else {
      icon = ''; // completed — CSS ::after handles it
    }

    if (n.state === 'locked') {
      nodeEl.innerHTML = `
        <div class="${classes}">${icon}</div>
        <span class="path-label">${n.title}</span>
      `;
    } else {
      const href = (n.href && n.href !== '#') ? n.href : '#';
      nodeEl.innerHTML = `
        <a href="${href}" class="${classes}">${icon}</a>
        <span class="path-label">${n.title}</span>
        ${n.state === 'completed' ? '<span class="path-stars">⭐⭐⭐⭐⭐</span>' : ''}
      `;

      if (n.type === 'practice') {
        const link = nodeEl.querySelector('a');
        link.addEventListener('click', (e) => {
          e.preventDefault();
          openListeningPractice(n);
        });
      }
    }

    row.appendChild(nodeEl);
  });

  container.appendChild(row);
}

/**
 * Inject practice and reading nodes after every 4-5 lessons.
 * Practice appears after every 4th lesson, reading after every 8th.
 */
function injectSkillNodes(lessons) {
  const result = [];
  let lessonCount = 0;

  lessons.forEach((lesson, i) => {
    result.push(lesson);
    lessonCount++;

    // Add practice node after every 4th lesson
    if (lessonCount % 4 === 0 && i < lessons.length - 1) {
      result.push({
        id: `practice-${lessonCount}`,
        title: 'Listening Practice',
        href: '#',
        unit: lesson.unit,
        unitName: lesson.unitName,
        category: lesson.category,
        type: 'practice'
      });
    }

    // Add reading node after every 8th lesson
    if (lessonCount % 8 === 0 && i < lessons.length - 1) {
      result.push({
        id: `reading-${lessonCount}`,
        title: 'Reading',
        href: '#',
        unit: lesson.unit,
        unitName: lesson.unitName,
        category: lesson.category,
        type: 'reading'
      });
    }
  });

  return result;
}

/**
 * Get completed lesson IDs for a user from Firestore + local session.
 * Merges Firebase progress (logged in) with sessionStorage (Incognito).
 */
export async function getCompletedLessons(courseId) {
  const ids = new Set();

  // Always check local session completions (works in Incognito)
  try {
    const local = JSON.parse(sessionStorage.getItem('mathagram_completed_' + courseId) || '[]');
    local.forEach(id => ids.add(id));
  } catch(e) {}

  // Also check Firebase if logged in
  try {
    const { auth } = await import('./firebase-config.js');
    const { db } = await import('./firebase-config.js');
    const { collection, getDocs } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const user = auth.currentUser;
    if (user) {
      const snap = await getDocs(collection(db, 'users', user.uid, 'progress', courseId, 'lessons'));
      snap.forEach(doc => ids.add(doc.id));
    }
  } catch (e) {}

  return ids;
}

/**
 * Open a listening-practice modal for a given practice node.
 * Picks up to 4 lessons from the same unit as answer options, speaks one,
 * and asks the student to identify which was spoken.
 */
async function openListeningPractice(practiceNode) {
  const pool = currentLessons.filter(l => l.unit === practiceNode.unit && !l.type);
  if (pool.length < 2) return;

  const shuffled = pool.slice().sort(() => Math.random() - 0.5);
  const options = shuffled.slice(0, Math.min(4, shuffled.length)).map(l => l.title);
  const correctIndex = Math.floor(Math.random() * options.length);
  const spokenText = options[correctIndex];

  const overlay = document.createElement('div');
  overlay.className = 'practice-modal-overlay';
  overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.6);display:flex;align-items:center;justify-content:center;z-index:9999;padding:16px;';

  const modal = document.createElement('div');
  modal.className = 'practice-modal';
  modal.style.cssText = 'background:var(--color-surface,#fff);color:var(--color-text,#111);border-radius:16px;max-width:560px;width:100%;max-height:90vh;overflow-y:auto;padding:24px;position:relative;';

  const closeBtn = document.createElement('button');
  closeBtn.type = 'button';
  closeBtn.innerHTML = '&times;';
  closeBtn.setAttribute('aria-label', 'Close');
  closeBtn.style.cssText = 'position:absolute;top:12px;right:12px;background:transparent;border:none;font-size:1.8rem;cursor:pointer;color:inherit;line-height:1;';
  closeBtn.addEventListener('click', () => closeModal());

  const title = document.createElement('h2');
  title.textContent = 'Listening Practice';
  title.style.cssText = 'margin:0 0 4px;font-size:1.4rem;';

  const subtitle = document.createElement('p');
  subtitle.textContent = `Unit ${practiceNode.unit}: ${practiceNode.unitName || ''}`;
  subtitle.style.cssText = 'margin:0 0 20px;color:var(--color-text-secondary,#666);font-size:0.9rem;';

  const exerciseContainer = document.createElement('div');

  modal.appendChild(closeBtn);
  modal.appendChild(title);
  modal.appendChild(subtitle);
  modal.appendChild(exerciseContainer);
  overlay.appendChild(modal);
  document.body.appendChild(overlay);

  function closeModal() {
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    overlay.remove();
  }
  overlay.addEventListener('click', (e) => { if (e.target === overlay) closeModal(); });

  try {
    const { renderExercise } = await import('./exercises.js');
    renderExercise(exerciseContainer, {
      type: 'listening',
      question: spokenText,
      spokenText,
      options,
      correctIndex,
    }, () => { /* answer handled by exercises.js UI */ });
  } catch (err) {
    exerciseContainer.textContent = 'Could not load practice. Please try again.';
  }
}

/**
 * Mark a lesson as completed in sessionStorage (for Incognito / no-login).
 * Called from showLessonComplete in exercises.js.
 */
export function markLessonLocalComplete(courseId, lessonId) {
  try {
    const key = 'mathagram_completed_' + courseId;
    const local = JSON.parse(sessionStorage.getItem(key) || '[]');
    if (!local.includes(lessonId)) {
      local.push(lessonId);
      sessionStorage.setItem(key, JSON.stringify(local));
    }
  } catch(e) {}
}
