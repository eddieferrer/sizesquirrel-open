<template>
  <div>
    <NotFoundBlock v-cloak v-if="!notEmptyObject(brand) && isInitialized"></NotFoundBlock>
    <div v-if="notEmptyObject(brand)" v-cloak class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">{{ brand.name | titleCase }}</h2>
        <h5 class="is-size-5 has-text-centered">All of the {{ brand.name | titleCase }} shoes</h5>
        <hr />
        <BrandItems
          v-if="urlContextBrandId"
          v-cloak
          :target="'brand/' + urlContextBrandId"
        ></BrandItems>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import BrandItems from '@/components/BrandItems';
import NotFoundBlock from '@/components/NotFoundBlock';

export default {
  name: 'Brand',
  components: {
    BrandItems,
    NotFoundBlock,
  },
  filters: {
    titleCase,
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
    ...mapGetters(['isInitialized', 'brand', 'urlContextBrandId']),
    brandName() {
      return this.$options.filters.titleCase(this.brand.name);
    },
  },
};
</script>
