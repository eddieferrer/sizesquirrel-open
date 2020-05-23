/* eslint-disable no-restricted-globals */
// This is the code piece that GenerateSW mode can't provide for us.
// This code listens for the user's confirmation to update the app.
self.addEventListener('message', event => {
  event.stopImmediatePropagation();
  if (event.data && event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
});

workbox.core.clientsClaim();

// The precaching code provided by Workbox.
self.__precacheManifest = [].concat(self.__precacheManifest || []);
workbox.precaching.precacheAndRoute(self.__precacheManifest, {});
