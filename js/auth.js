/**
 * Auth Module for Mathagram.org
 *
 * Handles Firebase Authentication (signup, signin, signout) and
 * creates/reads user profile documents in Firestore.
 */

import { auth, db } from './firebase-config.js';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  sendEmailVerification,
  sendPasswordResetEmail,
  GoogleAuthProvider,
  signInWithPopup,
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js';
import {
  doc,
  setDoc,
  getDoc,
} from 'https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js';

/**
 * Sanitize a string to prevent XSS by leveraging the DOM's built-in
 * text encoding.  Setting textContent on an element escapes any HTML
 * entities; reading innerHTML back gives us the safe version.
 *
 * @param {string} str — raw user input
 * @returns {string} HTML-entity-escaped string
 */
function sanitizeText(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

/**
 * Create a new user account, send a verification email, and initialise
 * their Firestore profile document.
 *
 * @param {string} email
 * @param {string} password
 * @param {string} displayName — will be sanitized before storage
 * @param {string} color  — chosen profile color (e.g. 'blue', 'green')
 * @returns {Promise<import('firebase/auth').User>}
 */
export async function signUp(email, password, displayName, color) {
  const { user } = await createUserWithEmailAndPassword(auth, email, password);

  await sendEmailVerification(user);

  const now = new Date().toISOString();
  await setDoc(doc(db, 'users', user.uid), {
    displayName: sanitizeText(displayName),
    color: color,
    xp: 0,
    level: 1,
    streak: 0,
    lastActive: now,
    createdAt: now,
  });

  return user;
}

/**
 * Sign in an existing user with email and password.
 *
 * @param {string} email
 * @param {string} password
 * @returns {Promise<import('firebase/auth').User>}
 */
export async function signIn(email, password) {
  const { user } = await signInWithEmailAndPassword(auth, email, password);
  return user;
}

/**
 * Sign in with Google account. Creates a Firestore profile if first time.
 *
 * @returns {Promise<import('firebase/auth').User>}
 */
export async function signInWithGoogle() {
  const provider = new GoogleAuthProvider();
  const { user } = await signInWithPopup(auth, provider);

  // Create Firestore profile if it doesn't exist yet
  const snap = await getDoc(doc(db, 'users', user.uid));
  if (!snap.exists()) {
    const now = new Date().toISOString();
    await setDoc(doc(db, 'users', user.uid), {
      displayName: sanitizeText(user.displayName || 'User'),
      color: 'blue',
      xp: 0,
      level: 1,
      streak: 0,
      lastActive: now,
      createdAt: now,
    });
  }

  return user;
}

/**
 * Sign the current user out.
 *
 * @returns {Promise<void>}
 */
export async function logOut() {
  await signOut(auth);
}

/**
 * Send a password-reset email to the given address.
 * Throws if the email is malformed or Firebase rejects the request.
 *
 * @param {string} email
 * @returns {Promise<void>}
 */
export async function resetPassword(email) {
  await sendPasswordResetEmail(auth, email);
}

/**
 * Subscribe to authentication state changes.
 *
 * @param {(user: import('firebase/auth').User | null) => void} callback
 * @returns {import('firebase/auth').Unsubscribe}
 */
export function onAuthChange(callback) {
  return onAuthStateChanged(auth, callback);
}

/**
 * Fetch the current user's Firestore profile document.
 *
 * @returns {Promise<Object|null>} profile data or null if not signed in /
 *   document missing
 */
export async function getUserProfile() {
  const user = auth.currentUser;
  if (!user) return null;

  const snap = await getDoc(doc(db, 'users', user.uid));
  return snap.exists() ? snap.data() : null;
}
