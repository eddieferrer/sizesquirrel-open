<template>
  <div v-cloak class="columns">
    <div class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">{{ brand.name | titleCase }}</h2>
      <h5 class="is-size-5 has-text-centered">All of the {{ brand.name | titleCase }} shoes</h5>
      <hr />
      <BrandItems v-cloak :target="'brand/' + brand.id"></BrandItems>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';
import store from '@/store/store';

import BrandItems from '@/components/BrandItems';

const getData = (to, from, next) => {
  store
    .dispatch('INITIALIZE_APP', {
      url: to.fullPath,
    })
    .then(() => {
      if (store.getters.hasBrand) {
        next();
      } else {
        next(`/404`);
      }
    })
    .catch(() => {
      store.commit('STATE_INIT_ERROR');
    });
};

export default {
  name: 'Brand',
  components: {
    BrandItems,
  },
  filters: {
    titleCase,
  },
  beforeRouteEnter(to, from, next) {
    getData(to, from, next);
  },
  beforeRouteUpdate(to, from, next) {
    getData(to, from, next);
  },
  metaInfo() {
    return {
      // title will be injected into parent titleTemplate
      title: `${this.brandName} Shoes`,
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: `${this.brandName} Shoes | SizeSquirrel`,
        },
      ],
    };
  },
  computed: {
    ...mapGetters(['brand']),
    brandName() {
      return this.$options.filters.titleCase(this.brand.name);
    },
  },
};
</script>
