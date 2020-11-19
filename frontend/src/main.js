import Vue from 'vue';
import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';
import { VLazyImagePlugin } from 'v-lazy-image';
import VueAnalytics from 'vue-analytics';

import App from './App.vue';
import router from './router';
import store from './store/store';
import './registerServiceWorker';
import './axiosConfig';

Vue.use(VLazyImagePlugin);

const isProd = process.env.NODE_ENV === 'production';

if (isProd) {
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

  Vue.use(VueAnalytics, {
    id: 'UA-75492234-4',
    router,
    debug: {
      enabled: !isProd,
      sendHitTask: isProd,
    },
    set: [{ field: 'anonymizeIp', value: true }],
  });
}

Vue.config.productionTip = false;

// Vue Mixins
// TODO move these out of this file
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
      return Object.keys(someObject).length !== 0;
    },
    getParameterByName(name) {
      const match = RegExp(`[?&]${name}=([^&]*)`).exec(window.location.search);
      return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
    },
    openFbLoginDialog(formType, redirect) {
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
      const stateParams = {
        redirect,
        time: new Date().getTime(), // Not currently used
      };

      const facebookURL = `https://www.facebook.com/v5.0/dialog/oauth?client_id=${appId}&redirect_uri=${redirecturi}&response_type=token&scope=email&state=${JSON.stringify(
        stateParams
      )}`;
      window.location.href = facebookURL;
    },
  },
});

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
