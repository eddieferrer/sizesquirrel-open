<template>
  <div
    v-show="contextFlashMessage.message"
    :class="'level box is-marginless ' + contextFlashMessage.class"
  >
    <span class="message">{{ contextFlashMessage.message }}</span>
    <a
      class="dismiss has-text-dark is-size-4 is-pulled-right"
      type="button"
      @click.prevent.stop="removeStickyAlert"
      >&times;</a
    >
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'FlashMessage',
  computed: {
    ...mapGetters(['contextFlashMessage']),
  },
  watch: {
    $route() {
      this.checkURL();
    },
  },
  created() {
    this.checkURL();
  },
  methods: {
    // TODO add messages based on last login here
    checkURL() {
      let message = '';
      let flashClass = '';

      if (this.getParameterByName('deleted')) {
        flashClass = 'has-background-danger';
        message = 'Your account has been deleted.';
      }
      if (this.getParameterByName('changed')) {
        flashClass = 'has-background-success';
        message = 'Account details changed. This is your new profile page.';
      }
      if (this.getParameterByName('loginagain')) {
        flashClass = 'has-background-danger';
        message = 'Please login again.';
      }

      if (message === '' && flashClass === '') {
        this.removeStickyAlert();
      } else {
        this.$store.dispatch('SHOW_FLASH_MESSAGE', {
          class: flashClass,
          message,
        });
      }
    },
    removeStickyAlert() {
      this.$store.dispatch('RESET_FLASH_MESSAGE');
    },
  },
};
</script>

<style scoped lang="scss">
$white: rgba(255, 255, 255, 1);
$purple: #3e3895;
$lightpurple: #7872c5;

.dismiss {
  text-decoration: none !important;
  margin-top: -5px;
}
</style>
