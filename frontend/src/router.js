import Vue from 'vue';
import Router from 'vue-router';
import Meta from 'vue-meta';
import * as Sentry from '@sentry/browser';
import VueAnalytics from 'vue-analytics';
import store from '@/store/store';
import Home from './views/Home.vue';

Vue.use(Router);
Vue.use(Meta);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/admin/stats',
      name: 'stats',
      component: () => import(/* webpackChunkName: "admin" */ './views/Stats.vue'),
      meta: {
        requiresAdmin: true,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/admin/matchtest',
      name: 'matchtest',
      component: () => import(/* webpackChunkName: "admin" */ './views/MatchTest.vue'),
      meta: {
        requiresAdmin: true,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/browse',
      name: 'browse',
      component: () => import(/* webpackChunkName: "browse" */ './views/Browse.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/facebookcallback_register',
      name: 'facebookcallback_register',
      component: () =>
        import(/* webpackChunkName: "facebookcallback" */ './views/FacebookCallback.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
      props: { formType: 'register' },
    },
    {
      path: '/facebookcallback_login',
      name: 'facebookcallback_login',
      component: () =>
        import(/* webpackChunkName: "facebookcallback" */ './views/FacebookCallback.vue'),
      meta: {
        hideItemMatchForm: true,
      },
      props: { formType: 'login' },
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import(/* webpackChunkName: "faq" */ './views/Faq.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/forgot_password',
      name: 'forgotPassword',
      component: () =>
        import(/* webpackChunkName: "forgotPassword" */ './views/ForgotPassword.vue'),
      meta: { requiresAuth: false },
    },
    {
      path: '/forgot_username',
      name: 'forgotUsername',
      component: () =>
        import(/* webpackChunkName: "forgotUsername" */ './views/ForgotUsername.vue'),
      meta: { requiresAuth: false },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import(/* webpackChunkName: "login" */ './views/Login.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/match',
      name: 'privateMatch',
      component: () => import(/* webpackChunkName: "match" */ './views/Match.vue'),
      meta: {
        requiresAuth: true,
        requiresContext: true,
      },
    },
    {
      path: '/my_profile',
      name: 'myProfile',
      beforeEnter: (to, from, next) => {
        store.dispatch('GET_USER').then(() => {
          // the above state is not available here, since it
          // it is resolved asynchronously in the store action
          const { username } = store.getters.user;
          // router.push({ path: '/profile/' + username });
          next(`/profile/${username}`);
        });
      },
      meta: { requiresAuth: true },
    },
    {
      path: '/my_user_details',
      name: 'myUserDetails',
      beforeEnter: (to, from, next) => {
        store.dispatch('GET_USER').then(() => {
          // the above state is not available here, since it
          // it is resolved asynchronously in the store action
          const { username } = store.getters.user;
          // router.push({ path: '/profile/' + username });
          next(`/profile/${username}#user_details`);
        });
      },
      meta: { requiresAuth: true },
    },
    {
      path: '/notauthorized',
      name: 'notAuthorized',
      component: () => import(/* webpackChunkName: "notAuthorized" */ './views/NotAuthorized.vue'),
      meta: { requiresAuth: false },
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () => import(/* webpackChunkName: "termsPrivacy" */ './views/Privacy.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: () => import(/* webpackChunkName: "profile" */ './views/Profile.vue'),
      meta: {
        requiresAuth: false,
        requiresContext: true,
      },
    },
    {
      path: '/public_match',
      name: 'publicMatch',
      component: () => import(/* webpackChunkName: "match" */ './views/Match.vue'),
      meta: {
        requiresAuth: false,
        requiresContext: true,
      },
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: () => import(/* webpackChunkName: "recommend" */ './views/Recommend.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import(/* webpackChunkName: "register" */ './views/Register.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/reset_password',
      name: 'reset_password',
      component: () => import(/* webpackChunkName: "reset_password" */ './views/ResetPassword.vue'),
      meta: { requiresAuth: false },
    },
    {
      path: '/release',
      name: 'release',
      component: () => import(/* webpackChunkName: "release" */ './views/Release.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/sales',
      name: 'sales',
      component: () => import(/* webpackChunkName: "sales" */ './views/Sales.vue'),
      meta: { requiresAuth: false },
    },
    {
      path: '/shoe/:shoe_brand',
      redirect: '/shoes/:shoe_brand',
    },
    {
      path: '/shoes/:shoe_brand',
      name: 'brand',
      component: () => import(/* webpackChunkName: "brand" */ './views/Brand.vue'),
      meta: {
        requiresAuth: false,
        requiresContext: true,
      },
    },
    {
      path: '/shoe/:shoe_brand/:shoe_model',
      redirect: '/shoes/:shoe_brand/:shoe_model',
    },
    {
      path: '/shoes/:shoe_brand/:shoe_model',
      name: 'shoe',
      component: () => import(/* webpackChunkName: "shoe" */ './views/Shoe.vue'),
      meta: {
        requiresAuth: false,
        requiresContext: true,
      },
    },
    {
      path: '/terms',
      name: 'terms',
      component: () => import(/* webpackChunkName: "termsPrivacy" */ './views/Terms.vue'),
      meta: {
        requiresAuth: false,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/404',
      name: 'notFound',
      component: () => import(/* webpackChunkName: "notFound" */ './views/NotFound.vue'),
      beforeEnter: (to, from, next) => {
        if (Sentry) {
          Sentry.captureMessage(`404 Error Not Found - ${to.redirectedFrom}`);
        }
        next();
      },
      meta: { requiresAuth: false },
    },
    { path: '*', redirect: '/404' },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({ selector: to.hash, offset: { x: 0, y: -350 } });
        }, 1500);
      });
    }
    if (savedPosition) {
      return savedPosition;
    }
    return { x: 0, y: 0 };
  },
});

const isProd = process.env.NODE_ENV === 'production';
if (isProd) {
  Vue.use(VueAnalytics, {
    id: 'UA-75492234-4',
    router,
    debug: {
      enabled: !isProd,
      sendHitTask: isProd,
    },
  });
}

export default router;
