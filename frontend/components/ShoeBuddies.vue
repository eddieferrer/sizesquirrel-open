<template>
  <ComponentLoader :component-state="componentState">
    <section class="section">
      <div class="columns">
        <div class="column">
          <h2 class="is-size-4 has-text-centered has-text-primary">
            Shoe Buddies
          </h2>
          <h5 class="is-size-5 has-text-centered">
            These users have the same shoes you do
          </h5>
          <hr />
          <template v-if="shoe_buddies.length > 0">
            <div
              v-for="(buddy, index) in shoe_buddies"
              :key="index"
              class="box has-background-light"
            >
              <p>
                You have {{ buddy.count_shoes }} shoes in common with
                <NuxtLink
                  :to="{
                    name: 'profile-username',
                    params: { username: buddy.username },
                  }"
                  >{{ buddy.username }}</NuxtLink
                >.
              </p>
            </div>
          </template>
          <div v-if="shoe_buddies.length == 0" class="box has-background-light">
            <p>Sorry, no shoe buddies found</p>
          </div>
        </div>
        <div class="column">
          <h2 class="is-size-4 has-text-centered has-text-primary">
            Best Shoe Buddies
          </h2>
          <h5 class="is-size-5 has-text-centered">These users and you</h5>
          <hr />
          <template v-if="best_shoe_buddies.length > 0">
            <div
              v-for="(buddy, index) in best_shoe_buddies"
              :key="index"
              class="box has-background-light"
            >
              <p>
                You and
                <NuxtLink
                  :to="{
                    name: 'profile-username',
                    params: { username: buddy.username },
                  }"
                  >{{ buddy.username }}</NuxtLink
                >
                wear {{ buddy['count_shoes'] }}
                <span v-if="buddy.count_shoes == 1">shoe</span>
                <span v-if="buddy.count_shoes > 1">shoes</span>&nbsp;
                <em>in the same size.</em> Check out their
                <NuxtLink
                  :to="{
                    name: 'profile-username',
                    params: { username: buddy.username },
                  }"
                  >profile</NuxtLink
                >.
              </p>
            </div>
          </template>

          <div
            v-if="best_shoe_buddies.length == 0"
            class="box has-background-light"
          >
            <p>Sorry, we cannot find a best shoe buddy.</p>
          </div>
        </div>
      </div>
    </section>
  </ComponentLoader>
</template>

<script>
import ComponentLoader from '@/components/ComponentLoader';

export default {
  name: 'ShoeBuddies',
  components: { ComponentLoader },
  props: {
    targetUserId: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      shoe_buddies: [],
      best_shoe_buddies: [],
      componentState: '',
    };
  },
  created() {
    this.componentState = 'loading';
    this.$store
      .dispatch('GET_SHOE_BUDDIES', this.targetUserId)
      .then((response) => {
        this.shoe_buddies = response.data.shoe_buddies;
        this.best_shoe_buddies = response.data.best_shoe_buddies;
        this.componentState = 'done';
      })
      .catch(() => {
        // on error, just displays no shoe buddies
        this.hasComponentFailedToLoad = true;
        this.componentState = 'error';
      });
  },
};
</script>
