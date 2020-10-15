<template>
  <div>
    <div v-if="componentState == 'loading'" class="columns">
      <div class="column">
        <div class="container">
          <span class="has-text-grey">Loading<span class="loading"></span></span>
        </div>
      </div>
    </div>
    <div v-if="componentState == 'error'" class="columns">
      <div class="column">
        <div class="container">
          <span class="has-text-grey">Error loading this part of the page.</span>
        </div>
      </div>
    </div>
    <slot v-if="componentState == 'done'" />
  </div>
</template>

<script>
export default {
  name: 'ComponentLoader',
  props: {
    // State of the component
    // One of three states:
    // 'loading', 'done', 'error'
    componentState: {
      type: String,
      default: 'loading',
    },
  },
};
</script>

<style scoped lang="scss"></style>
