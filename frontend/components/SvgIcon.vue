<template>
  <!-- eslint-disable vue/no-v-html -->
  <div
    class="svg-container"
    v-html="
      require(`!html-loader!./../assets/scss/vendor/foundation-icons/svgs/${icon}.svg`)
    "
  ></div>
</template>

<script>
export default {
  name: 'SvgIcon',
  props: {
    icon: {
      type: String,
      default: null,
    },
    growByHeight: {
      type: Boolean,
      default: true,
    },
  },
  mounted() {
    if (this.$el.firstElementChild.nodeName === 'svg') {
      const svgElement = this.$el.firstElementChild;
      // use `viewBox` attribute to get the svg's inherent width and height
      const viewBox = svgElement
        .getAttribute('viewBox')
        .split(' ')
        .map((n) => Number(n));
      const widthToHeight = (viewBox[2] / viewBox[3]).toFixed(2);
      // set width and height relative to font size
      // if growByHeight is true, height set to 1em else width set to 1em and remaining is calculated based on widthToHeight ratio
      if (this.growByHeight) {
        svgElement.setAttribute('height', '1em');
        svgElement.setAttribute('width', `${widthToHeight}em`);
      } else {
        svgElement.setAttribute('width', '1em');
        svgElement.setAttribute('height', `${1 / widthToHeight}em`);
      }
    }
  },
};
</script>

<style lang="scss">
.svg-container {
  display: inline-flex;
  vertical-align: middle;
  margin-top: -0.2em;
}
</style>
