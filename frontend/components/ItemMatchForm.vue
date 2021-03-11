<template>
  <div class="homepage_form">
    <form>
      <div v-if="!isAuthenticated" class="columns">
        <div class="column is-8">
          <h4 class="is-size-5 has-text-white">Shoe I Have</h4>
          <MultiSelectItems
            v-model="haveItem"
            class="multiselect-large"
          ></MultiSelectItems>
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
          <MultiSelectItems
            v-model="wantItem"
            class="multiselect-large"
          ></MultiSelectItems>
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
      wantItem: null,
      haveItem: null,
      itemSize: null,
    };
  },
  computed: {
    ...mapGetters([
      'isAuthenticated',
      'matchInfoSize',
      'matchInfoWant',
      'matchInfoHave',
    ]),
    isFormDisabled() {
      // conditions for form to be disabled for authorized users
      if (this.isAuthenticated) {
        // form is missing required fields
        if (this.wantItem === null) {
          return true;
        }
        // form hasn't been touched and has same values as route
        if (Number(this.$route.query.want_item_id) === this.wantItem.id) {
          return true;
        }
      }
      // conditions for form to be disabled for not authorized users
      if (!this.isAuthenticated) {
        // form is missing required fields
        if (
          this.wantItem === null ||
          this.haveItem === null ||
          this.itemSize === null
        ) {
          return true;
        }
        // form hasn't been touched and has same values as route
        // eslint-disable-next-line no-console
        if (
          Number(this.$route.query.want_item_id) === this.wantItem.id &&
          Number(this.$route.query.have_item_id) === this.haveItem.id &&
          this.$route.query.size === this.itemSize?.value
        ) {
          return true;
        }
      }
      return false;
    },
  },
  watch: {
    matchInfoWant: {
      deep: true,
      handler(newValue) {
        this.wantItem = newValue.shoe;
      },
    },
    matchInfoHave: {
      deep: true,
      handler(newValue) {
        this.haveItem = newValue.shoe;
      },
    },
    matchInfoSize: {
      deep: true,
      handler(newValue) {
        this.itemSize = newValue;
      },
    },
  },
  methods: {
    formAction() {
      if (this.isAuthenticated) {
        this.$router.push({
          path: '/match',
          query: { want_item_id: this.wantItem.id },
        });
      } else {
        this.$router.push({
          path: '/public_match',
          query: {
            want_item_id: this.wantItem.id,
            have_item_id: this.haveItem.id,
            size: this.itemSize.value,
          },
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
$white: rgba(255, 255, 255, 1);

.homepage_form {
  background-color: rgba(0, 0, 0, 0.8);
  max-width: 800px;
  margin: 0 auto;
  padding: 1.25em 1.55em 1.35em 1.55em;

  h3 {
    color: $white;
  }
}
#find_my_size {
  margin-top: 1.45em;
}
</style>
