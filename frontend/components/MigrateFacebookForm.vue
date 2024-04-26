<template>
  <div>
    <div class="columns is-centered">
      <div class="column is-two-thirds-desktop">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Migrate SizeSquirrel Facebook Account
        </h2>
        <h5 class="is-size-5 has-text-centered">
          Enter your email address to unlink your SizeSquirrel account from
          Facebook
        </h5>
        <hr />
        <div>
          <p>
            <strong>Why can't I log in with Facebook anymore?</strong><br />
            Unfortunately Facebook has implemented some policy changes that
            prevent sites like SizeSquirrel from using your Facebook email and
            name to create accounts and log you in.
          </p>
          <p>
            <strong>What now?</strong><br />
            We'll need to migrate your account to use a SizeSquirrel username
            and password combination to log in to the site. Your profile and all
            your shoes will be saved, but you'll now use your username and a new
            password to log in instead of the Facebook login button.
            <br />
            <br />
            Please fill out the form below with your email address. It must be
            the same email address associated with your Facebook account. We'll
            send you an email with instructions on how to set a new password for
            your account. You'll only have to do this process once.
          </p>
          <p>
            Sorry for the inconvenience and thank you for your understanding. It
            is truly out of my hands. <br />- <strong>Eddie</strong>
          </p>
        </div>
        <form v-if="status !== 'success'" @submit.prevent="migrateFromFacebook">
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input
                v-model="email"
                class="input"
                type="email"
                name="email"
                required
                :class="{ 'is-danger': migrate_facebook_error != '' }"
              />
            </div>
            <p v-if="migrate_facebook_error != ''" class="help is-danger">
              {{ migrate_facebook_error }}
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
              Send Email<span v-if="isFormSubmitting" class="loading"></span>
            </button>
          </div>
        </form>
        <div v-if="status == 'success'" class="columns is-centered">
          <div class="column is-two-thirds-desktop">
            <h2 class="is-size-4 has-text-centered has-text-primary">
              Thank You
            </h2>
            <h5 class="is-size-5 has-text-centered">Email Sent</h5>
            <hr />
            <p>{{ message }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MigrateFacebookForm',
  components: {},
  props: [],
  data() {
    return {
      status: '',
      email: '',
      message: '',
      migrate_facebook_error: '',
      isFormSubmitting: false,
    };
  },
  methods: {
    migrateFromFacebook() {
      this.isFormSubmitting = true;
      const vm = this;
      vm.migrate_facebook_error = '';
      vm.status = '';
      this.$store
        .dispatch('MIGRATE_FACEBOOK', {
          email: vm.email,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            vm.status = 'success';
            vm.message = response.data.message;
          }
          if (response.data.status === 'error') {
            vm.status = 'error';
            vm.migrate_facebook_error = response.data.message;
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

p,
h5 {
  margin-bottom: 1em;
}

h5 {
  font-size: 1.25em;
}
</style>
