<template>
  <div v-cloak class="columns">
    <div class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        {{ brand.name | titleCase }}
      </h2>
      <h5 class="is-size-5 has-text-centered">
        All of the {{ brand.name | titleCase }} shoes
      </h5>
      <hr />
      <BrandItems v-cloak :target="'brand/' + brand.id"></BrandItems>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import BrandItems from '@/components/BrandItems';

export default {
  name: 'Brand',
  components: {
    BrandItems,
  },
  filters: {
    titleCase,
  },
  layout: 'homepageForm',
  asyncData(context) {
    return context.store
      .dispatch('INITIALIZE_APP', {
        url: context.route.fullPath,
      })
      .then(() => {
        if (!context.store.getters.hasBrand) {
          context.redirect(`/404`);
        }
      })
      .catch(() => {
        context.store.commit('STATE_INIT_ERROR');
      });
  },
  head() {
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
