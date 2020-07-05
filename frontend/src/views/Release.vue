<template>
  <div>
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">Release Information</h2>
        <hr />
      </div>
    </div>
    <div class="columns is-centered">
      <div class="column is-one-quarter-desktop">
        <p>
          <strong>Current Branch</strong>
        </p>
        <p>
          {{ gitbranch }}
        </p>
      </div>
      <div class="column is-one-quarter-desktop">
        <p>
          <strong>Current Version</strong>
        </p>
        <p>
          {{ version }}
        </p>
      </div>
      <div class="column">
        <p>
          <strong>Current Hash</strong>
        </p>
        <p>
          {{ hash }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Release',
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Release',
  },
  data() {
    return {
      gitbranch: process.env.VUE_APP_GITBRANCH,
      version: process.env.VUE_APP_GITVERSION,
      hash: process.env.VUE_APP_GITHASH,
    };
  },
};
</script>
