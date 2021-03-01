import Vue from 'vue';
import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';

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
}
