/**
 * Progress System for Mathagram.org
 *
 * Handles XP, levels, grades, and Firestore persistence.
 */

import { db, auth } from './firebase-config.js';
import {
  doc,
  getDoc,
  setDoc,
  updateDoc,
  increment,
  getDocs,
  collection
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

export const LEVELS = [
  { level: 1, xp: 0,    title: 'Spark' },
  { level: 2, xp: 50,   title: 'Beam' },
  { level: 3, xp: 150,  title: 'Glow' },
  { level: 4, xp: 300,  title: 'Flare' },
  { level: 5, xp: 500,  title: 'Radiance' },
  { level: 6, xp: 800,  title: 'Beacon' },
  { level: 7, xp: 1200, title: 'Lighthouse Keeper' },
  { level: 8, xp: 1800, title: 'Lighthouse Master' }
];

// ---------------------------------------------------------------------------
// Pure helpers
// ---------------------------------------------------------------------------

/**
 * Determine the user's level info from their total XP.
 * @param {number} xp – total XP accumulated
 * @returns {{ level: number, title: string, xpForNext: number, xpProgress: number }}
 */
export function calculateLevel(xp) {
  let current = LEVELS[0];

  for (const l of LEVELS) {
    if (xp >= l.xp) {
      current = l;
    } else {
      break;
    }
  }

  const idx = LEVELS.indexOf(current);
  const next = LEVELS[idx + 1];

  if (!next) {
    // Max level reached
    return { level: current.level, title: current.title, xpForNext: 0, xpProgress: 1 };
  }

  const range = next.xp - current.xp;
  const progress = (xp - current.xp) / range;

  return {
    level: current.level,
    title: current.title,
    xpForNext: next.xp - xp,
    xpProgress: progress
  };
}

/**
 * Convert a 0-100 score into a letter grade, star count, and pass/fail.
 * @param {number} score – 0 to 100
 * @returns {{ grade: string, stars: number, passed: boolean }}
 */
export function calculateGrade(score) {
  if (score >= 95) return { grade: 'A',  stars: 3, passed: true };
  if (score >= 90) return { grade: 'A-', stars: 3, passed: true };
  if (score >= 85) return { grade: 'B+', stars: 2, passed: true };
  if (score >= 80) return { grade: 'B',  stars: 2, passed: true };
  if (score >= 75) return { grade: 'B-', stars: 2, passed: true };
  if (score >= 70) return { grade: 'C+', stars: 1, passed: true };
  if (score >= 65) return { grade: 'C',  stars: 1, passed: true };
  if (score >= 60) return { grade: 'C-', stars: 1, passed: true };
  if (score >= 50) return { grade: 'D',  stars: 0, passed: false };
  return              { grade: 'F',  stars: 0, passed: false };
}

/**
 * Calculate XP earned for a given score.
 * @param {number} score – 0 to 100
 * @returns {number} XP earned (0 if not passed)
 */
export function calculateXP(score) {
  const { passed } = calculateGrade(score);
  if (!passed) return 0;

  let xp = 10; // base XP for passing
  if (score === 100) xp += 5; // perfect-score bonus
  return xp;
}

// ---------------------------------------------------------------------------
// Firestore persistence
// ---------------------------------------------------------------------------

/**
 * Save a lesson result to Firestore and update the user's XP / level.
 *
 * @param {string} courseId
 * @param {string} lessonId
 * @param {number} score – 0 to 100
 * @returns {Promise<{ grade: string, stars: number, xpEarned: number }|null>}
 */
export async function saveLessonResult(courseId, lessonId, score, quizXP) {
  const user = auth.currentUser;
  if (!user) return null;

  const { grade, stars, passed } = calculateGrade(score);
  const xpEarned = quizXP != null ? quizXP : calculateXP(score);

  // Persist lesson result
  const lessonRef = doc(db, 'users', user.uid, 'progress', courseId, 'lessons', lessonId);
  await setDoc(lessonRef, {
    score,
    grade,
    stars,
    passed,
    xpEarned,
    completedAt: new Date().toISOString()
  }, { merge: true });

  // Update total XP on user document
  const userRef = doc(db, 'users', user.uid);

  // Migrate any legacy totalXP into xp field
  const prevSnap = await getDoc(userRef);
  if (prevSnap.exists()) {
    const data = prevSnap.data();
    if (data.totalXP && !data.xp) {
      await updateDoc(userRef, { xp: data.totalXP, totalXP: 0 });
    }
  }

  await updateDoc(userRef, { xp: increment(xpEarned) });

  // Update streak
  const now = new Date();
  const todayStr = now.toISOString().slice(0, 10);
  const snapAfterXP = await getDoc(userRef);
  const userData = snapAfterXP.exists() ? snapAfterXP.data() : {};
  const lastActive = userData.lastActive ? userData.lastActive.slice(0, 10) : null;

  let newStreak = userData.streak || 0;
  if (lastActive !== todayStr) {
    const yesterday = new Date(now);
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toISOString().slice(0, 10);

    if (lastActive === yesterdayStr) {
      newStreak += 1; // consecutive day
    } else if (lastActive !== todayStr) {
      newStreak = 1; // streak broken, start fresh
    }
    await updateDoc(userRef, { streak: newStreak, lastActive: now.toISOString() });
  }

  // Recalculate level from new total and persist
  const userSnap = await getDoc(userRef);
  const totalXP = userSnap.exists() ? (userSnap.data().xp || 0) : 0;
  const { level, title } = calculateLevel(totalXP);
  await updateDoc(userRef, { level, levelTitle: title });

  return { grade, stars, xpEarned };
}

/**
 * Retrieve all lesson results for a course.
 *
 * @param {string} courseId
 * @returns {Promise<Object.<string, { grade: string, stars: number, score: number }>>}
 */
export async function getCourseProgress(courseId) {
  const user = auth.currentUser;
  if (!user) return {};

  const lessonsCol = collection(db, 'users', user.uid, 'progress', courseId, 'lessons');
  const snapshot = await getDocs(lessonsCol);

  const progress = {};
  snapshot.forEach((docSnap) => {
    const data = docSnap.data();
    progress[docSnap.id] = {
      grade: data.grade,
      stars: data.stars,
      score: data.score
    };
  });

  return progress;
}
