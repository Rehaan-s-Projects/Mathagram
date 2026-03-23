// js/learning-path.js
// Renders Duolingo-style learning paths with side-by-side nodes,
// practice sessions, and reading skill nodes.

// Firebase imports moved into getCompletedLessons() so renderPath works even if Firebase fails

/**
 * Render a learning path into a container.
 * Lessons are displayed in zigzag rows of 3 with practice & reading nodes.
 */
export function renderPath(container, lessons, completedIds = new Set()) {
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

    // Determine state
    const isCompleted = completedIds.has(lesson.id);
    let isCurrent = false;
    let isLocked = false;

    if (!isCompleted && !foundCurrent) {
      isCurrent = true;
      foundCurrent = true;
    } else if (!isCompleted) {
      isLocked = true;
    }

    const state = isCompleted ? 'completed' : isCurrent ? 'current' : 'locked';

    rowBuffer.push({ ...lesson, state, index: i });

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
        ${n.state === 'completed' ? '<span class="path-stars">⭐⭐⭐</span>' : ''}
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
 * Get completed lesson IDs for a user from Firestore.
 */
export async function getCompletedLessons(courseId) {
  try {
    const { auth } = await import('./firebase-config.js');
    const { db } = await import('./firebase-config.js');
    const { collection, getDocs } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const user = auth.currentUser;
    if (!user) return new Set();
    const snap = await getDocs(collection(db, 'users', user.uid, 'progress', courseId, 'lessons'));
    const ids = new Set();
    snap.forEach(doc => ids.add(doc.id));
    return ids;
  } catch (e) {
    return new Set();
  }
}
