import Vue from 'vue';
import Router from 'vue-router';
import Meta from 'vue-meta';
import * as Sentry from '@sentry/browser';
import store from '@/store/store';

Vue.use(Router);
Vue.use(Meta);

// All Possible Route Properties:
// Default is false
// requiresAdmin: true,
// requiresAuth: true
// hideItemMatchForm: true,

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    // DONE IN NUXT
    {
      path: '/',
      name: 'home',
      component: () =>
        import(/* webpackChunkName: "admin" */ './views/Home.vue'),
    },
    {
      path: '/admin/stats',
      name: 'stats',
      component: () =>
        import(/* webpackChunkName: "admin" */ './views/Stats.vue'),
      meta: {
        requiresAdmin: true,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/admin/matchtest',
      name: 'matchtest',
      component: () =>
        import(/* webpackChunkName: "admin" */ './views/MatchTest.vue'),
      meta: {
        requiresAdmin: true,
        hideItemMatchForm: true,
      },
    },
    {
      path: '/browse',
      name: 'browse',
      component: () =>
        import(/* webpackChunkName: "browse" */ './views/Browse.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import(/* webpackChunkName: "faq" */ './views/Faq.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    {
      path: '/forgot_password',
      name: 'forgotPassword',
      component: () =>
        import(
          /* webpackChunkName: "forgotPassword" */ './views/ForgotPassword.vue'
        ),
      meta: {},
    },
    {
      path: '/forgot_username',
      name: 'forgotUsername',
      component: () =>
        import(
          /* webpackChunkName: "forgotUsername" */ './views/ForgotUsername.vue'
        ),
      meta: {},
    },
    {
      path: '/login',
      name: 'login',
      component: () =>
        import(/* webpackChunkName: "login" */ './views/Login.vue'),
      meta: {
        hideItemMatchForm: true,
      },
      props: (route) => ({ redirect: route.query.redirect }),
    },
    {
      path: '/notauthorized',
      name: 'notAuthorized',
      component: () =>
        import(
          /* webpackChunkName: "notAuthorized" */ './views/NotAuthorized.vue'
        ),
      meta: {},
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () =>
        import(/* webpackChunkName: "termsPrivacy" */ './views/Privacy.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: () =>
        import(/* webpackChunkName: "profile" */ './views/Profile.vue'),
      meta: {},
    },
    {
      path: '/my_profile',
      name: 'myProfile',
      beforeEnter: (to, from, next) => {
        store.dispatch('GET_USER').then(() => {
          // the above state is not available here, since it
          // it is resolved asynchronously in the store action
          const { username } = store.getters.user;
          next(`/profile/${username}`);
        });
      },
      meta: { requiresAuth: true },
    },
    {
      path: '/release',
      name: 'release',
      component: () =>
        import(/* webpackChunkName: "release" */ './views/Release.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    {
      path: '/terms',
      name: 'terms',
      component: () =>
        import(/* webpackChunkName: "termsPrivacy" */ './views/Terms.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    {
      path: '/404',
      name: 'notFound',
      component: () =>
        import(/* webpackChunkName: "notFound" */ './views/NotFound.vue'),
      beforeEnter: (to, from, next) => {
        if (Sentry) {
          Sentry.captureMessage(`404 Error Not Found - ${to.redirectedFrom}`);
        }
        next();
      },
      meta: {},
    },
    { path: '*', redirect: '/404' },
    {
      path: '/register',
      name: 'register',
      component: () =>
        import(/* webpackChunkName: "register" */ './views/Register.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    // NOT DONE
    {
      path: '/match',
      name: 'privateMatch',
      component: () =>
        import(/* webpackChunkName: "match" */ './views/Match.vue'),
      meta: {
        requiresAuth: true,
      },
      beforeEnter: (to, from, next) => {
        // eslint-disable-next-line camelcase
        if (!to.query?.want_item_id) {
          next('/');
        } else {
          next();
        }
      },
      props: (route) => ({
        wantItemId: route.query.want_item_id,
      }),
    },
    {
      path: '/my_user_details',
      name: 'myUserDetails',
      beforeEnter: (to, from, next) => {
        store.dispatch('GET_USER').then(() => {
          // the above state is not available here, since it
          // it is resolved asynchronously in the store action
          const { username } = store.getters.user;
          next(`/profile/${username}#user_details`);
        });
      },
      meta: { requiresAuth: true },
    },
    {
      path: '/public_match',
      name: 'publicMatch',
      component: () =>
        import(/* webpackChunkName: "match" */ './views/Match.vue'),
      meta: {},
      beforeEnter: (to, from, next) => {
        // If query is missing, redirect
        // eslint-disable-next-line camelcase
        if (
          !to.query?.want_item_id ||
          !to.query?.size ||
          !to.query?.have_item_id
        ) {
          next('/');
        } else {
          next();
        }
      },
      props: (route) => ({
        wantItemId: route.query.want_item_id,
        size: route.query.size,
        haveItemId: route.query.have_item_id,
      }),
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: () =>
        import(/* webpackChunkName: "recommend" */ './views/Recommend.vue'),
      meta: {
        hideItemMatchForm: true,
      },
    },
    {
      path: '/reset_password',
      name: 'reset_password',
      component: () =>
        import(
          /* webpackChunkName: "reset_password" */ './views/ResetPassword.vue'
        ),
      meta: {},
    },
    {
      path: '/sales',
      name: 'sales',
      component: () =>
        import(/* webpackChunkName: "sales" */ './views/Sales.vue'),
      meta: {},
    },
    {
      path: '/shoe/:shoe_brand',
      redirect: '/shoes/:shoe_brand',
    },
    {
      path: '/shoes/:shoe_brand',
      name: 'brand',
      component: () =>
        import(/* webpackChunkName: "brand" */ './views/Brand.vue'),
      meta: {},
    },
    {
      path: '/shoe/:shoe_brand/:shoe_model',
      redirect: '/shoes/:shoe_brand/:shoe_model',
    },
    {
      path: '/shoes/:shoe_brand/:shoe_model',
      name: 'shoe',
      component: () =>
        import(/* webpackChunkName: "shoe" */ './views/Shoe.vue'),
      meta: {},
    },
  ],
  // Scroll behavior
  scrollBehavior(to, from, savedPosition) {
    if (to.hash && !to.hash.includes('access_token')) {
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

// Loading
router.beforeEach((to, from, next) => {
  if (to.name) {
    store.commit('STATE_INIT_LOADING');
  }
  next();
});

// Authentication Guard
router.beforeEach((to, from, next) => {
  // User is not authenticated and should be
  if (
    (to.meta.requiresAuth || to.meta.requiresAdmin) &&
    !store.getters.isAuthenticated
  ) {
    next({ name: 'login', query: { redirect: to.path } });
  } else if (store.getters.isAuthenticated) {
    // Get user info in state
    store.dispatch('GET_USER').then(() => {
      next();
    });
  } else {
    next();
  }
});

router.afterEach(() => {
  store.commit('STATE_INIT_DONE');
});

export default router;
