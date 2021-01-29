<template>
  <div>
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Admin Match Test
        </h2>
        <hr />
      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <MultiSelectItems v-model="item"></MultiSelectItems>
      </div>
      <div class="column is-3">
        <button
          class="button is-info is-medium is-fullwidth"
          @click.prevent.stop="matchTestSubmit"
        >
          Match
        </button>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <table class="table">
          <thead>
            <tr>
              <th>DataFeed Brand_Name</th>
              <th>DataFeed Product_Name</th>
              <th>Match</th>
              <th>Retailer_Name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(itm, index) in matchTestItems" :key="index">
              <td>{{ itm['DataFeed Brand_Name'] }}</td>
              <td>{{ itm['DataFeed Product_Name'] }}</td>
              <td>{{ itm['Match'] }}</td>
              <td>{{ itm['Retailer_Name'] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MultiSelectItems from '@/components/MultiSelectItems';

export default {
  name: 'MatchTest',
  middleware: ['auth'],
  components: { MultiSelectItems },
  layout: 'no-homepage-form',
  data() {
    return {
      item: null,
      matchTestItems: [],
    };
  },
  computed: {
    ...mapGetters(['allitems']),
  },
  methods: {
    matchTestSubmit() {
      // eslint-disable-next-line no-console
      console.log(
        'Matching:',
        this.item.brand.name,
        this.item.model,
        this.item.id
      );
      this.$store
        .dispatch('POST_ADMIN_MATCH_TEST', {
          matchTestItemId: this.item.id,
        })
        .then((response) => {
          this.matchTestItems = response.data.matchTest;
        });
    },
  },
  head() {
    return {
      title: 'Admin',
    };
  },
};
</script>
<style lang="scss" scoped>
table {
  width: 100%;
}
</style>
