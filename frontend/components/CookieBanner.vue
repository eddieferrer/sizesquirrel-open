<template>
  <div
    v-if="isOpen"
    class="level box is-marginless has-background-white cookie_banner"
  >
    <div class="columns">
      <div class="column is-narrow">
        <span class="is-size-3 has-text-dark">🍪</span>
      </div>
      <div class="column">
        <span class="is-size-5 has-text-dark">
          Can I use cookies for analytics? Read
          <nuxt-link class="text-link has-text-info" to="/privacy"
            >the privacy policy</nuxt-link
          >
          for more information.
        </span>
      </div>
      <div class="column is-narrow">
        <button class="button is-info is-medium" type="button" @click="accept">
          Yes, sure
        </button>
        <button class="button is-light is-medium" type="button" @click="deny">
          &times;
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { bootstrap } from 'vue-gtag';

export default {
  name: 'CookieBanner',
  data() {
    return {
      isOpen: false,
    };
  },
  created() {
    if (!this.getGDPR() === true) {
      this.isOpen = true;
    }
  },
  methods: {
    getGDPR() {
      return localStorage.getItem('GDPR:accepted', true);
    },
    accept() {
      bootstrap().then((gtag) => {
        this.isOpen = false;
        localStorage.setItem('GDPR:accepted', true);
        location.reload();
      });
    },
    deny() {
      this.isOpen = false;
      localStorage.setItem('GDPR:accepted', false);
    },
  },
};
</script>

<style scoped lang="scss">
.cookie_banner {
  position: fixed;
  bottom: 0;
  z-index: 10000;
  width: 100%;
}
</style>
