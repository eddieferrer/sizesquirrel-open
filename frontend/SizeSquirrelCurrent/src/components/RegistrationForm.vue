<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">Register</h2>
      <h5 class="is-size-5 has-text-centered">It's super easy</h5>
      <hr />
      <div class="columns">
        <div class="column is-two-thirds-desktop">
          <form @submit.prevent="register">
            <p class="is-size-6">Register an account for all SizeSquirrel features.</p>
            <p class="has-text-grey">
              <em>Create an account using Facebook.</em>
            </p>
            <a class="button is-normal is-info" @click="openFbLoginDialog('register')">
              <span id="fbicon" class="icon is-medium">
                <img src="/images/icons/facebook32.png" alt />
              </span>
              <span>Register using your Facebook account</span>
            </a>
            <hr />
            <p class="has-text-grey">
              <em>Create an account with SizeSquirrel.</em>
            </p>
            <div v-if="registration_error" class="columns">
              <div class="column">
                <div class="level box is-marginless has-background-danger">
                  <span class="message">{{ registration_error | capitalize }}</span>
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
                      :class="{ 'is-danger': field_errors.username != '' }"
                    />
                  </div>
                  <p v-if="field_errors.username != ''" class="help is-danger">
                    {{ field_errors.username | capitalize }}
                  </p>
                </div>

                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input
                      v-model="password"
                      type="password"
                      class="input"
                      name="password"
                      required
                      :class="{ 'is-danger': field_errors.password != '' }"
                    />
                  </div>
                  <p v-if="field_errors.password != ''" class="help is-danger">
                    {{ field_errors.password | capitalize }}
                  </p>
                </div>

                <div class="field">
                  <label class="label">Confirm Password</label>
                  <div class="control">
                    <input
                      v-model="confirmPassword"
                      type="password"
                      class="input"
                      name="confirmPassword"
                      required
                      :class="{ 'is-danger': field_errors.confirmPassword != '' }"
                    />
                  </div>
                  <p v-if="field_errors.confirmPassword != ''" class="help is-danger">
                    {{ field_errors.confirmPassword | capitalize }}
                  </p>
                </div>

                <div class="field">
                  <label class="label">Email</label>
                  <div class="control">
                    <input
                      v-model="email"
                      type="email"
                      class="input"
                      name="email"
                      required
                      :class="{ 'is-danger': field_errors.email != '' }"
                    />
                  </div>
                  <p v-if="field_errors.email != ''" class="help is-danger">
                    {{ field_errors.email | capitalize }}
                  </p>
                </div>

                <div class="field">
                  <label class="label">First Name</label>
                  <div class="control">
                    <input
                      v-model="firstName"
                      type="text"
                      class="input"
                      name="firstName"
                      required
                      :class="{ 'is-danger': field_errors.firstName != '' }"
                    />
                  </div>
                  <p v-if="field_errors.firstName != ''" class="help is-danger">
                    {{ field_errors.firstName | capitalize }}
                  </p>
                </div>

                <div class="field">
                  <label class="label">Last Name</label>
                  <div class="control">
                    <input
                      v-model="lastName"
                      type="text"
                      class="input"
                      name="lastName"
                      required
                      :class="{ 'is-danger': field_errors.lastName != '' }"
                    />
                  </div>
                  <p v-if="field_errors.lastName != ''" class="help is-danger">
                    {{ field_errors.lastName | capitalize }}
                  </p>
                </div>
              </div>
            </div>
            <div class="columns">
              <div class="column">
                <small
                  >By registering for an account you agree to our
                  <RouterLink to="/terms/">Terms Of Use</RouterLink>
                </small>
              </div>
            </div>
            <div class="columns">
              <div class="column">
                <button
                  type="submit"
                  name="button"
                  class="button is-pulled-right is-info"
                  :disabled="isFormSubmitting"
                >
                  Register<span v-if="isFormSubmitting" class="loading"></span>
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
  name: 'RegistrationForm',
  components: {},
  filters: {
    capitalize,
  },
  props: [],
  data() {
    return {
      confirmPassword: '',
      email: '',
      firstName: '',
      lastName: '',
      password: '',
      username: '',
      registration_error: '',
      field_errors: {
        confirmPassword: '',
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        username: '',
      },
      isFormSubmitting: false,
    };
  },
  methods: {
    register() {
      this.isFormSubmitting = true;
      this.registration_error = '';
      const { confirmPassword, email, firstName, lastName, password, username } = this;
      this.$store
        .dispatch('REGISTER', {
          confirmPassword,
          email,
          firstName,
          lastName,
          password,
          username,
        })
        .then((response) => {
          this.$router
            .push({
              name: 'profile',
              params: { username: response.data.username },
              query: { new: '1' },
            })
            .catch(() => {});
        })
        .catch((error) => {
          this.registration_error = 'Registration error';
          this.field_errors = error.response.data.message || error;
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
