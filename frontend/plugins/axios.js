import * as Sentry from '@sentry/browser';

export default function ({ $axios, redirect, store, $cookies }) {
  $axios.onRequest((config) => {
    // eslint-disable-next-line no-console
    console.log('Making request to ' + config.url);
  });

  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status);
    if (code === 400 || code === 504) {
      const errorMessage = error.response?.data?.message;
      const errorMessageFeedback = errorMessage
        ? Object.values(errorMessage).filter((entry) => entry.trim() !== '')
            ?.length > 0
        : undefined;

      // If these exist vue template handles error
      if (!errorMessage || !errorMessageFeedback) {
        store.dispatch('SHOW_FLASH_MESSAGE', {
          class: 'has-background-danger',
          message:
            'There has been a fatal server error. Please reload the page.',
        });
      }
    }

    if (code === 401) {
      $cookies.remove('user-token');
      $axios.setToken(false);
      if (process.server) {
        redirect(`/login?loginagain=1`);
      } else {
        const redirectUrl = decodeURIComponent(window.location.pathname);
        redirect(`/login?loginagain=1&redirect=${redirectUrl}`);
      }
    }

    if (code === 404) {
      if (Sentry) {
        Sentry.captureMessage(`404 Error API - ${error.config.url}`);
      }
      redirect('/404');
    }
  });

  if (process.server) {
    return;
  }

  $axios.interceptors.request.use((request) => {
    // Get token from auth.js store
    const token = store.state.token;

    // Update token axios header
    if (token) {
      request.headers.common.Authorization = `Bearer ${token}`;
    }
    return request;
  });
}
