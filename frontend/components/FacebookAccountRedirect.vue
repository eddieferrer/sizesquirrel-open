<template>
  <ComponentLoader :component-state="componentState">
    <div class="columns">
      <div class="column">
        <div
          v-if="fb_login_error != ''"
          class="level box is-marginless has-background-danger-dark"
        >
          <span class="has-text-white">{{ fb_login_error | capitalize }}</span>
        </div>
      </div>
    </div>
  </ComponentLoader>
</template>
<script>
import ComponentLoader from '@/components/ComponentLoader';
import { capitalize } from '@/filters';

export default {
  name: 'FacebookCallback',
  filters: {
    capitalize,
  },
  components: { ComponentLoader },
  props: {
    formType: {
      type: String,
      default: '',
    },
    state: {
      type: String,
      default: '',
    },
    accessToken: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      fb_login_error: '',
      componentState: '',
    };
  },
  computed: {
    redirect() {
      try {
        return JSON.parse(decodeURIComponent(this.state)).redirect;
      } catch {
        return '';
      }
    },
  },
  mounted() {
    this.componentState = 'loading';
    const vm = this;
    if (typeof FB !== 'undefined' && window.location.hostname !== 'localhost') {
      FB.getLoginStatus(function fbGetLogin(response) {
        if (response.authResponse) {
          vm.checkLoginState(response);
        } else {
          vm.$router.push({ path: '/login/' });
        }
      });
    } else {
      vm.dispatchLogin(this.accessToken);
    }
  },
  methods: {
    navigateAfterLogin() {
      const nextRoute = this.redirect || '/my_profile/';
      this.$router.push({ path: nextRoute });
    },
    dispatchLogin(token) {
      if (this.formType === 'register') {
        this.$store
          .dispatch('FB_REGISTER', { accessToken: token })
          .then(() => {
            this.navigateAfterLogin();
          })
          .catch((error) => {
            this.fb_login_error = error.response.data.message || error;
            this.componentState = 'error';
          });
      } else {
        this.$store
          .dispatch('AUTH_FB_LOGIN', { accessToken: token })
          .then(() => {
            this.navigateAfterLogin();
          })
          .catch((error) => {
            this.fb_login_error = error.response.data.message || error;
            this.componentState = 'error';
          });
      }
    },
    checkLoginState(response) {
      if (response.status === 'connected') {
        this.dispatchLogin(response.authResponse.accessToken);
      } else if (response.status === 'not_authorized') {
        // the user is logged in to Facebook,
        // but has not authenticated your app
        this.fb_login_error = 'Not authorized on Facebook';
      } else {
        // the user isn't logged in to Facebook.
        this.fb_login_error = 'Facebook Error';
      }
    },
  },
};
</script>
