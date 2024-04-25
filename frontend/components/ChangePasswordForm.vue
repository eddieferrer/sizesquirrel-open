<template>
  <div class="columns">
    <div v-if="status == 'success'" class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">Thank You</h2>
      <h5 class="is-size-5 has-text-centered">Password reset</h5>
      <hr />
      <p>{{ message }}</p>
      <NuxtLink :to="'login'">Login with your new password</NuxtLink>
    </div>
    <div v-if="status !== 'success'" class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        Change Password
      </h2>
      <h5 class="is-size-5 has-text-centered">Enter your new password</h5>
      <hr />
      <form @submit.prevent="resetPassword">
        <div v-if="password_change_error.general" class="columns">
          <div class="column">
            <div class="level box is-marginless has-background-danger">
              <span class="message">{{
                password_change_error.general | capitalize
              }}</span>
            </div>
          </div>
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
              :class="{ 'is-danger': password_change_error.password != '' }"
            />
          </div>
          <p v-if="password_change_error.password != ''" class="help is-danger">
            {{ password_change_error.password | capitalize }}
          </p>
        </div>

        <div class="field">
          <label class="label">Confirm Password</label>
          <div class="control">
            <input
              v-model="confirmPassword"
              class="input"
              type="password"
              name="confirmPassword"
              required
              :class="{
                'is-danger': password_change_error.confirmPassword != '',
              }"
            />
          </div>
          <p
            v-if="password_change_error.confirmPassword != ''"
            class="help is-danger"
          >
            {{ password_change_error.confirmPassword | capitalize }}
          </p>
        </div>

        <div class="control">
          <button
            id="send_form"
            :disabled="isFormSubmitting"
            type="submit"
            name="button"
            class="button is-info is-pulled-right"
          >
            Change Password<span v-if="isFormSubmitting" class="loading"></span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { capitalize } from '@/filters';

export default {
  name: 'ChangePasswordForm',
  components: {},
  filters: {
    capitalize,
  },
  props: [],
  data() {
    return {
      status: '',
      message: '',
      password: '',
      confirmPassword: '',
      password_change_error: {
        general: '',
        password: '',
        confirmPassword: '',
      },
      isFormSubmitting: false,
    };
  },
  methods: {
    resetPassword() {
      this.isFormSubmitting = true;
      const vm = this;
      vm.password_change_error = {
        general: '',
        password: '',
        confirmPassword: '',
      };
      vm.status = '';

      this.$store
        .dispatch('RESET_PASSWORD', {
          password: vm.password,
          confirmPassword: vm.confirmPassword,
          token: vm.getParameterByName('token'),
        })
        .then((response) => {
          if (response.data.status === 'success') {
            vm.status = 'success';
            vm.message = response.data.message;
          }
          if (response.data.status === 'error') {
            vm.status = 'error';
            vm.password_change_error.general = response.data.message.general;
            vm.password_change_error.password = response.data.message.password;
            vm.password_change_error.confirmPassword =
              response.data.message.confirmPassword;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.log(error);
        })
        .finally(() => {
          this.isFormSubmitting = false;
        });
    },
  },
};
</script>

<style scoped>
form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
