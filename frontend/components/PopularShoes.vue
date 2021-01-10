<template>
  <ComponentLoader :component-state="componentState">
    <section class="section">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        Popular Shoes
      </h2>
      <hr />
      <ShoeTiles>
        <FindMySizeBlock
          v-for="(shoe, index) in popular_shoes"
          :slot="'index' + index"
          :key="shoe.id"
          :shoe="shoe"
          :show-shape-stats="true"
        ></FindMySizeBlock>
      </ShoeTiles>
      <br />
      <!-- logged in  -->
      <h4 v-if="isAuthenticated" class="has-text-centered is-size-5">
        <NuxtLink to="/browse">See Detailed Stats on More Shoes</NuxtLink>
      </h4>
      <!-- not logged in  -->
      <div class="columns is-centered">
        <div class="column is-8">
          <h4
            v-if="!isAuthenticated"
            class="has-text-centered box has-background-light is-size-5"
          >
            <strong
              >Want to see detailed stats like these for other shoes?</strong
            ><br />
            Registered users have the ability to browse shoes.
            <NuxtLink to="/register" class="has-text-info"
              >Sign up for an account.</NuxtLink
            >
          </h4>
        </div>
      </div>
    </section>
  </ComponentLoader>
</template>

<script>
import { mapGetters } from 'vuex';

import ComponentLoader from '@/components/ComponentLoader';
import FindMySizeBlock from '@/components/FindMySizeBlock';
import ShoeTiles from '@/components/ShoeTiles';

export default {
  name: 'PopularShoes',
  components: { FindMySizeBlock, ShoeTiles, ComponentLoader },
  data() {
    return {
      popular_shoes: [],
      componentState: '',
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  created() {
    this.componentState = 'loading';
    this.$store
      .dispatch('GET_POPULAR_SHOES', this.targetUserId)
      .then((response) => {
        this.popular_shoes = response.data.items;
        this.componentState = 'done';
      })
      .catch(() => {
        // on error, just displays no popular shoes
        this.hasComponentFailedToLoad = true;
        this.componentState = 'error';
      });
  },
};
</script>
