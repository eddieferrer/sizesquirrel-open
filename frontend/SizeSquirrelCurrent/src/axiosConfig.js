import * as Sentry from '@sentry/browser';
import axios from 'axios';
import store from '@/store/store';

// Axios settings
axios.interceptors.response.use(
  (response) => {
    // intercept the global error
    return response;
  },
  (error) => {
    if (error.response && error.response.status) {
      // console.log('original request', error.config);
      if (error.response.status === 401) {
        localStorage.removeItem('user-token'); // clear your user's token from localstorage
        delete axios.defaults.headers.common.Authorization;
        window.location.href = '/login?loginagain=1';
      }
      if (error.response.status === 404) {
        if (Sentry) {
          Sentry.captureMessage(`404 Error API - ${error.config.url}`);
        }
      }
      if (error.response.status === 400) {
        if (Sentry) {
          Sentry.captureMessage(`400 Error - ${error.config.url} - ${error.config.url}`);
        }
      }

      const errorMessage = error.response?.data?.message;
      const errorMessageFeedback = errorMessage
        ? Object.values(errorMessage).filter((entry) => entry.trim() !== '')?.length > 0
        : undefined;

      if (error.response.status === 400 && (!errorMessage || !errorMessageFeedback)) {
        store.dispatch('SHOW_FLASH_MESSAGE', {
          class: 'has-background-danger',
          message: 'There has been a fatal server error. Please reload the page.',
        });
      }
    }
    // Do something with response error
    return Promise.reject(error);
  }
);

const token = localStorage.getItem('user-token');
if (token) {
  axios.defaults.headers.common.Authorization = `Bearer ${token}`;
}
