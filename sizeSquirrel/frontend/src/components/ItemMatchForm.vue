<template>
  <div class="homepage_form">
    <form>
      <div v-if="!isAuthenticated" class="columns">
        <div class="column is-8">
          <h4 class="is-size-5 has-text-white">Shoe I Have</h4>
          <MultiSelectItems v-model="haveitem" class="multiselect-large"></MultiSelectItems>
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
          <MultiSelectItems v-model="wantitem" class="multiselect-large"></MultiSelectItems>
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

import MultiSelectItems from './MultiSelectItems';
import MultiSelectSize from './MultiSelectSize';

import SizeOptions from '@/mixins/SizeOptions';

export default {
  name: 'ItemMatchForm',
  components: { MultiSelectSize, MultiSelectItems },
  mixins: [SizeOptions],
  computed: {
    ...mapGetters(['allitems', 'isAuthenticated', 'urlContextMatch']),
    itemSize: {
      // getter
      get() {
        if (this.urlContextMatch.size) {
          const reducedArray = this.size_option_groups[0].sizes.concat(
            this.size_option_groups[1].sizes
          );
          return reducedArray.filter(
            sizeArray => sizeArray.value === this.urlContextMatch.size.toString()
          )[0];
        }
        return null;
      },
      set(size) {
        this.$store.commit('SET_CONTEXT_MATCH_SIZE', size.value);
      },
    },
    isFormDisabled() {
      try {
        if (!this.isAuthenticated) {
          if (this.wantitem === null || this.haveitem === null || this.size === null) {
            return true;
          }
          return false;
        }
        if (this.wantitem === null) {
          return true;
        }
        return false;
      } catch {
        return true;
      }
    },
    wantitem: {
      // getter
      get() {
        return this.urlContextMatch.want_item;
      },
      // setter
      set(newValue) {
        this.$store.commit('SET_CONTEXT_MATCH_WANT_ITEM', newValue);
      },
    },
    haveitem: {
      // getter
      get() {
        return this.urlContextMatch.have_item;
      },
      // setter
      set(newValue) {
        this.$store.commit('SET_CONTEXT_MATCH_HAVE_ITEM', newValue);
      },
    },
  },
  methods: {
    formAction() {
      if (this.isAuthenticated) {
        this.$router.push(`/match/?want_item_id=${this.urlContextMatch.want_item.id}`);
      } else {
        this.$router.push(
          `/public_match/?have_item_id=${this.urlContextMatch.have_item.id}&size=${
            this.urlContextMatch.size
          }&want_item_id=${this.urlContextMatch.want_item.id}`
        );
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
