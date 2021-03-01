<template>
  <div class="tile is-ancestor">
    <div class="tile is-6 is-parent is-vertical">
      <div class="tile is-child">
        <slot name="index0"></slot>
      </div>
      <div class="tile is-child">
        <slot name="index2"></slot>
      </div>
    </div>
    <div class="tile is-6 is-parent is-vertical">
      <div class="tile is-child">
        <slot name="index1"></slot>
      </div>
      <div class="tile is-child">
        <slot name="index3"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShoeTiles',
};
</script>
