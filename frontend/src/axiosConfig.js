import * as Sentry from '@sentry/browser';
import axios from 'axios';

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
    }
    // Do something with response error
    return Promise.reject(error);
  }
);

const token = localStorage.getItem('user-token');
if (token) {
  axios.defaults.headers.common.Authorization = `Bearer ${token}`;
}
