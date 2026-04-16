/**
 * Firebase Configuration for Mathagram.org
 *
 * Firebase config values are public by design — they identify your project
 * to the Firebase SDK but do NOT grant privileged access. Security is
 * enforced by Firestore security rules (see firestore.rules).
 *
 * Replace the placeholder values below with your real Firebase project config.
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyBU3VwkSJDbwBumJoRKz-7b6eHxvgfB_Ho",
  authDomain: "mathagram-cb526.firebaseapp.com",
  projectId: "mathagram-cb526",
  storageBucket: "mathagram-cb526.firebasestorage.app",
  messagingSenderId: "513288333441",
  appId: "1:513288333441:web:909c16d06a8ed0b7208580"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
