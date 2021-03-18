import Vue from 'vue';
import VueGtag from 'vue-gtag';

const isProd = process.env.NODE_ENV === 'production';

export default ({ app }) => {
  const getGDPR = localStorage.getItem('GDPR:accepted');
  Vue.use(
    VueGtag,
    {
      config: { id: 'UA-75492234-4' },
      bootstrap: getGDPR === 'true',
      appName: 'APP_NAME',
      enabled: getGDPR === 'true' && isProd,
      pageTrackerScreenviewEnabled: true,
    },
    app.router
  );
};
