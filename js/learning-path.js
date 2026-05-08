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
  // (skip if any lesson opts out via skipSkillNodes — e.g. Typing Skills)
  const enriched = lessons.some(l => l.skipSkillNodes) ? lessons : injectSkillNodes(lessons);

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
      const categoryLabels = { math: 'Math', science: 'Science', data: 'Data Analysis', logic: 'Logic', language: 'Language', programming: 'Programming & CS', others: 'Others' };
      const categoryLabel = categoryLabels[lesson.category] || lesson.category || '';
      const header = document.createElement('div');
      header.className = 'path-unit-header';
      const unitLabel = lesson.unitLabel || 'Unit';
      header.innerHTML = `
        <span class="path-unit-badge ${lesson.category || ''}">${categoryLabel}</span>
        <div class="path-unit-name">${unitLabel} ${lesson.unit}: ${lesson.unitName || ''}</div>
      `;
      container.appendChild(header);
    }

    let state;
    if (lesson.type === 'reading' || lesson.type === 'practice') {
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
      icon = n.type === 'practice' ? '🎧' : n.type === 'reading' ? '📖' : (n.customIcon || '🔒');
    } else if (n.state === 'current') {
      icon = n.type === 'practice' ? '🎧' : n.type === 'reading' ? '📖' : n.checkpoint ? '⭐' : (n.customIcon || String(n.index + 1));
    } else {
      icon = ''; // completed — CSS ::after handles it
    }

    // Lessons with a real page (href !== '#') are always clickable, even if locked.
    const hasRealPage = n.type !== 'practice' && n.type !== 'reading' && n.href && n.href !== '#';

    if (n.state === 'locked' && !hasRealPage) {
      nodeEl.innerHTML = `
        <div class="${classes}">${icon}</div>
        <span class="path-label">${n.title}</span>
      `;
    } else {
      let href;
      if (n.type === 'practice') {
        href = buildPracticeUrl(n);
      } else if (n.href && n.href !== '#') {
        href = n.href;
      } else {
        href = '#';
      }
      nodeEl.innerHTML = `
        <a href="${href}" class="${classes}">${icon}</a>
        <span class="path-label">${n.title}</span>
        ${n.state === 'completed' ? '<span class="path-stars">⭐⭐⭐⭐⭐</span>' : ''}
      `;
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
    if (lesson.type === 'practice' || lesson.type === 'reading') return;
    lessonCount++;

    // Skip auto-inject if the next lesson is already a manual practice/reading
    const next = lessons[i + 1];
    const nextIsManual = next && (next.type === 'practice' || next.type === 'reading');

    // Add practice node after every 4th lesson
    if (!nextIsManual && lessonCount % 4 === 0 && i < lessons.length - 1) {
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
    if (!nextIsManual && lessonCount % 8 === 0 && i < lessons.length - 1) {
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
 * Hard 4-second timeout on the Firebase fetch so the learning path always
 * renders even if Firestore / gstatic CDN is unreachable.
 */
export async function getCompletedLessons(courseId) {
  const ids = new Set();

  // Always check local session completions (works in Incognito)
  try {
    const local = JSON.parse(sessionStorage.getItem('mathagram_completed_' + courseId) || '[]');
    local.forEach(id => ids.add(id));
  } catch(e) {}

  // Also check Firebase if logged in — but never let it block rendering
  const firebaseFetch = (async () => {
    const { auth, db } = await import('./firebase-config.js');
    const { collection, getDocs } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const user = auth.currentUser;
    if (!user) return;
    const snap = await getDocs(collection(db, 'users', user.uid, 'progress', courseId, 'lessons'));
    snap.forEach(doc => ids.add(doc.id));
  })();
  const timeout = new Promise((resolve) => setTimeout(resolve, 4000));
  try { await Promise.race([firebaseFetch, timeout]); } catch (e) {}

  return ids;
}

/**
 * Build a URL for the dedicated listening-practice page for this practice node.
 * Derives the course slug from the current page path (/courses/<slug>/...)
 * and the depth-appropriate path prefix to practice.html.
 */
function buildPracticeUrl(practiceNode) {
  const m = window.location.pathname.match(/\/courses?\/([^/]+)\//);
  const slug = m ? m[1] : '';
  const depth = (window.location.pathname.match(/\//g) || []).length - 1;
  const prefix = depth >= 2 ? '../../' : depth === 1 ? '../' : '';
  // Encode how many real lessons preceded this practice — lets practice.html
  // identify the *exact* next normal lesson to continue with.
  const idMatch = /practice-(\d+)/.exec(practiceNode.id || '');
  const after = idMatch ? idMatch[1] : '';
  const qs = `course=${encodeURIComponent(slug)}&unit=${encodeURIComponent(practiceNode.unit)}${after ? `&after=${after}` : ''}`;
  return `${prefix}practice.html?${qs}`;
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
