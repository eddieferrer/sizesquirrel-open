<template>
  <ComponentLoader :component-state="componentState">
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
                <div v-for="shoe in items" :key="shoe.id" class="column is-6">
                  <FindMySizeBlock
                    :shoe="shoe"
                    :retailers="queryParams.retailer"
                    :show-shape-stats="pagetype === 'browse'"
                  ></FindMySizeBlock>
                </div>
              </div>
            </div>
            <div v-if="items.length === 0" class="fail-message">
              <span>No shoes were found matching the selected filters.</span>
            </div>
          </div>
        </div>
        <Pagination
          :total="total_items"
          :per-page="items_per_page"
          noun="shoes"
          :current-page="queryParams.page"
          @pagechanged="changePage"
        />
      </div>
    </div>
  </ComponentLoader>
</template>

<script>
import ComponentLoader from '@/components/ComponentLoader';
import ItemListFiltersServer from '@/components/ItemListFiltersServer';
import ItemListSearchSortServer from '@/components/ItemListSearchSortServer';
import FindMySizeBlock from '@/components/FindMySizeBlock';
import Pagination from '@/components/Pagination';

export default {
  name: 'ItemListServer',
  components: {
    Pagination,
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
      componentState: '',

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
  watch: {
    '$route.query': {
      deep: true,
      handler() {
        this.updatedComponent();
      },
    },
  },
  created() {
    this.updatedComponent();
  },
  methods: {
    resetQueryParam() {
      this.queryParams = {
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
      };
    },
    changePage(pagenumber) {
      this.queryParams.page = pagenumber;
      this.updateRoute();
    },
    updateRoute() {
      this.$router.push({
        name: this.pagetype,
        query: this.queryParams,
      });
      window.scrollTo(0, 0);
    },
    updatedComponent() {
      this.resetQueryParam();
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
          ? this.$route.query.gender.map((gender) => Number(gender))
          : [Number(this.$route.query.gender)];
      }

      if (this.$route.query.min_rating) {
        this.queryParams.min_rating = Number(this.$route.query.min_rating);
      }

      if (this.$route.query.max_rating) {
        this.queryParams.max_rating = Number(this.$route.query.max_rating);
      }

      if (this.$route.query.mostCommonFit) {
        this.queryParams.mostCommonFit = Array.isArray(
          this.$route.query.mostCommonFit
        )
          ? this.$route.query.mostCommonFit
          : [this.$route.query.mostCommonFit];
      }

      if (this.$route.query.recommendedFootShape) {
        this.queryParams.recommendedFootShape = Array.isArray(
          this.$route.query.recommendedFootShape
        )
          ? this.$route.query.recommendedFootShape
          : [this.$route.query.recommendedFootShape];
      }

      if (this.$route.query.brand) {
        this.queryParams.brand = Array.isArray(this.$route.query.brand)
          ? this.$route.query.brand.map((brand) => Number(brand))
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

      this.componentState = 'loading';
      this.$store
        .dispatch('POST_LIST_ITEMS', {
          target: this.target,
          queryParams: { ...this.queryParams },
        })
        .then((response) => {
          this.items = response.data.items;
          this.total_items = response.data.count;
          this.items_per_page = response.data.items_per_page;
          this.componentState = 'done';
        })
        .catch((error) => {
          this.$store.dispatch('SHOW_FLASH_MESSAGE', {
            class: 'has-background-danger-dark',
            message: error,
          });
          this.componentState = 'error';
        });

      this.$on('allFilterValues', (filterValues) => {
        this.queryParams.brand = filterValues.brand;
        this.queryParams.gender = filterValues.gender;
        this.queryParams.max_price = filterValues.max_price;
        this.queryParams.max_rating = filterValues.max_rating;
        this.queryParams.min_price = filterValues.min_price;
        this.queryParams.min_rating = filterValues.min_rating;
        this.queryParams.mostCommonFit = filterValues.mostCommonFit;
        this.queryParams.recommendedFootShape =
          filterValues.recommendedFootShape;
        this.queryParams.percent_off = filterValues.percent_off;
        this.queryParams.rating_by_foot_shape_max_rating =
          filterValues.rating_by_foot_shape_max_rating;
        this.queryParams.rating_by_foot_shape_min_rating =
          filterValues.rating_by_foot_shape_min_rating;
        if (
          filterValues.rating_by_foot_shape_max_rating ||
          filterValues.rating_by_foot_shape_min_rating
        ) {
          this.queryParams.rating_by_foot_shape_shape =
            filterValues.rating_by_foot_shape_shape;
        }
        this.queryParams.retailer = filterValues.retailer;
        this.queryParams.shoe_type = filterValues.shoe_type;
        this.queryParams.percent_off = filterValues.percent_off;

        this.queryParams.page = 1;
        this.updateRoute();
      });

      this.$on('filterItems', (filterValues) => {
        this.queryParams.search = filterValues.search;
        this.queryParams.page = 1;
        this.updateRoute();
      });

      this.$on('sortValue', (sortValues) => {
        this.queryParams.sort = sortValues.sort;
        this.queryParams.page = 1;
        this.updateRoute();
      });

      this.$on('sortOrderValue', (sortValues) => {
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
    resetPages() {
      this.changePage(1);
    },
  },
};
</script>
