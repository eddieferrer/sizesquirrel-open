<template>
  <div>
    <div v-cloak class="columns">
      <div class="column">
        <h2 v-cloak class="is-size-4 has-text-centered has-text-primary">
          {{ shoe_brand | titleCase }} {{ shoe_model | titleCase }}
        </h2>
        <h5 class="is-size-5 has-text-centered">More information about this shoe</h5>
        <hr />
      </div>
    </div>
    <!-- dual shoes display -->
    <div v-if="shoe[0] && shoe[1]" class="columns is-centered">
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
    <div v-if="shoe[0] && !shoe[1]" class="columns is-centered">
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
import store from '@/store/store';

import FindMySizeBlock from '@/components/FindMySizeBlock';
import ShoeComments from '@/components/ShoeComments';
import ShoeRatingsByFootShape from '@/components/ShoeRatingsByFootShape';
import ShoeSaleLinks from '@/components/ShoeSaleLinks';

const getData = (to, from, next) => {
  store
    .dispatch('INITIALIZE_APP', {
      url: to.fullPath,
    })
    .then(() => {
      if (store.getters.hasShoe) {
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
  name: 'Shoe',
  components: {
    FindMySizeBlock,
    ShoeComments,
    ShoeRatingsByFootShape,
    ShoeSaleLinks,
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
      title: `${this.brandTitleCase} ${this.model}`,
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: `${this.brandTitleCase} ${this.model} | SizeSquirrel`,
        },
        { vmid: 'og:image', property: 'og:image', content: this.shoe_image },
        { vmid: 'twitter:image:src', property: 'twitter:image:src', content: this.shoe_image },
        { vmid: 'og:image:width', property: 'og:image:width', content: '300' },
        { vmid: 'og:image:height', property: 'og:image:height', content: '300' },
      ],
    };
  },
  computed: {
    ...mapGetters(['isInitialized', 'shoe', 'brand']),
    shoe_image() {
      // eslint-disable-next-line camelcase
      return this.shoe?.[0]?.shoe_image;
    },
    shoe_brand() {
      return this.shoe?.[0]?.brand?.name;
    },
    shoe_model() {
      return this.shoe?.[0]?.model;
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
