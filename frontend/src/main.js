import Vue from 'vue';
import axios from 'axios';
import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';
import { VLazyImagePlugin } from 'v-lazy-image';

import App from './App.vue';
import router from './router';
import store from './store/store';
import './registerServiceWorker';

Vue.use(VLazyImagePlugin);

if (process.env.NODE_ENV === 'production') {
  Sentry.init({
    dsn: 'https://a9141ca353da483ea41c75d13d949694@sentry.io/830985',
    integrations: [
      new Integrations.Vue({
        Vue,
        attachProps: true,
      }),
    ],
    release: process.env.VUE_APP_RELEASE_TAG,
  });
}

Vue.config.productionTip = false;

axios.interceptors.response.use(
  (response) => {
    // intercept the global error
    return response;
  },
  (error) => {
    if (error.response && error.response.status) {
      // const originalRequest = error.config;
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
    // sample code
    // if (error.response.status === 401 && !originalRequest._retry) { // if the error is 401 and hasent already been retried
    //   originalRequest._retry = true // now it can be retried
    //   return Vue.axios.post('/users/token', null).then((data) => {
    //     store.dispatch('authfalse')
    //     store.dispatch('authtruth', data.data)
    //     originalRequest.headers['Authorization'] = 'Bearer ' + store.state.token // new header new token
    //     return Vue.axios(originalRequest) // retry the request that errored out
    //   }).catch((error) => {
    //     for (let i = 0; i < error.response.data.errors.length; i++) {
    //       if (error.response.data.errors[i] === 'TOKEN-EXPIRED') {
    //         auth.logout()
    //         return
    //       }
    //     }
    //   })
    // }
    // if (error.response.status === 404 && !originalRequest._retry) {
    //   originalRequest._retry = true
    //   window.location.href = '/'
    //   return
    // }
    // Do something with response error
    return Promise.reject(error);
  }
);

Vue.mixin({
  methods: {
    deepFind(obj, path) {
      const paths = path.split('.');
      let current = obj;
      let i;

      for (i = 0; i < paths.length; ++i) {
        if (Array.isArray(current)) {
          [current] = current;
        }
        if (current[paths[i]] === undefined) {
          return undefined;
        }
        current = current[paths[i]];
      }

      return current;
    },
    getClass(percentage) {
      if (percentage > 50) {
        return 'is-success';
      }
      if (percentage < 50) {
        return 'is-warning';
      }
      // if (percentage === 50) {
      return 'is-danger';
    },
    notEmptyObject(someObject) {
      return Object.keys(someObject).length;
    },
    getParameterByName(name) {
      const match = RegExp(`[?&]${name}=([^&]*)`).exec(window.location.search);
      return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
    },
    openFbLoginDialog(formType) {
      // prod appId
      let appId = '943851385727348';
      let protocol = 'https';
      let port = '';
      if (window.location.hostname === 'localhost') {
        // dev appId
        protocol = 'http';
        port = ':5000';
        appId = '944781472301006';
      }
      const redirecturi = `${protocol}://${window.location.hostname}${port}/facebookcallback_${formType}/`;
      const stateParam = new Date().getUTCDate();

      const facebookURL = `https://www.facebook.com/v5.0/dialog/oauth?client_id=${appId}&redirect_uri=${redirecturi}&response_type=token&scope=email&state=${stateParam}`;
      window.location.href = facebookURL;
    },
    getUrlVars() {
      const vars = {};
      window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, (m, key, value) => {
        vars[key] = value;
      });
      return vars;
    },
  },
});

Vue.mixin({
  data() {
    return {
      isLoadingComponent: false,
      hasComponentFailedToLoad: false,
    };
  },
});

const token = localStorage.getItem('user-token');
if (token) {
  axios.defaults.headers.common.Authorization = `Bearer ${token}`;
}

new Vue({
  beforeCreate() {
    // Safari, in Private Browsing Mode, looks like it supports localStorage but all calls to setItem
    // throw QuotaExceededError. We're going to detect this and just silently drop any calls to setItem
    // to avoid the entire page breaking, without having to do a check at each usage of Storage.
    if (typeof localStorage === 'object') {
      try {
        localStorage.setItem('localStorage', 1);
        localStorage.removeItem('localStorage');
      } catch (e) {
        Storage.prototype._setItem = Storage.prototype.setItem;
        Storage.prototype.setItem = () => {};
        // eslint-disable-next-line no-alert
        alert(
          'Your web browser does not support storing settings locally. In Safari, the most common cause of this is using "Private Browsing Mode". Some settings may not save or some features may not work properly for you.'
        );
      }
    }
  },
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
