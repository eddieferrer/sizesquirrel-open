<template>
  <div>
    <ComponentLoader :component-state="componentState">
      <MatchResult :match-results="matchResults" :target-item="targetItem"></MatchResult>
    </ComponentLoader>

    <div class="columns is-centered" style="margin-top: 1em">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <ShoeSaleLinks :shoe="shoe" :sale-links="saleLinks" page="match"></ShoeSaleLinks>
      </div>
    </div>

    <div v-if="isAuthenticated" class="columns is-centered">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <ComponentLoader :component-state="componentState">
          <PrivateMatchResult
            :comments="shoeComments"
            :match-results="matchResults"
            :target-item="targetItem"
            :grouped-match-users="groupedMatchUsers"
            :street-results="streetResults"
          ></PrivateMatchResult>
        </ComponentLoader>
      </div>
    </div>

    <div v-if="!isAuthenticated" class="columns is-centered">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <h4 class="has-text-centered box has-background-light is-size-5">
          <RouterLink to="/register">Sign Up</RouterLink>&nbsp; for an account to see more detailed
          sizing information, user comments, ratings, recommended foot shape and more.
        </h4>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';
import store from '@/store/store';
import { sizeOptions } from '@/utils/utils';

import ShoeSaleLinks from '@/components/ShoeSaleLinks';
import MatchResult from '@/components/MatchResult';
import PrivateMatchResult from '@/components/PrivateMatchResult';
import ComponentLoader from '@/components/ComponentLoader';

const getData = (to, from, next) => {
  const promises = [];

  if (to.query.want_item_id) {
    promises.push(
      store.dispatch('GET_MATCH_INFO', {
        key: 'want',
        id: to.query.want_item_id,
      })
    );
  }

  if (to.query.have_item_id) {
    promises.push(
      store.dispatch('GET_MATCH_INFO', {
        key: 'have',
        id: to.query.have_item_id,
      })
    );
  }

  if (to.query.size) {
    const sizesArray = sizeOptions();
    const reducedArray = sizesArray[0].sizes.concat(sizesArray[1].sizes);
    store.commit(
      'SET_MATCH_SIZE',
      reducedArray.filter((sizeArray) => sizeArray.value === to.query.size.toString())[0]
    );
  }

  Promise.all(promises)
    .then(() => {
      next();
    })
    .catch(() => {
      store.commit('STATE_INIT_ERROR');
    });
};

export default {
  name: 'Match',
  components: {
    ShoeSaleLinks,
    MatchResult,
    PrivateMatchResult,
    ComponentLoader,
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
  props: {
    wantItemId: {
      type: String,
      default: '',
    },
    size: {
      type: String,
      default: '',
    },
    haveItemId: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      matchResults: [],
      targetItem: {},
      groupedMatchUsers: [],
      streetResults: [],
      shoe: {},
      shoeComments: [],
      saleLinks: [],
      componentState: '',
    };
  },
  metaInfo() {
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
        { vmid: 'og:image:width', property: 'og:image:width', content: '300' },
        { vmid: 'og:image:height', property: 'og:image:height', content: '300' },
      ],
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'matchInfoWant']),
    shoe_image() {
      // eslint-disable-next-line camelcase
      return this.shoe.shoe?.shoe_image;
    },
    brand() {
      return this.$options.filters.titleCase(this.shoe.shoe?.brand?.name || '');
    },
    model() {
      return this.$options.filters.titleCase(this.shoe.model);
    },
  },
  created() {
    this.shoe = this.matchInfoWant.shoe;
    this.shoeComments = this.matchInfoWant.shoe_comments;
    this.saleLinks = this.matchInfoWant.shoe_sale_links;

    this.componentState = 'loading';

    let getMatch;
    if (this.isAuthenticated) {
      getMatch = this.$store.dispatch('PRIVATE_MATCH', {
        wantItemId: this.wantItemId,
      });
    } else {
      getMatch = this.$store.dispatch('PUBLIC_MATCH', {
        wantItemId: this.wantItemId,
        haveItemId: this.haveItemId,
        size: this.size,
      });
    }

    getMatch
      .then(({ data }) => {
        this.matchResults = data.match_results;
        this.targetItem = data.target_item;
        this.groupedMatchUsers = data.grouped_match_users;
        this.streetResults = data.street_results;

        this.componentState = 'done';
      })
      .catch(() => {
        this.componentState = 'error';
      });
  },
};
</script>
