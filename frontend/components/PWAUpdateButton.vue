<template>
  <div
    v-if="updateExists"
    class="level box is-marginless has-background-warning"
  >
    <div class="container is-fluid">
      <div class="columns">
        <div class="column">
          <span class="message">A new version of the site is available!</span>
        </div>
        <div class="column is-narrow">
          <button
            class="button is-info"
            type="button"
            title="Ascending"
            @click="refreshApp"
          >
            Click to update
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// TODO possibly not needed anymore?

export default {
  name: 'PWAUpdateButton',
  data() {
    return {
      refreshing: false,
      worker: null,
      updateExists: false,
    };
  },
  created() {
    // eslint-disable-next-line nuxt/no-globals-in-created
    document.addEventListener('swUpdated', this.showRefreshUI, { once: true });
    // Check for support of navigator service worker browser API
    if (navigator.serviceWorker) {
      navigator.serviceWorker.addEventListener('controllerchange', () => {
        if (this.refreshing) return;
        this.refreshing = true;
        // eslint-disable-next-line nuxt/no-globals-in-created
        window.location.reload();
      });
    }
  },
  methods: {
    refreshApp() {
      this.updateExists = false;
      if (!this.worker) {
        return;
      }
      this.worker.postMessage({ action: 'skipWaiting' });
    },
    showRefreshUI(e) {
      if (e.detail) {
        this.worker = e.detail;
        this.updateExists = true;
      }
    },
  },
};
</script>

<style scoped lang="scss">
button {
  margin-top: -8px;
}
</style>
