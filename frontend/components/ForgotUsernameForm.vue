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
          Forgot Username
        </h2>
        <h5 class="is-size-5 has-text-centered">
          Enter the email address associated with your account
        </h5>
        <hr />
        <form @submit.prevent="forgotUsername">
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input
                v-model="email"
                class="input"
                type="email"
                name="email"
                required
                :class="{ 'is-danger': username_request_error_email != '' }"
              />
            </div>
            <p v-if="username_request_error_email != ''" class="help is-danger">
              {{ username_request_error_email }}
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
              Send My Username<span
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
  name: 'ForgotUsernameForm',
  components: {},
  props: [],
  data() {
    return {
      status: '',
      email: '',
      message: '',
      username_request_error_email: '',
      isFormSubmitting: false,
    };
  },
  methods: {
    forgotUsername() {
      this.isFormSubmitting = true;
      const vm = this;
      vm.username_request_error_email = '';
      vm.status = '';
      this.$store
        .dispatch('FORGOT_USERNAME', {
          email: vm.email,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            vm.status = 'success';
            vm.message = response.data.message;
          }
          if (response.data.status === 'error') {
            vm.status = 'error';
            vm.username_request_error_email = response.data.message;
          }
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
  width: 400px;
  margin: 0 auto;
}
</style>
