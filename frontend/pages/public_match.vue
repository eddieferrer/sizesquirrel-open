<template>
  <div>
    <ComponentLoader :component-state="componentState">
      <MatchResult
        :match-results="matchResults"
        :target-item="targetItem"
      ></MatchResult>
    </ComponentLoader>

    <div class="columns is-centered" style="margin-top: 1em">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <ShoeSaleLinks
          :shoe="shoe"
          :sale-links="saleLinks"
          page="match"
        ></ShoeSaleLinks>
      </div>
    </div>

    <div class="columns is-centered">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <h4 class="has-text-centered box has-background-light is-size-5">
          <NuxtLink to="/register">Sign Up</NuxtLink>&nbsp; for an account to
          see more detailed sizing information, user comments, ratings,
          recommended foot shape and more.
        </h4>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';
import { sizeOptions } from '@/utils/utils';

import ShoeSaleLinks from '@/components/ShoeSaleLinks';
import MatchResult from '@/components/MatchResult';
import ComponentLoader from '@/components/ComponentLoader';

export default {
  name: 'Match',
  components: {
    ShoeSaleLinks,
    MatchResult,
    ComponentLoader,
  },
  filters: {
    titleCase,
  },
  layout: 'homepageForm',
  data() {
    return {
      matchResults: [],
      targetItem: {},
      shoe: {},
      shoeComments: [],
      saleLinks: [],
      componentState: '',
    };
  },
  async fetch() {
    const context = this.$nuxt.context;
    const promises = [];

    if (context.route.query.want_item_id) {
      promises.push(
        context.store.dispatch('GET_MATCH_INFO', {
          key: 'want',
          id: context.route.query.want_item_id,
        })
      );
    } else {
      return;
    }

    if (context.route.query.have_item_id) {
      promises.push(
        context.store.dispatch('GET_MATCH_INFO', {
          key: 'have',
          id: context.route.query.have_item_id,
        })
      );
    }

    if (context.route.query.size) {
      const sizesArray = sizeOptions();
      const reducedArray = sizesArray[0].sizes.concat(sizesArray[1].sizes);
      context.store.commit(
        'SET_MATCH_SIZE',
        reducedArray.filter(
          (sizeArray) => sizeArray.value === context.route.query.size.toString()
        )[0]
      );
    }

    await Promise.all(promises)
      .then(() => {
        this.updateComponent();
      })
      .catch(() => {
        context.store.commit('STATE_INIT_ERROR');
      });
  },
  head() {
    return {
      // title will be injected into parent titleTemplate
      title: `${this.brand} ${this.model} - Your Size`,
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: `${this.brand} ${this.model} - Your Size | SizeSquirrel`,
        },
        { vmid: 'og:image', property: 'og:image', content: this.shoe_image },
        {
          vmid: 'twitter:image:src',
          property: 'twitter:image:src',
          content: this.shoe_image,
        },
        { vmid: 'og:image:width', property: 'og:image:width', content: '300' },
        {
          vmid: 'og:image:height',
          property: 'og:image:height',
          content: '300',
        },
      ],
    };
  },
  computed: {
    ...mapGetters(['matchInfoWant']),
    shoe_image() {
      return this.shoe?.shoe_image;
    },
    brand() {
      const brand = this.shoe?.brand?.name ?? 'Unknown Shoe';
      return this.$options.filters.titleCase(brand);
    },
    model() {
      return this.$options.filters.titleCase(this.shoe.model);
    },
  },
  watch: {
    '$route.query': '$fetch',
  },
  created() {
    this.updateComponent();
  },
  methods: {
    updateComponent() {
      this.shoe = this.matchInfoWant?.shoe ?? {};
      this.shoeComments = this.matchInfoWant?.shoe_comments ?? [];
      this.saleLinks = this.matchInfoWant?.shoe_sale_links ?? [];

      this.componentState = 'loading';

      const getMatch = this.$store.dispatch('PUBLIC_MATCH', {
        size: this.$route.query.size,
        haveItemId: this.$route.query.have_item_id,
        wantItemId: this.$route.query.want_item_id,
      });

      getMatch
        .then(({ data }) => {
          this.matchResults = data.match_results;
          this.targetItem = data.target_item;

          this.componentState = 'done';
        })
        .catch(() => {
          this.componentState = 'error';
          // show error if params missing
          this.$store.dispatch('SHOW_FLASH_MESSAGE', {
            class: 'has-background-danger-dark',
            message:
              'There has been an error. Please restart the process to find a match.',
          });
        });
    },
  },
};
</script>
