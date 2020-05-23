<template>
  <div class="modal" :class="{ 'is-active': show }">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card" :class="modalSize">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    modalSize: {
      type: String,
      default: '',
    },
  },
  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<style lang="scss">
@media screen and (min-width: 769px) {
  .modal-card.medium {
    width: 710px;
  }
}
@media screen and (min-width: 769px) {
  .modal-card.small {
    width: 510px;
  }
}
.modal-card {
  overflow-y: auto;
}
</style>
