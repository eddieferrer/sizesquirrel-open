<template>
  <ComponentLoader :component-state="componentState">
    <div class="columns">
      <div class="column is-3">
        <BrandItemListFilters
          @allFilterValues="changeAllFilterValues"
          @resetAll="resetAllFilters"
        ></BrandItemListFilters>
      </div>
      <div class="column is-9">
        <div class="columns">
          <div class="column">
            <ItemListSearchSort
              pagetype="brand"
              :sort-order="sort_order"
              @sortOrder="changeSortOrder"
              @sortItems="changeSortValue"
              @filterItems="changeFilterValue"
            ></ItemListSearchSort>
            <div v-if="getItems.length !== 0">
              <div class="columns is-multiline">
                <div
                  v-for="shoe in paginatedItems"
                  :key="shoe.id"
                  class="column is-6"
                >
                  <FindMySizeBlock :shoe="shoe"></FindMySizeBlock>
                </div>
              </div>
            </div>
            <div v-if="getItems.length === 0" class="fail-message">
              <span>No shoes were found matching the selected filters.</span>
            </div>
          </div>
        </div>
        <Pagination
          :total="getItems.length"
          :per-page="30"
          noun="shoes"
          :current-page="currentPage"
          @pagechanged="onPageChange"
        />
      </div>
    </div>
  </ComponentLoader>
</template>

<script>
import ComponentLoader from '@/components/ComponentLoader';
import BrandItemListFilters from '@/components/BrandItemListFilters';
import ItemListSearchSort from '@/components//ItemListSearchSort';
import FindMySizeBlock from '@/components/FindMySizeBlock';
import Pagination from '@/components/Pagination';

export default {
  name: 'BrandItems',
  components: {
    BrandItemListFilters,
    ComponentLoader,
    FindMySizeBlock,
    ItemListSearchSort,
    Pagination,
  },
  props: {
    target: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      componentState: '',
      filter: '',
      sort: 'stats.count',
      sort_order: 'desc',
      shoe_type: [],
      gender: [],
      mostCommonFit: [],
      recommendedFootShape: [],
      brand: [],
      min_rating: undefined,
      max_rating: undefined,
      items: [],
      foot_shape: {
        shape: undefined,
        min: undefined,
        max: undefined,
      },
      currentPage: 1,
      startIndex: 0,
      endIndex: 29,
    };
  },
  computed: {
    paginatedItems() {
      return this.getItems.slice(this.startIndex, this.endIndex + 1);
    },
    getItems() {
      // deep copy of items
      let itemsFiltered = JSON.parse(JSON.stringify(this.items));

      // Filtering
      // model or brand in filter
      if (this.filter !== '') {
        itemsFiltered = itemsFiltered.filter(
          (item) =>
            item.model.toLowerCase().includes(this.filter.toLowerCase()) ||
            item.brand.name.toLowerCase().includes(this.filter.toLowerCase())
        );
      }

      // shoe_type filter
      if (this.shoe_type.length > 0) {
        itemsFiltered = itemsFiltered.filter((item) =>
          this.shoe_type.includes(item.type.toLowerCase())
        );
      }

      // rating filter
      if (this.min_rating && !Number.isNaN(this.min_rating)) {
        itemsFiltered = itemsFiltered.filter(
          (item) => item.stats.avg_rating >= this.min_rating
        );
      }
      if (this.max_rating && !Number.isNaN(this.max_rating)) {
        itemsFiltered = itemsFiltered.filter(
          (item) => item.stats.avg_rating <= this.max_rating
        );
        this.resetPages();
      }

      // foot shape rating filter
      if (this.foot_shape.min && !Number.isNaN(this.foot_shape.min)) {
        itemsFiltered = itemsFiltered.filter((item) => {
          const found = item.stats.ratings.find(
            (rating) =>
              rating.foot_shape_descriptor_id === this.foot_shape.shape
          );
          return found.avg_rating >= this.foot_shape.min;
        });
      }

      if (this.foot_shape.max && !Number.isNaN(this.foot_shape.max)) {
        itemsFiltered = itemsFiltered.filter((item) => {
          const found = item.stats.ratings.find(
            (rating) =>
              rating.foot_shape_descriptor_id === this.foot_shape.shape
          );
          return found.avg_rating <= this.foot_shape.max;
        });
        this.resetPages();
      }

      // gender filter
      if (this.gender.length > 0) {
        itemsFiltered = itemsFiltered.filter((item) =>
          this.gender.includes(item.gender.name.toLowerCase())
        );
      }

      // mostCommonFit filter
      if (this.mostCommonFit.length > 0) {
        itemsFiltered = itemsFiltered.filter((item) =>
          this.mostCommonFit.includes(
            item.stats.popular_fit_descriptor.toLowerCase()
          )
        );
      }

      // recommendedFootShape filter
      if (this.recommendedFootShape.length > 0) {
        itemsFiltered = itemsFiltered.filter((item) => {
          // this.recommendedFootShape.indexOf(item.stats.highest_rated_foot_shape.toLowerCase().trim()) > -1
          const footshapearr = item.stats.highest_rated_foot_shape
            .toLowerCase()
            .replace(/\s/g, '')
            .trim()
            .split('&');
          const found = this.recommendedFootShape.some((r) =>
            footshapearr.includes(r)
          );
          return found;
        });
      }

      // brand filter
      if (this.brand.length > 0) {
        itemsFiltered = itemsFiltered.filter((item) =>
          this.brand.includes(item.brand.name.toLowerCase())
        );
      }

      // Sorting
      if (this.sort !== '') {
        const vueSort = this.sort;
        if (this.sort_order === 'desc') {
          itemsFiltered = itemsFiltered.sort((a, b) => {
            if (
              vueSort === 'model' ||
              vueSort === 'brand.name' ||
              vueSort === 'stats.popular_fit_descriptor' ||
              vueSort === 'stats.highest_rated_foot_shape'
            ) {
              // sort alpha
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA > textB) return -1;
              if (textA < textB) return 1;
              return 0;
            }
            // sort numerically
            return this.deepFind(b, vueSort) - this.deepFind(a, vueSort);
          });
        }
        if (this.sort_order === 'asc') {
          itemsFiltered = itemsFiltered.sort((a, b) => {
            if (
              vueSort === 'model' ||
              vueSort === 'brand.name' ||
              vueSort === 'stats.popular_fit_descriptor' ||
              vueSort === 'stats.highest_rated_foot_shape'
            ) {
              // sort alpha
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA < textB) return -1;
              if (textA > textB) return 1;
              return 0;
            }
            return this.deepFind(a, vueSort) - this.deepFind(b, vueSort);
          });
        }
      }

      this.resetPages();

      return itemsFiltered;
    },
  },
  created() {
    this.componentState = 'loading';
    this.$store
      .dispatch('GET_LIST_ITEMS', {
        target: this.target,
      })
      .then((response) => {
        this.items = response.data.items;
        this.componentState = 'done';
      })
      .catch(() => {
        this.componentState = 'error';
      });
  },
  methods: {
    changeAllFilterValues(filterValues) {
      this.gender = filterValues.gender;
      this.max_rating = filterValues.max_rating;
      this.min_rating = filterValues.min_rating;
      this.mostCommonFit = filterValues.mostCommonFit;
      this.shoe_type = filterValues.shoe_type;
    },
    resetAllFilters() {
      this.gender = [];
      this.max_rating = undefined;
      this.min_rating = undefined;
      this.mostCommonFit = [];
      this.shoe_type = [];
    },
    resetPages() {
      this.currentPage = 1;
      this.startIndex = 0;
      this.endIndex = 29;
    },
    onPageChange(page, startIndex, endIndex) {
      this.currentPage = page;
      this.startIndex = startIndex;
      this.endIndex = endIndex;
    },
    changeSortOrder(value) {
      this.sort_order = value;
    },
    changeSortValue(value) {
      this.sort = value;
    },
    changeFilterValue(value) {
      this.filter = value;
    },
  },
};
</script>
