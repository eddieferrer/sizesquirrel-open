<template>
  <Modal :modal-size="modalSize" :show="show" @close="close">
    <form
      id="change_password_form"
      class="modal_form"
      @submit.prevent="changePassword"
    >
      <header class="modal-card-head">
        <p class="modal-card-title">Change Password</p>
        <span
          class="close-button is-size-4"
          aria-label="close"
          @click.prevent.stop="close"
          >&#215;</span
        >
      </header>
      <section class="modal-card-body">
        <div v-if="formErrors && showAlert" class="columns">
          <div class="column">
            <div class="level box is-marginless has-background-danger">
              <span class="has-text-white"
                >There was an error changing your password.</span
              >
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column">
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal"
                >Current Password</label
              >
              <div class="control">
                <input
                  v-model="current_password"
                  class="input"
                  type="password"
                  name="current_password"
                  required
                />
              </div>
              <p v-if="error_current_password != ''" class="help is-danger">
                {{ error_current_password }}
              </p>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column">
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal"
                >New Password</label
              >
              <div class="control">
                <input
                  v-model="new_password"
                  class="input"
                  type="password"
                  name="new_password"
                  required
                />
              </div>
              <p v-if="error_new_password_confirm != ''" class="help is-danger">
                {{ error_new_password_confirm }}
              </p>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column">
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal"
                >Confirm New Password</label
              >
              <div class="control">
                <input
                  v-model="new_password_confirm"
                  class="input"
                  type="password"
                  name="new_password_confirm"
                  required
                />
              </div>
              <p v-if="error_new_password_confirm != ''" class="help is-danger">
                {{ error_new_password_confirm }}
              </p>
            </div>
          </div>
        </div>
      </section>
      <section class="modal-card-body">
        <button
          type="submit"
          class="button is-pulled-right is-info"
          :disabled="isFormSubmitting"
        >
          Change Password<span v-if="isFormSubmitting" class="loading"></span>
        </button>
        <button class="button is-pulled-left" @click.prevent.stop="close">
          Cancel
        </button>
      </section>
    </form>
  </Modal>
</template>

<script>
import Modal from '@/components/Modal';

export default {
  name: 'ChangePasswordModal',
  components: { Modal },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      modalSize: 'small',
      current_password: '',
      new_password: '',
      new_password_confirm: '',
      error_current_password: '',
      error_new_password_confirm: '',
      formErrors: false,
      showAlert: false,
      isFormSubmitting: false,
    };
  },
  methods: {
    close() {
      this.formErrors = false;
      this.$emit('close');
    },
    changePassword() {
      this.isFormSubmitting = true;
      const changePasswordModalComponent = this;
      changePasswordModalComponent.formErrors = false;
      changePasswordModalComponent.showAlert = true;

      this.$store
        .dispatch('CHANGE_PASSWORD', {
          currentPassword: changePasswordModalComponent.current_password,
          newPassword: changePasswordModalComponent.new_password,
          newPasswordConfirm: changePasswordModalComponent.new_password_confirm,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            changePasswordModalComponent.$emit('close');
            changePasswordModalComponent.$store.dispatch('SHOW_FLASH_MESSAGE', {
              class: 'has-background-success',
              message: response.data.message,
            });
            window.scrollTo(0, 0);
            changePasswordModalComponent.current_password = '';
            changePasswordModalComponent.new_password = '';
            changePasswordModalComponent.new_password_confirm = '';
            changePasswordModalComponent.error_current_password = '';
            changePasswordModalComponent.error_new_password_confirm = '';
            changePasswordModalComponent.formErrors = false;
            changePasswordModalComponent.showAlert = false;
          }
          if (response.data.status === 'error') {
            changePasswordModalComponent.error_current_password =
              response.data.error_current_password;
            changePasswordModalComponent.error_new_password_confirm =
              response.data.error_new_password_confirm;
            changePasswordModalComponent.formErrors = true;
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
