<template>
  <div>
    <div v-if="loadingComponent" class="columns">
      <div class="column">
        <div class="container">
          <span class="has-text-grey">Loading<span class="loading"></span></span>
        </div>
      </div>
    </div>
    <div v-if="failedToLoad" class="columns">
      <div class="column">
        <div class="container">
          <span class="has-text-grey">Error loading this part of the page.</span>
        </div>
      </div>
    </div>
    <slot v-if="!loadingComponent && !failedToLoad" />
  </div>
</template>

<script>
export default {
  name: 'ComponentLoader',
  props: {
    loadingComponent: {
      type: Boolean,
      default: true,
    },
    failedToLoad: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped lang="scss"></style>
