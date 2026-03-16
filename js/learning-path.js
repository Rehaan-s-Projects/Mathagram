// js/learning-path.js
// Renders Duolingo-style learning paths from lesson data.

import { auth } from './firebase-config.js';
import { db } from './firebase-config.js';
import { collection, getDocs } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

/**
 * Render a learning path into a container.
 * @param {HTMLElement} container - element to render path into
 * @param {object[]} lessons - array of { id, title, href, unit, unitName, category, checkpoint }
 * @param {Set<string>} completedIds - set of completed lesson IDs
 */
export function renderPath(container, lessons, completedIds = new Set()) {
  container.innerHTML = '';

  // Progress bar
  const completedCount = lessons.filter(l => completedIds.has(l.id)).length;
  const progressPct = lessons.length > 0 ? Math.round((completedCount / lessons.length) * 100) : 0;

  const progressBar = document.createElement('div');
  progressBar.className = 'path-progress';
  progressBar.innerHTML = `
    <div class="path-progress-bar">
      <div class="path-progress-fill" style="width:${progressPct}%"></div>
    </div>
    <span class="path-progress-text">${completedCount}/${lessons.length}</span>
  `;
  container.appendChild(progressBar);

  // Path line
  const pathLine = document.createElement('div');
  pathLine.className = 'path-line';
  container.appendChild(pathLine);

  let currentUnit = null;
  let foundCurrent = false;

  lessons.forEach((lesson, i) => {
    // Unit header
    if (lesson.unit !== currentUnit) {
      currentUnit = lesson.unit;
      const header = document.createElement('div');
      header.className = 'path-unit-header';
      header.innerHTML = `
        <span class="path-unit-badge ${lesson.category}">${lesson.category}</span>
        <div class="path-unit-name">${lesson.unitName}</div>
      `;
      container.appendChild(header);
    }

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
    const nodeState = isCompleted ? 'completed' : isCurrent ? 'current' : 'locked';

    const node = document.createElement('div');
    node.className = `path-node ${nodeState}`;

    const isCheckpoint = lesson.checkpoint || (i > 0 && i % 5 === 4);
    const circleClass = `path-circle ${state}${isCheckpoint ? ' checkpoint' : ''}`;

    if (isLocked) {
      node.innerHTML = `
        <div class="${circleClass}">
          <span style="font-size:1.2rem">🔒</span>
        </div>
        <span class="path-label">${lesson.title}</span>
      `;
    } else if (isCurrent) {
      node.innerHTML = `
        <a href="${lesson.href}" class="${circleClass}">
          ${i + 1}
        </a>
        <span class="path-label">${lesson.title}</span>
      `;
    } else if (isCompleted) {
      node.innerHTML = `
        <a href="${lesson.href}" class="${circleClass}"></a>
        <span class="path-label">${lesson.title}</span>
        <span class="path-stars">⭐⭐⭐</span>
      `;
    }

    container.appendChild(node);
  });
}

/**
 * Get completed lesson IDs for a user from Firestore.
 * @param {string} courseId
 * @returns {Promise<Set<string>>}
 */
export async function getCompletedLessons(courseId) {
  const user = auth.currentUser;
  if (!user) return new Set();

  try {
    const snap = await getDocs(
      collection(db, 'users', user.uid, 'progress', courseId, 'lessons')
    );
    const ids = new Set();
    snap.forEach(doc => ids.add(doc.id));
    return ids;
  } catch (e) {
    return new Set();
  }
}
