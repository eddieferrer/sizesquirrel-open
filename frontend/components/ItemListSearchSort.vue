<template>
  <form>
    <div class="columns is-multiline">
      <div
        v-if="include_search"
        class="column is-offset-1-tablet is-offset-3-desktop is-4"
      >
        <div class="field">
          <label class="label has-text-grey-dark">Search</label>
        </div>
        <div class="field has-addons">
          <div class="control is-expanded">
            <input
              v-model="search"
              class="input"
              type="text"
              placeholder="Search for shoe by model or brand..."
            />
          </div>
          <div class="control">
            <a class="button is-info" @click="filterValue">
              <span class="icon-wrapper-search">
                <svg-icon icon="fi-magnifying-glass"></svg-icon>
              </span>
            </a>
          </div>
        </div>
      </div>

      <div class="column" :class="{ 'is-offset-one-quarter': !include_search }">
        <div class="field">
          <label class="label has-text-grey-dark">Sort</label>
        </div>
        <div class="field has-addons">
          <div class="control is-expanded">
            <div class="select is-fullwidth">
              <select id="sortSelect" @change="sortValue">
                <option v-if="include_popularity" value="stats.count">
                  Popularity
                </option>
                <option v-if="include_pricing" value="percent_off">
                  Percent Off
                </option>
                <option v-if="include_pricing" value="lowest_sale_price">
                  Sale Price
                </option>
                <option v-if="include_model" value="model">Model</option>
                <option v-if="include_brands" value="brand.name">Brand</option>
                <option
                  v-if="pagetype !== 'profile' && pagetype !== 'comments'"
                  value="stats.avg_rating"
                >
                  Rating
                </option>
                <option v-if="pagetype === 'profile'" value="user_item.rating">
                  Rating
                </option>
                <option v-if="pagetype === 'comments'" value="rating">
                  Rating
                </option>
                <option
                  v-if="pagetype === 'comments'"
                  value="user.get_foot_shape"
                >
                  Foot Shape
                </option>
                <option v-if="pagetype === 'comments'" value="fit_descriptor">
                  Fit
                </option>

                <option v-if="pagetype === 'comments'" value="size">
                  Size
                </option>
                <option
                  v-if="include_pricing"
                  value="datafeeds.Product.Retail_Price"
                >
                  Retail Price
                </option>
              </select>
            </div>
          </div>
          <div class="control">
            <button
              class="button is-normal"
              type="button"
              title="Ascending"
              :class="sortOrder == 'asc' ? 'is-primary' : 'is-info'"
              @click="sortOrderValue('asc')"
            >
              <span class="chevron top"></span>
            </button>
            <button
              class="button is-normal"
              type="button"
              title="Descending"
              :class="sortOrder == 'desc' ? 'is-primary' : 'is-info'"
              @click="sortOrderValue('desc')"
            >
              <span class="chevron bottom"></span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import SvgIcon from '@/components/SvgIcon';

export default {
  name: 'ItemListSearchSort',
  components: { SvgIcon },
  props: {
    pagetype: {
      type: String,
      default: '',
    },
    sortOrder: {
      type: String,
      default: 'desc',
    },
  },
  data() {
    return {
      include_pricing: false,
      include_search: true,
      include_popularity: true,
      include_brands: false,
      include_model: true,
      search: undefined,
    };
  },
  created() {
    const vm = this;

    if (vm.pagetype === 'brand') {
      vm.include_pricing = false;
      vm.include_search = true;
      vm.include_popularity = true;
      vm.include_brands = false;
      vm.include_model = true;
    }
    if (vm.pagetype === 'profile') {
      vm.include_pricing = false;
      vm.include_search = false;
      vm.include_popularity = false;
      vm.include_brands = true;
      vm.include_model = true;
    }
    if (vm.pagetype === 'comments') {
      vm.include_pricing = false;
      vm.include_search = false;
      vm.include_popularity = false;
      vm.include_brands = false;
      vm.include_model = false;
    }
  },
  methods: {
    sortOrderValue(sort) {
      this.$emit('sortOrder', sort);
    },
    filterValue() {
      this.$emit('filterItems', this.search);
    },
    sortValue(e) {
      this.$emit('sortItems', e.target.value);
    },
  },
};
</script>

<style scoped lang="scss">
input {
  background: $white;
}

form {
  margin-bottom: 1em;
}
// chevrons
.chevron {
  color: $white;
}

.chevron::before {
  border-style: solid;
  border-width: 0.25em 0.25em 0 0;
  content: '';
  display: inline-block;
  height: 1em;
  // left: 0.05em;
  position: relative;
  top: 0.45em;
  transform: rotate(-45deg);
  vertical-align: top;
  width: 1em;
}

.chevron.right:before {
  left: 0;
  transform: rotate(45deg);
}

.chevron.bottom:before {
  top: 0;
  transform: rotate(135deg);
}

.chevron.left:before {
  // left: 0.25em;
  transform: rotate(-135deg);
}
// bulma overwrite bug?
.button,
.control.has-icons-left .icon,
.control.has-icons-right .icon,
.input,
.pagination-ellipsis,
.pagination-link,
.pagination-next,
.pagination-previous,
.select,
.select select,
.textarea {
  height: 2.5em;
}
</style>
