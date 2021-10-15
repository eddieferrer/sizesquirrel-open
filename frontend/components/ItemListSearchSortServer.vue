<template>
  <form @submit="filterValue">
    <div class="columns is-multiline">
      <div class="column is-offset-1-tablet is-offset-3-desktop is-4">
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

      <div class="column">
        <div class="field">
          <label class="label has-text-grey-dark">Sort</label>
        </div>
        <div class="field has-addons">
          <div class="control is-expanded">
            <div class="select is-fullwidth">
              <select id="sortSelect" v-model="sort" @change="sortValue">
                <option value="popularity">Popularity</option>
                <option v-if="include_pricing" value="percent_off">
                  Percent Off
                </option>
                <option v-if="include_pricing" value="lowest_sale_price">
                  Sale Price
                </option>
                <option value="model">Model</option>
                <option v-if="include_brands" value="brand_name">Brand</option>

                <option
                  v-if="pagetype === 'browse'"
                  value="popular_fit_descriptor"
                >
                  Most Common Fit
                </option>
                <option
                  v-if="pagetype === 'browse'"
                  value="highest_rated_foot_shape"
                >
                  Recommended Foot Shape
                </option>

                <option value="avg_rating">Average Rating</option>
                <option v-if="include_pricing" value="retail_price">
                  Retail Price
                </option>
              </select>
            </div>
          </div>
          <div class="control">
            <button
              class="button is-normal"
              :class="queryParams.sortOrder == 'asc' ? 'is-primary' : 'is-info'"
              type="button"
              title="Ascending"
              @click="sortOrderValue('asc')"
            >
              <span class="chevron top"></span>
            </button>
            <button
              class="button is-normal"
              :class="
                queryParams.sortOrder == 'desc' || !queryParams.sortOrder
                  ? 'is-primary'
                  : 'is-info'
              "
              type="button"
              title="Descending"
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
  name: 'ItemListSearchSortServer',
  components: { SvgIcon },
  props: {
    pagetype: {
      type: String,
      default: '',
    },
    queryParams: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      include_pricing: false,
      include_brands: false,
      include_model: true,

      search: undefined,
      sort: 'popularity',
    };
  },
  created() {
    const vm = this;

    if (vm.pagetype === 'brand') {
      vm.include_pricing = false;
      vm.include_brands = false;
    }
    if (vm.pagetype === 'sales') {
      vm.include_pricing = true;
      vm.include_brands = true;
    }
    if (vm.pagetype === 'browse') {
      vm.include_pricing = false;
      vm.include_brands = true;
    }
    this.search = this.queryParams.search;
    if (this.queryParams.sort) {
      this.sort = this.queryParams.sort;
    }
  },
  methods: {
    sortOrderValue(sortOrder) {
      this.$parent.$parent.$emit('sortOrderValue', {
        sortOrder,
      });
    },
    sortValue() {
      this.$parent.$parent.$emit('sortValue', {
        sort: this.sort,
      });
    },
    filterValue() {
      this.$parent.$parent.$emit('filterItems', {
        search: this.search,
      });
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
