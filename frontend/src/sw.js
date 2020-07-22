/* eslint-disable no-restricted-globals */

// config
workbox.setConfig({
  debug: false,
});

// workbox.core.clientsClaim();

// This is the code piece that GenerateSW mode can't provide for us.
// This code listens for the user's confirmation to update the app.
self.addEventListener('message', (event) => {
  event.stopImmediatePropagation();
  if (event.data && event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
});

// apply precaching. In the built version, the precacheManifest will
// be imported using importScripts (as is workbox itself) and we can
// precache this. This is all we need for precaching
workbox.precaching.precacheAndRoute([]);

workbox.routing.registerRoute(
  ({ request }) => request.destination === 'image',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'images',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
      }),
    ],
  })
);

workbox.routing.registerRoute(
  ({ request }) => request.destination === 'script' || request.destination === 'style',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'static-resources',
  })
);

workbox.routing.registerRoute(
  new RegExp(/\/apiv2/),
  new workbox.strategies.NetworkFirst({
    cacheName: 'api',
  })
);

workbox.routing.registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  new workbox.strategies.CacheFirst({
    cacheName: 'googleapis',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 30,
      }),
    ],
  })
);
