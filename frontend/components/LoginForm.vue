<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">Log In</h2>
      <h5 class="is-size-5 has-text-centered">Hello again</h5>
      <hr />
      <div class="columns">
        <div class="column is-two-thirds-desktop">
          <form class="user_login_form" @submit.prevent="login">
            <p class="is-size-6">Already have an account? Log in below.</p>
            <p class="has-text-grey">
              <em>Using your Facebook account</em>
            </p>
            <a
              class="button is-normal is-info"
              @click="openFbLoginDialog('login', redirect)"
            >
              <span id="fbicon" class="icon is-medium">
                <img src="/images/icons/facebook32.png" alt />
              </span>
              <span>Log in using Facebook</span>
            </a>
            <hr />
            <p class="has-text-grey">
              <em>Using your SizeSquirrel username and password</em>
            </p>
            <div v-if="login_error" class="columns">
              <div class="column">
                <div class="level box is-marginless has-background-danger">
                  <span class="message">{{ login_error | capitalize }}</span>
                </div>
              </div>
            </div>
            <div class="columns">
              <div class="column">
                <div class="field">
                  <label class="label">Username</label>
                  <div class="control">
                    <input
                      v-model="username"
                      type="text"
                      class="input"
                      name="username"
                      required
                      :class="{ 'is-danger': login_error != '' }"
                    />
                  </div>
                  <p class="help is-primary">
                    <NuxtLink to="/forgot_username/"
                      >Forgot your username?</NuxtLink
                    >
                  </p>
                </div>
                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input
                      v-model="password"
                      class="input"
                      type="password"
                      name="password"
                      required
                      :class="{ 'is-danger': login_error != '' }"
                    />
                  </div>
                  <p class="help is-primary">
                    <NuxtLink to="/forgot_password/"
                      >Forgot your password?</NuxtLink
                    >
                  </p>
                </div>
              </div>
            </div>
            <div class="columns">
              <div class="column">
                <button
                  type="submit"
                  name="button"
                  class="button is-info is-pulled-right"
                  :disabled="isFormSubmitting"
                >
                  Log In<span v-if="isFormSubmitting" class="loading"></span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { capitalize } from '@/filters';

export default {
  name: 'LoginForm',
  components: {},
  filters: {
    capitalize,
  },
  props: {
    redirect: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      username: '',
      password: '',
      login_error: '',
      isFormSubmitting: false,
    };
  },
  methods: {
    login() {
      this.isFormSubmitting = true;
      this.login_error = '';
      const { username, password } = this;
      this.$store
        .dispatch('AUTH_REQUEST', { username, password })
        .then(() => {
          const nextRoute = this.redirect || '/my_profile/';
          this.$router.push({ path: nextRoute }).catch(() => {});
        })
        .catch((error) => {
          this.login_error = error.response.data.message || error;
        })
        .finally(() => {
          this.isFormSubmitting = false;
        });
    },
  },
};
</script>

<style scoped>
.button span.icon#fbicon {
  margin-right: 0.45em;
  margin-left: 0.05em;
}
form {
  width: 350px;
  margin: 0 auto;
}
p {
  margin-bottom: 1em;
}
</style>
