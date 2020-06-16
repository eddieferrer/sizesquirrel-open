<template>
  <Modal :modal-size="modalSize" :show="show" @close="close">
    <header class="modal-card-head">
      <p class="modal-card-title">Delete Shoe</p>
      <span class="close-button is-size-4" aria-label="close" @click.prevent.stop="close"
        >&#215;</span
      >
    </header>
    <section class="modal-card-body">
      <p>
        Are you sure you want to remove
        <span class="is-capitalized has-text-weight-bold">{{ item.item.brand.name }}&nbsp;</span>
        <span class="is-capitalized has-text-weight-bold">{{ item.item.model }}</span> from your
        profile?
      </p>
    </section>
    <section class="modal-card-body">
      <button class="button is-pulled-left" @click.prevent.stop="close">Cancel</button>
      <button
        class="button is-danger is-pulled-right"
        :disabled="isFormSubmitting"
        @click.prevent.stop="deleteItem(item.id)"
      >
        Delete Shoe<span v-if="isFormSubmitting" class="loading"></span>
      </button>
    </section>
  </Modal>
</template>

<script>
import Modal from './Modal';

export default {
  name: 'ConfirmDeleteModal',
  components: { Modal },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    item: {
      type: Object,
      default() {
        return {};
      },
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
    deleteItem(itemid) {
      this.isFormSubmitting = true;
      const confirmDeleteModalComponent = this;
      this.$store
        .dispatch('REMOVE_PROFILE_ITEM', itemid)
        .then(response => {
          if (response.data.status === 'success') {
            confirmDeleteModalComponent.$store.dispatch('SHOW_FLASH_MESSAGE', {
              class: 'has-background-success',
              message: response.data.message,
            });
            window.scrollTo(0, 0);
            confirmDeleteModalComponent.$emit('close');
          }
        })
        .catch(error => {
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

<style scoped></style>
