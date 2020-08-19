<template>
  <div>
    <multiselect
      v-model="selectedItem"
      label="model"
      track-by="id"
      placeholder="Search for a shoe"
      open-direction="bottom"
      :options="items"
      :option-height="52"
      :show-labels="false"
      :multiple="false"
      :searchable="true"
      :loading="isLoading"
      :internal-search="false"
      :options-limit="100"
      :hide-selected="false"
      :close-on-select="true"
      :clear-on-select="false"
      :max-height="400"
      @search-change="asyncFind"
      @input="updateValue"
    >
      <template slot="option" slot-scope="props">
        <div class="option_wrapper">
          <div class="option_img">
            <v-lazy-image
              class="lazyload"
              loading="lazy"
              :src-placeholder="'/static/images/placeholder_' + props.option.type + '.png'"
              :src="props.option.shoe_image"
              :alt="props.option.brand['name'] + ' ' + props.option.model"
            />
          </div>
          <div class="option__desc">
            <p class="option__title">
              <strong>{{ props.option.model | titleCase }}</strong> -
              {{ props.option.brand.name | titleCase }}
            </p>
            <p class="option__subtitle">
              {{ props.option.gender.name_pretty | titleCase }}
              {{ props.option.type | titleCase }} Shoe
            </p>
          </div>
        </div>
      </template>
      <template slot="singleLabel" slot-scope="props">
        <div v-if="props.option.brand && props.option.model" class="option__desc">
          <p class="option__title">
            <strong>{{ props.option.model | titleCase }}</strong> -
            {{ props.option.brand.name | titleCase }}
          </p>
        </div>
      </template>
      <template slot="noResult">
        <span v-if="query.length <= 2">Please enter 3 characters or more</span>
        <span v-if="query.length > 2">Oops! No shoes found</span>
      </template>
      <span slot="noOptions">Please enter 3 characters or more</span>
    </multiselect>
  </div>
</template>

<script>
import debounce from 'lodash.debounce';
import Multiselect from 'vue-multiselect';
import { titleCase } from '@/filters';

export default {
  name: 'MultiSelectItems',
  components: {
    Multiselect,
  },
  filters: {
    titleCase,
  },
  props: {
    value: {
      type: Object,
      default() {
        return {
          brand: {},
          model: {},
        };
      },
    },
  },
  data() {
    return {
      selectedItem: this.value,
      items: [],
      isLoading: false,
      query: '',
    };
  },
  watch: {
    value() {
      this.selectedItem = this.value;
      this.$emit('input', this.selectedItem);
    },
  },
  methods: {
    updateValue() {
      this.$emit('input', this.selectedItem);
    },
    searchForItem(query) {
      this.$store
        .dispatch('ITEM_SEARCH', {
          query,
        })
        .then((response) => {
          this.items = response.data.items;
          this.isLoading = false;
        });
    },
    // eslint-disable-next-line func-names
    debouncedSearch: debounce(function (query) {
      this.searchForItem(query);
    }, 750),
    asyncFind(query) {
      this.query = query;
      this.isLoading = true;
      if (query.length <= 2) {
        this.items = [];
        this.isLoading = false;
      } else {
        this.debouncedSearch(query);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~vue-multiselect/dist/vue-multiselect.min.css';
@import '../scss/custom_multiselect.scss';

.option__image {
  height: 50px;
  max-width: 50px;
  border: 1px solid $gray;
}

.option_wrapper {
  display: grid;
  grid-template-columns: auto 1fr;
  grid-gap: 3px;
}
.option_img {
  border: 1px solid $gray;
  float: left;
  margin-right: 10px;
  background-color: white;
  height: 52px;
  padding: 1px;
  max-width: 52px;
  min-width: 52px;
}
.option__subtitle {
  padding-top: 4px;
  font-style: italic;
}
img {
  width: 50px;
}
</style>
