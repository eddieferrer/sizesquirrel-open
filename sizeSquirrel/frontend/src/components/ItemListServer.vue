<template>
  <ComponentLoader
    :loading-component="isLoadingComponent"
    :failed-to-load="hasComponentFailedToLoad"
  >
    <div class="columns">
      <div class="column is-3">
        <ItemListFiltersServer
          :pagetype="pagetype"
          :query-params="queryParams"
        ></ItemListFiltersServer>
      </div>
      <div class="column is-9">
        <div class="columns">
          <div class="column">
            <ItemListSearchSortServer
              :pagetype="pagetype"
              :query-params="queryParams"
            ></ItemListSearchSortServer>
            <div v-if="items.length !== 0">
              <div class="columns is-multiline">
                <template v-for="shoe in items" :id="'item_' + shoe.item.id">
                  <div :key="shoe.id" class="column is-6">
                    <FindMySizeBlock
                      :shoe="shoe"
                      :retailers="queryParams.retailer"
                      :show-shape-stats="pagetype === 'browse'"
                    ></FindMySizeBlock>
                  </div>
                </template>
              </div>
            </div>
            <div v-if="items.length === 0" class="fail-message">
              <span>No shoes were found matching the selected filters.</span>
            </div>
          </div>
        </div>
        <div class="columns is-centered">
          <div v-if="total_items > 0" class="column is-10 has-text-centered">
            Showing {{ startIndex + 1 }} - {{ endIndex }} of {{ total_items }} items
            <nav
              v-if="numberOfPages > 1"
              class="pagination is-centered"
              role="navigation"
              aria-label="pagination"
            >
              <ul class="pagination-list">
                <li>
                  <a
                    class="pagination-link"
                    aria-label="Go to previous"
                    :disabled="queryParams.page == 1 ? true : false"
                    @click.prevent.stop="
                      queryParams.page != 1 ? changePage(queryParams.page - 1) : null
                    "
                    >&laquo;</a
                  >
                </li>
                <li v-for="page_number in numberOfPages" :key="page_number">
                  <a
                    class="pagination-link"
                    :class="{ 'is-current': page_number == queryParams.page }"
                    :aria-label="'Goto page ' + page_number"
                    @click.prevent.stop="changePage(page_number)"
                    >{{ page_number }}</a
                  >
                </li>
                <li>
                  <a
                    class="pagination-link"
                    aria-label="Go to next"
                    :disabled="queryParams.page == numberOfPages ? true : false"
                    @click.prevent.stop="changePage(queryParams.page + 1)"
                    >&raquo;</a
                  >
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </ComponentLoader>
</template>

<script>
import ComponentLoader from '@/components/ComponentLoader';

import ItemListFiltersServer from './ItemListFiltersServer';
import ItemListSearchSortServer from './ItemListSearchSortServer';
import FindMySizeBlock from './FindMySizeBlock';

export default {
  name: 'ItemListServer',
  components: {
    FindMySizeBlock,
    ItemListFiltersServer,
    ItemListSearchSortServer,
    ComponentLoader,
  },
  props: {
    target: {
      type: String,
      default: '',
    },
    pagetype: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      filter: '',
      sort: 'stats.count',
      sort_order: 'desc',

      total_items: 0,
      items_per_page: 0, // this has to match setting in api
      items: [],

      queryParams: {
        page: 1,
        shoe_type: [],
        gender: [],
        mostCommonFit: [],
        recommendedFootShape: [],
        brand: [],
        retailer: [],
        min_price: undefined,
        max_price: undefined,
        percent_off: 0,
        min_rating: undefined,
        max_rating: undefined,
        rating_by_foot_shape_shape: undefined,
        rating_by_foot_shape_max_rating: undefined,
        rating_by_foot_shape_mmin_rating: undefined,
        search: undefined,
      },
    };
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.total_items / this.items_per_page);
    },
    startIndex() {
      return (this.queryParams.page - 1) * this.items_per_page;
    },
    endIndex() {
      if (this.startIndex + this.items_per_page > this.total_items) {
        return this.total_items;
      }
      return this.startIndex + this.items_per_page;
    },
  },
  created() {
    // other params
    this.queryParams.page = Number(this.$route.query.page) || 1;
    // filter params
    if (this.$route.query.shoe_type) {
      this.queryParams.shoe_type = Array.isArray(this.$route.query.shoe_type)
        ? this.$route.query.shoe_type
        : [this.$route.query.shoe_type];
    }
    if (this.$route.query.gender) {
      this.queryParams.gender = Array.isArray(this.$route.query.gender)
        ? this.$route.query.gender.map(gender => Number(gender))
        : [Number(this.$route.query.gender)];
    }

    if (this.$route.query.min_rating) {
      this.queryParams.min_rating = Number(this.$route.query.min_rating);
    }

    if (this.$route.query.max_rating) {
      this.queryParams.max_rating = Number(this.$route.query.max_rating);
    }

    if (this.$route.query.mostCommonFit) {
      this.queryParams.mostCommonFit = Array.isArray(this.$route.query.mostCommonFit)
        ? this.$route.query.mostCommonFit
        : [this.$route.query.mostCommonFit];
    }

    if (this.$route.query.recommendedFootShape) {
      this.queryParams.recommendedFootShape = Array.isArray(this.$route.query.recommendedFootShape)
        ? this.$route.query.recommendedFootShape
        : [this.$route.query.recommendedFootShape];
    }

    if (this.$route.query.brand) {
      this.queryParams.brand = Array.isArray(this.$route.query.brand)
        ? this.$route.query.brand.map(brand => Number(brand))
        : [Number(this.$route.query.brand)];
    }

    if (
      this.$route.query.rating_by_foot_shape_min_rating ||
      this.$route.query.rating_by_foot_shape_max_rating
    ) {
      this.queryParams.rating_by_foot_shape_shape = Number(
        this.$route.query.rating_by_foot_shape_shape
      );
    }
    if (this.$route.query.rating_by_foot_shape_min_rating) {
      this.queryParams.rating_by_foot_shape_min_rating = Number(
        this.$route.query.rating_by_foot_shape_min_rating
      );
    }
    if (this.$route.query.rating_by_foot_shape_max_rating) {
      this.queryParams.rating_by_foot_shape_max_rating = Number(
        this.$route.query.rating_by_foot_shape_max_rating
      );
    }

    this.queryParams.search = this.$route.query.search || undefined;
    this.queryParams.sort = this.$route.query.sort || undefined;
    this.queryParams.sortOrder = this.$route.query.sortOrder || undefined;

    this.queryParams.max_price = this.$route.query.max_price || undefined;
    this.queryParams.min_price = this.$route.query.min_price || undefined;
    this.queryParams.percent_off = this.$route.query.percent_off || 0;

    if (this.$route.query.retailer) {
      this.queryParams.retailer = Array.isArray(this.$route.query.retailer)
        ? this.$route.query.retailer
        : [this.$route.query.retailer];
    }

    this.isLoadingComponent = true;
    this.$store
      .dispatch('POST_LIST_ITEMS', {
        target: this.target,
        queryParams: Object.assign({}, this.queryParams),
      })
      .then(response => {
        this.items = response.data.items;
        this.total_items = response.data.count;
        this.items_per_page = response.data.items_per_page;
      })
      .catch(error => {
        this.$store.dispatch('SHOW_FLASH_MESSAGE', {
          class: 'has-background-danger',
          message: error,
        });
        this.hasComponentFailedToLoad = true;
      })
      .finally(() => {
        this.isLoadingComponent = false;
      });

    this.$on('allFilterValues', filterValues => {
      this.queryParams.brand = filterValues.brand;
      this.queryParams.gender = filterValues.gender;
      this.queryParams.max_price = filterValues.max_price;
      this.queryParams.max_rating = filterValues.max_rating;
      this.queryParams.min_price = filterValues.min_price;
      this.queryParams.min_rating = filterValues.min_rating;
      this.queryParams.mostCommonFit = filterValues.mostCommonFit;
      this.queryParams.recommendedFootShape = filterValues.recommendedFootShape;
      this.queryParams.percent_off = filterValues.percent_off;
      this.queryParams.rating_by_foot_shape_max_rating =
        filterValues.rating_by_foot_shape_max_rating;
      this.queryParams.rating_by_foot_shape_min_rating =
        filterValues.rating_by_foot_shape_min_rating;
      if (
        filterValues.rating_by_foot_shape_max_rating ||
        filterValues.rating_by_foot_shape_min_rating
      ) {
        this.queryParams.rating_by_foot_shape_shape = filterValues.rating_by_foot_shape_shape;
      }
      this.queryParams.retailer = filterValues.retailer;
      this.queryParams.shoe_type = filterValues.shoe_type;
      this.queryParams.percent_off = filterValues.percent_off;

      this.queryParams.page = 1;
      this.updateRoute();
    });

    this.$on('filterItems', filterValues => {
      this.queryParams.search = filterValues.search;
      this.queryParams.page = 1;
      this.updateRoute();
    });

    this.$on('sortValue', sortValues => {
      this.queryParams.sort = sortValues.sort;
      this.queryParams.page = 1;
      this.updateRoute();
    });

    this.$on('sortOrderValue', sortValues => {
      this.queryParams.sortOrder = sortValues.sortOrder;
      this.queryParams.page = 1;
      this.updateRoute();
    });

    this.$on('resetAll', () => {
      this.$router.push({
        name: this.pagetype,
        query: {
          page: 1,
        },
      });
    });
  },
  methods: {
    changePage(pagenumber) {
      this.queryParams.page = pagenumber;
      this.updateRoute();
    },
    updateRoute() {
      this.$router.push({
        name: this.pagetype,
        query: this.queryParams,
      });
    },
    resetPages() {
      this.changePage(1);
    },
  },
};
</script>

<style scoped lang="scss">
.pagination {
  margin-top: 0.65em;
}
</style>
