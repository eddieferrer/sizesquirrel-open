<template>
  <div class="homepage_form">
    <form>
      <div v-if="!isAuthenticated" class="columns">
        <div class="column is-8">
          <h4 class="is-size-5 has-text-white">Shoe I Have</h4>
          <MultiSelectItems v-model="haveItem" class="multiselect-large"></MultiSelectItems>
        </div>
        <div class="column is-4">
          <h4 class="is-size-5 has-text-white">Size</h4>
          <MultiSelectSize
            v-model="itemSize"
            class="multiselect-large"
            placeholder="Select A Size"
          ></MultiSelectSize>
        </div>
      </div>
      <div class="columns">
        <div class="column is-8">
          <h4 class="is-size-5 has-text-white">Shoe I Want</h4>
          <MultiSelectItems v-model="wantItem" class="multiselect-large"></MultiSelectItems>
        </div>
        <div class="column is-4">
          <button
            id="find_my_size"
            type="submit"
            class="button is-info is-medium is-fullwidth"
            :disabled="isFormDisabled"
            @click.stop.prevent="formAction()"
          >
            Find My Size
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import SizeOptions from '@/mixins/SizeOptions';

import MultiSelectItems from '@/components/MultiSelectItems';
import MultiSelectSize from '@/components/MultiSelectSize';

export default {
  name: 'ItemMatchForm',
  components: { MultiSelectSize, MultiSelectItems },
  mixins: [SizeOptions],
  data() {
    return {
      wantItem: {},
      haveItem: {},
      itemSize: {},
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'matchInfoSize', 'matchInfoWant', 'matchInfoHave']),
    isFormDisabled() {
      // conditions for form to be disabled for authorized users
      if (this.isAuthenticated) {
        // form is missing required fields
        if (this.wantItem === null) {
          return true;
        }
        // form hasn't been touched and has same values as route
        if (this.$route.query.want_item_id === this.wantItem.id?.toString()) {
          return true;
        }
      }
      // conditions for form to be disabled for not authorized users
      if (!this.isAuthenticated) {
        // form is missing required fields
        if (this.wantItem === null || this.haveItem === null || this.itemSize === null) {
          return true;
        }
        // form hasn't been touched and has same values as route
        if (
          this.$route.query.want_item_id === this.wantItem.id?.toString() &&
          this.$route.query.have_item_id === this.haveItem.id?.toString() &&
          this.$route.query.size === this.matchInfoSize.toString()
        ) {
          return true;
        }
      }
      return false;
    },
  },
  created() {
    this.wantItem = this.matchInfoWant;
    this.haveItem = this.matchInfoHave;
    this.itemSize = this.matchInfoSize;
  },
  methods: {
    formAction() {
      // TODO fix this route to pass values into component
      // TODO remove this casting
      // When doing a hard refresh on browser,
      // these values are coming from $route.query as strings
      if (this.isAuthenticated) {
        this.$router
          .push({
            path: '/match',
            query: { want_item_id: this.wantItem.id.toString() },
          })
          .catch(() => {});
      } else {
        this.$router
          .push({
            path: '/public_match',
            query: {
              want_item_id: this.wantItem.id.toString(),
              have_item_id: this.haveItem.id.toString(),
              size: this.itemSize.value.toString(),
            },
          })
          .catch(() => {});
      }
    },
  },
};
</script>

<style scoped lang="scss">
$white: rgba(255, 255, 255, 1);

.homepage_form {
  background-color: rgba(0, 0, 0, 0.8);
  h3 {
    color: $white;
  }
  max-width: 800px;
  margin: 0 auto;
  padding: 1.25em 1.55em 1.35em 1.55em;
}
#find_my_size {
  margin-top: 1.45em;
}
</style>
