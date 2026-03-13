// js/leaderboard.js
import { db } from './firebase-config.js';
import { collection, query, orderBy, limit, getDocs } from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';
import { LEVELS } from './progress.js';

/**
 * Fetch top users by XP.
 * @param {number} count - number of users to fetch (default 50)
 * @returns {Promise<Array>} array of { rank, displayName, character, xp, level, title }
 */
export async function getLeaderboard(count = 50) {
  const q = query(
    collection(db, 'users'),
    orderBy('xp', 'desc'),
    limit(count)
  );

  const snap = await getDocs(q);
  const users = [];
  let rank = 1;

  snap.forEach(doc => {
    const data = doc.data();
    const levelInfo = getLevelInfo(data.xp || 0);
    users.push({
      rank: rank++,
      uid: doc.id,
      displayName: data.displayName || 'Anonymous',
      character: data.character || 'edam',
      xp: data.xp || 0,
      level: levelInfo.level,
      title: levelInfo.title
    });
  });

  return users;
}

/**
 * Get level info from XP (duplicated from progress.js to avoid circular deps).
 */
function getLevelInfo(xp) {
  let current = LEVELS[0];
  for (const l of LEVELS) {
    if (xp >= l.xp) current = l;
    else break;
  }
  return current;
}
