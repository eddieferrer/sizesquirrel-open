import GitRevisionPlugin from 'git-revision-webpack-plugin';

const gitRevisionPlugin = new GitRevisionPlugin({ lightweightTags: true });

const isProd = process.env.NODE_ENV === 'production';
const isDev = process.env.NODE_ENV !== 'production';

const d = new Date();
const nicelyFormattedDate = `${
  d.getMonth() + 1
}${d.getDate()}${d.getFullYear()}`;
const gitHash = gitRevisionPlugin.commithash().substring(0, 7);
const nicelyFormattedHour = `0${d.getHours()}`.slice(-2);
const nicelyFormattedTime = `${nicelyFormattedHour}${d.getMinutes()}`;

// Environment dependent variables
const envReleaseTag = isProd
  ? `${gitHash}-${nicelyFormattedDate}_${nicelyFormattedTime}`
  : 'dev';

// Common config
const config = {
  env: {
    baseUrl: process.env.BASE_URL || 'http://localhost:3000',
    VUE_APP_RELEASE_TAG: envReleaseTag,
    VUE_APP_GITBRANCH: gitRevisionPlugin.branch(),
    VUE_APP_GITVERSION: gitRevisionPlugin.version(),
    VUE_APP_GITHASH: gitRevisionPlugin.commithash(),
    isProd: process.env.NODE_ENV === 'production',
    isDev: process.env.NODE_ENV !== 'production',
  },

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'SizeSquirrel',
    titleTemplate: '%s | SizeSquirrel',
    htmlAttrs: {
      lang: 'en',
      amp: true,
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content:
          'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
      },
      { name: 'author', content: 'SizeSquirrel' },
      { name: 'copyright', content: 'SizeSquirrel, Copyright (c) 2021' },
      { property: 'fb:app_id', content: '943851385727348' },

      // Google / Schema.org markup:
      { itemprop: 'name', content: 'SizeSquirrel' },
      {
        itemprop: 'description',
        content:
          'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
      },
      {
        itemprop: 'image',
        content: 'https://www.sizesquirrel.com/images/OGImage1200x1200.jpg',
      },

      // Twitter
      // Test on: https://cards-dev.twitter.com/validator
      {
        hid: 'twitter:card',
        name: 'twitter:card',
        content: 'summary_large_image',
      },
      {
        hid: 'twitter:site',
        name: 'twitter:site',
        content: 'https://sizesquirrel.com',
      },
      {
        hid: 'twitter:url',
        name: 'twitter:url',
        content: 'https://sizesquirrel.com',
      },
      {
        hid: 'twitter:title',
        name: 'twitter:title',
        content:
          'Climbing shoe sizing, recommendations, and deals | SizeSquirrel',
      },
      {
        hid: 'twitter:description',
        name: 'twitter:description',
        content:
          'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
      },
      {
        hid: 'twitter:image',
        name: 'twitter:image',
        content: 'https://www.sizesquirrel.com/images/OGImage1200x1200.jpg',
      },

      // Open Graph
      // Test on: https://developers.facebook.com/tools/debug/
      {
        hid: 'og:site_name',
        property: 'og:site_name',
        content: 'SizeSquirrel',
      },
      { hid: 'og:type', property: 'og:type', content: 'website' },
      {
        hid: 'og:url',
        property: 'og:url',
        content: 'https://sizesquirrel.com',
      },
      {
        hid: 'og:title',
        property: 'og:title',
        content:
          'Climbing shoe sizing, recommendations, and deals | SizeSquirrel',
      },
      {
        hid: 'og:description',
        property: 'og:description',
        content:
          'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://www.sizesquirrel.com/images/OGImage1200x1200.jpg',
      },
      {
        hid: 'og:image:secure_url',
        property: 'og:image:secure_url',
        content: 'https://www.sizesquirrel.com/images/OGImage1200x1200.jpg',
      },
      {
        hid: 'og:image:alt',
        property: 'og:image:alt',
        content: 'SizeSquirrel',
      },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        hid: 'canonical',
        rel: 'canonical',
        href: `https://sizesquirrel.com`,
      },
    ],
    script: [
      { src: '/js/gtag-head.js' },
      { src: '/js/gtag-body.js', body: true },
      { src: '/js/fb-sdk.js', body: true },
      {
        src: 'https://www.googletagmanager.com/gtag/js?id=AW-872632887',
        async: true,
      },
    ],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    'vue-loading-overlay/dist/vue-loading.css',
    '~/assets/scss/colors.scss',
    '~/assets/scss/custom_bulma.scss',
    '~/assets/scss/global.scss',
    'vue-multiselect/dist/vue-multiselect.min.css',
    '~assets/scss/custom_multiselect.scss',
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    { src: '~/plugins/mixins' },
    { src: '~/plugins/lazy-image' },
    { src: '~/plugins/sentry' },
    '~/plugins/axios',
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: false,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    [
      '@nuxtjs/google-fonts',
      {
        display: 'swap',
        families: {
          'Shadows Into Light': true,
          Lato: {
            wght: [400, 700, 900],
          },
          Nunito: {
            wght: [400, 700],
          },
        },
      },
    ],
    [
      '@nuxtjs/google-analytics',
      {
        id: 'UA-75492234-4',
        set: [{ field: 'anonymizeIp', value: true }],
      },
    ],
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/style-resources',
    '@nuxtjs/proxy',
    'cookie-universal-nuxt',
  ],

  styleResources: {
    scss: ['~/assets/scss/colors.scss'],
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  // axios: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false,
        },
      },
    },
  },

  pwa: {
    meta: {
      name: 'SizeSquirrel',
      theme_color: '#0776bc',
    },
  },

  router: {
    extendRoutes(routes, resolve) {
      routes.push({
        path: '/facebookcallback_register',
        name: 'facebookcallback_register',
        component: resolve(__dirname, 'views/FacebookCallback.vue'),
        props: (route) => {
          const getUrlVarsFromHash = (hash) => {
            const vars = {};
            `?${hash}`.replace(/[?&]+([^=&]+)=([^&]*)/gi, (m, key, value) => {
              vars[key] = value;
            });
            return vars;
          };
          // facebook call back url starts with '#access_token`
          // which causes vue router to treat it all as hash and ignore
          // query params that come after '#access_token`
          const hashObj = getUrlVarsFromHash(route.hash);
          return {
            state: hashObj.state,
            formType: 'register',
            accessToken: hashObj['#access_token'],
          };
        },
      });
      routes.push({
        path: '/facebookcallback_login',
        name: 'facebookcallback_login',
        component: resolve(__dirname, 'views/FacebookCallback.vue'),
        props: (route) => {
          const getUrlVarsFromHash = (hash) => {
            const vars = {};
            `?${hash}`.replace(/[?&]+([^=&]+)=([^&]*)/gi, (m, key, value) => {
              vars[key] = value;
            });
            return vars;
          };
          // facebook call back url starts with '#access_token`
          // which causes vue router to treat it all as hash and ignore
          // query params that come after '#access_token`
          const hashObj = getUrlVarsFromHash(route.hash);
          return {
            state: hashObj.state,
            formType: 'login',
            accessToken: hashObj['#access_token'],
          };
        },
      });
    },
  },
};

if (isDev) {
  config.proxy = {
    '/apiv2': {
      target: 'http://localhost:5000',
      changeOrigin: false,
    },
  };
}

export default config;
