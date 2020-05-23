<template>
  <ComponentLoader
    :loading-component="isLoadingComponent"
    :failed-to-load="hasComponentFailedToLoad"
  >
    <MatchResult
      v-if="urlContextModelIdList[0]"
      :match-results="matchResults"
      :target-item="targetItem"
    ></MatchResult>

    <div class="columns is-centered" style="margin-top: 1em;">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <ShoeSaleLinks
          v-if="urlContextModelIdList[0] && shoe[0]"
          :shoe="shoe[0]"
          :sale-links="shoe[0].shoe_sale_links"
          page="match"
        ></ShoeSaleLinks>
      </div>
    </div>

    <div v-if="isAuthenticated" class="columns is-centered">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <PrivateMatchResult
          v-if="urlContextModelIdList[0] && shoe[0]"
          :comments="shoe[0].shoe_comments"
          :match-results="matchResults"
          :target-item="targetItem"
          :grouped-match-users="groupedMatchUsers"
          :street-results="streetResults"
        ></PrivateMatchResult>
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
  </ComponentLoader>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import ShoeSaleLinks from '@/components/ShoeSaleLinks';
import MatchResult from '@/components/MatchResult';
import PrivateMatchResult from '@/components/PrivateMatchResult';
import ComponentLoader from '@/components/ComponentLoader';

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
  data() {
    return {
      matchResults: [],
      targetItem: {},
      groupedMatchUsers: [],
      streetResults: [],
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
    ...mapGetters(['isAuthenticated', 'urlContextModelIdList', 'shoe']),
    shoe_image() {
      if (this.shoe[0]) {
        return this.shoe[0].shoe_image;
      }
      return '';
    },
    brand() {
      if (this.shoe[0]) {
        return this.$options.filters.titleCase(this.shoe[0].brand.name);
      }
      return '';
    },
    model() {
      if (this.shoe[0]) {
        return this.$options.filters.titleCase(this.shoe[0].model);
      }
      return '';
    },
  },
  created() {
    this.isLoadingComponent = true;

    const vm = this;

    function getUrlParam(parameter) {
      let urlparameter = '';
      if (window.location.href.indexOf(parameter) > -1) {
        urlparameter = vm.getUrlVars()[parameter];
      }
      return urlparameter;
    }

    const urlWantItemId = getUrlParam('want_item_id');
    const urlSize = getUrlParam('size');
    const urlHaveItemId = getUrlParam('have_item_id');

    if (vm.isAuthenticated) {
      this.$store
        .dispatch('PRIVATE_MATCH', {
          wantItemId: urlWantItemId,
        })
        .then(response => {
          vm.matchResults = response.data.match_results;
          vm.targetItem = response.data.target_item;
          vm.groupedMatchUsers = response.data.grouped_match_users;
          vm.streetResults = response.data.street_results;
        })
        .catch(() => {
          this.hasComponentFailedToLoad = true;
        })
        .finally(() => {
          this.isLoadingComponent = false;
        });
    } else {
      this.$store
        .dispatch('PUBLIC_MATCH', {
          wantItemId: urlWantItemId,
          haveItemId: urlHaveItemId,
          size: urlSize,
        })
        .then(response => {
          vm.matchResults = response.data.match_results;
          vm.targetItem = response.data.target_item;
        })
        .catch(() => {
          this.hasComponentFailedToLoad = true;
        })
        .finally(() => {
          this.isLoadingComponent = false;
        });
    }
  },
};
</script>
