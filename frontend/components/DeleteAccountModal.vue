<template>
  <Modal :modal-size="modalSize" :show="show" @close="close">
    <header class="modal-card-head">
      <p class="modal-card-title">Delete Account</p>
      <span
        class="close-button is-size-4"
        aria-label="close"
        @click.prevent.stop="close"
        >&#215;</span
      >
    </header>
    <section class="modal-card-body">
      <p>
        Are you sure you want to delete your account? By hitting the "Yes I am
        sure" button, all your account information will be deleted, including
        all your shoes.
        <br />
        <br />
        <strong>This action cannot be undone.</strong>
      </p>
    </section>
    <section class="modal-card-body">
      <button class="button is-pulled-left" @click.prevent.stop="close">
        Cancel
      </button>
      <button
        class="button is-danger is-pulled-right"
        :disabled="isFormSubmitting"
        @click.prevent.stop="deleteUser"
      >
        Yes, I am sure<span v-if="isFormSubmitting" class="loading"></span>
      </button>
    </section>
  </Modal>
</template>

<script>
import Modal from '@/components/Modal';

export default {
  name: 'DeleteAccountModal',
  components: { Modal },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    userId: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      modalSize: 'small',
      isFormSubmitting: false,
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    deleteUser() {
      this.isFormSubmitting = true;

      const deleteAccountModalComponent = this;
      this.$store
        .dispatch('DELETE_ACCOUNT', deleteAccountModalComponent.userId)
        .then((response) => {
          if (response.data.status === 'success') {
            deleteAccountModalComponent.$emit('close');
            const endUrl = response.data.new_url;
            this.$store.dispatch('AUTH_LOGOUT').then(() => {
              window.location.href = endUrl;
            });
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
