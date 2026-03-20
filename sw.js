// Mathagram Service Worker — enables offline and PWA install
const CACHE_NAME = 'mathagram-v1';
const OFFLINE_URL = '/';

// Files to cache for offline
const PRECACHE = [
  '/',
  '/index.html',
  '/courses.html',
  '/login.html',
  '/css/global.css',
  '/css/exercises.css',
  '/css/characters.css',
  '/css/learning-path.css',
  '/js/exercises.js',
  '/js/characters.js',
  '/js/auth.js',
  '/js/nav.js',
  '/js/progress.js',
  '/js/sanitize.js',
  '/js/lighthouse.js',
  '/js/learning-path.js',
  '/assets/lighthouse/logo.svg',
  '/manifest.json'
];

// Install — cache core files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(PRECACHE))
  );
  self.skipWaiting();
});

// Activate — clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch — serve from cache, fallback to network
self.addEventListener('fetch', event => {
  // Skip non-GET and Firebase requests
  if (event.request.method !== 'GET') return;
  if (event.request.url.includes('firestore.googleapis.com')) return;
  if (event.request.url.includes('identitytoolkit.googleapis.com')) return;
  if (event.request.url.includes('gstatic.com/firebasejs')) return;

  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        // Cache successful responses
        if (response.ok && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      }).catch(() => {
        // Offline fallback
        if (event.request.destination === 'document') {
          return caches.match(OFFLINE_URL);
        }
      });
    })
  );
});
