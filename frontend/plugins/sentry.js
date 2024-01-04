import Vue from 'vue';
import * as Sentry from '@sentry/vue';

const isProd = process.env.NODE_ENV === 'production';

export default ({ app }, inject) => {
  if (isProd) {
    Sentry.init({
      Vue,
      dsn: 'https://a9141ca353da483ea41c75d13d949694@sentry.io/830985',
      integrations: [
        new Sentry.BrowserTracing({
          routingInstrumentation: Sentry.vueRouterInstrumentation(app.router),
        }),
        new Sentry.Replay(),
      ],
      release: process.env.VUE_APP_RELEASE_TAG,
    });
  }
};
