import Vue from 'vue';
import VLazyImage from 'v-lazy-image/v2/v-lazy-image.es';

const components = { VLazyImage };

Object.entries(components).forEach(([name, component]) => {
  Vue.component(name, component);
});
