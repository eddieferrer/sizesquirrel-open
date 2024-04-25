<template>
  <div>
    <div v-if="status == 'success'" class="columns is-centered">
      <div class="column is-two-thirds-desktop">
        <h2 class="is-size-4 has-text-centered has-text-primary">Thank You</h2>
        <h5 class="is-size-5 has-text-centered">Email Sent</h5>
        <hr />
        <p>{{ message }}</p>
      </div>
    </div>
    <div v-if="status !== 'success'" class="columns is-centered">
      <div class="column is-two-thirds-desktop">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Forgot Password
        </h2>
        <h5 class="is-size-5 has-text-centered">
          Enter your email address to reset your password
        </h5>
        <hr />
        <form @submit.prevent="forgotPassword">
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input
                v-model="email"
                class="input"
                type="email"
                name="email"
                required
                :class="{ 'is-danger': password_request_error != '' }"
              />
            </div>
            <p v-if="password_request_error != ''" class="help is-danger">
              {{ password_request_error }}
            </p>
          </div>
          <div class="control">
            <button
              id="send_form"
              class="button is-info is-pulled-right"
              type="submit"
              name="button"
              :disabled="isFormSubmitting"
            >
              Send Password Reset Email<span
                v-if="isFormSubmitting"
                class="loading"
              ></span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ForgotPasswordForm',
  components: {},
  props: [],
  data() {
    return {
      status: '',
      email: '',
      message: '',
      password_request_error: '',
      isFormSubmitting: false,
    };
  },
  methods: {
    forgotPassword() {
      this.isFormSubmitting = true;
      const vm = this;
      vm.password_request_error = '';
      vm.status = '';
      this.$store
        .dispatch('FORGOT_PASSWORD', {
          email: vm.email,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            vm.status = 'success';
            vm.message = response.data.message;
          }
          if (response.data.status === 'error') {
            vm.status = 'error';
            vm.password_request_error = response.data.message;
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
