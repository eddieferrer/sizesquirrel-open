<template>
  <div>
    <NotFoundBlock v-cloak v-if="shoe.length === 0 && isInitialized" />
    <div v-if="shoe.length !== 0" class="columns">
      <div class="column">
        <h2
          v-if="urlContextModelIdList[0] && shoe[0]"
          v-cloak
          class="is-size-4 has-text-centered has-text-primary"
        >
          {{ shoe[0].brand.name | titleCase }} {{ shoe[0].model | titleCase }}
        </h2>
        <h5 class="is-size-5 has-text-centered">More information about this shoe</h5>
        <hr />
      </div>
    </div>
    <!-- dual shoes display -->
    <div
      v-if="urlContextModelIdList[0] && urlContextModelIdList[1] && shoe[0] && shoe[1]"
      class="columns is-centered"
    >
      <div class="column is-5">
        <FindMySizeBlock :shoe="shoe[0]" />
        <ShoeRatingsByFootShape :stats="shoe[0].stats" />
        <ShoeSaleLinks :shoe="shoe[0]" :sale-links="shoe[0].shoe_sale_links" />
        <ShoeComments :shoe="shoe[0]" :comments="shoe[0].shoe_comments" />
      </div>
      <div class="column is-offset-1 is-5">
        <FindMySizeBlock :shoe="shoe[1]" />
        <ShoeRatingsByFootShape :stats="shoe[1].stats" />
        <ShoeSaleLinks :shoe="shoe[1]" :sale-links="shoe[1].shoe_sale_links" />
        <ShoeComments :shoe="shoe[1]" :comments="shoe[1].shoe_comments" />
      </div>
    </div>
    <!-- single shoe display -->
    <div
      v-if="urlContextModelIdList[0] && !urlContextModelIdList[1] && shoe[0] && !shoe[1]"
      class="columns is-centered"
    >
      <div class="column is-half-desktop">
        <FindMySizeBlock :shoe="shoe[0]" />
        <ShoeRatingsByFootShape :stats="shoe[0].stats" />
        <ShoeSaleLinks :shoe="shoe[0]" :sale-links="shoe[0].shoe_sale_links" />
        <ShoeComments :shoe="shoe[0]" :comments="shoe[0].shoe_comments" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import FindMySizeBlock from '@/components/FindMySizeBlock';
import ShoeComments from '@/components/ShoeComments';
import ShoeRatingsByFootShape from '@/components/ShoeRatingsByFootShape';
import ShoeSaleLinks from '@/components/ShoeSaleLinks';
import NotFoundBlock from '@/components/NotFoundBlock';

export default {
  name: 'Shoe',
  components: {
    FindMySizeBlock,
    ShoeComments,
    ShoeRatingsByFootShape,
    ShoeSaleLinks,
    NotFoundBlock,
  },
  filters: {
    titleCase,
  },
  metaInfo() {
    return {
      // title will be injected into parent titleTemplate
      title: `${this.brandTitleCase} ${this.model}`,
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: `${this.brandTitleCase} ${this.model} | SizeSquirrel`,
        },
        { vmid: 'og:image', property: 'og:image', content: this.shoe_image },
        { vmid: 'og:image:width', property: 'og:image:width', content: '300' },
        { vmid: 'og:image:height', property: 'og:image:height', content: '300' },
      ],
    };
  },
  computed: {
    ...mapGetters(['isInitialized', 'urlContextModelIdList', 'shoe', 'brand']),
    shoe_image() {
      if (this.shoe[0]) {
        return this.shoe[0].shoe_image;
      }
      return '';
    },
    brandTitleCase() {
      return this.$options.filters.titleCase(this.brand.name);
    },
    model() {
      if (this.shoe[0]) {
        return this.$options.filters.titleCase(this.shoe[0].model);
      }
      return '';
    },
  },
};
</script>
