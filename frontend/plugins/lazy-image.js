import Vue from 'vue';
import VLazyImage from 'v-lazy-image/v2';

const components = { VLazyImage };

Object.entries(components).forEach(([name, component]) => {
  Vue.component(name, component);
});
