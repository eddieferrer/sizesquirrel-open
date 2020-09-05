<!-- eslint-disable vue/no-v-html -->
<script>
// function recursivelyRemoveFill(el) {
//   if (!el) {
//     return;
//   }
//   el.removeAttribute('fill');
//   [].slice.call(el.children).forEach((child) => {
//     recursivelyRemoveFill(child);
//   });
// }
export default {
  name: 'SvgIcon',
  props: {
    icon: {
      type: String,
      default: null,
    },
    hasFill: {
      type: Boolean,
      default: false,
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
      // if (this.hasFill) {
      //   // recursively remove all fill attribute of element and its nested children
      //   recursivelyRemoveFill(svgElement);
      // }
      // set width and height relative to font size
      // if growByHeight is true, height set to 1em else width set to 1em and remaining is calculated based on widthToHeight ratio
      if (this.growByHeight) {
        svgElement.setAttribute('height', '1em');
        svgElement.setAttribute('width', `${widthToHeight}em`);
      } else {
        svgElement.setAttribute('width', '1em');
        svgElement.setAttribute('height', `${1 / widthToHeight}em`);
      }
      svgElement.classList.add('svg-class');
    }
  },
};
</script>

<template>
  <div
    class="svg-container"
    v-html="require(`!html-loader!./../scss/vendor/foundation-icons/svgs/${icon}.svg`)"
  ></div>
</template>

<style lang="scss">
.svg-container {
  display: inline-flex;
  vertical-align: middle;
  margin-top: -0.2em;
}
.svg-class {
  vertical-align: middle;
}
</style>
