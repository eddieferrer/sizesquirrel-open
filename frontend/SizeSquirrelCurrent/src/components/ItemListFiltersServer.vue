<template>
  <form class="controls is-clearfix">
    <div class="columns is-mobile is-multiline">
      <div class="column is-full-tablet">
        <!-- shoe type -->
        <div class="accordion" :class="{ active: accordionType }">
          <div class="field accordion-header" @click.prevent.stop="accordionType = !accordionType">
            <label class="label has-text-grey-dark">
              Shoe Type
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionType" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionType" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionType" class="field accordion-content">
            <label class="checkbox">
              <input v-model="shoe_type" type="checkbox" value="rock" />
              Rock
            </label>
            <label class="checkbox">
              <input v-model="shoe_type" type="checkbox" value="approach" />
              Approach
            </label>
            <label class="checkbox">
              <input v-model="shoe_type" type="checkbox" value="mountain" />
              Mountain
            </label>
          </div>
        </div>

        <!-- percent off -->
        <div v-if="include_pricing" class="accordion" :class="{ active: accordionSale }">
          <div class="field accordion-header" @click.prevent.stop="accordionSale = !accordionSale">
            <label class="label has-text-grey-dark">
              Sale
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionSale" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionSale" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionSale" class="field accordion-content">
            <label class="radio">
              <input v-model="percent_off" type="radio" value="0" />
              Show All
            </label>
            <label class="radio">
              <input v-model="percent_off" type="radio" value="20" />
              > 20% Off
            </label>
            <label class="radio">
              <input v-model="percent_off" type="radio" value="40" />
              > 40% Off
            </label>
            <label class="radio">
              <input v-model="percent_off" type="radio" value="60" />
              > 60% Off
            </label>
          </div>
        </div>

        <!-- min/max price -->
        <div v-if="include_pricing" class="accordion" :class="{ active: accordionPrice }">
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionPrice = !accordionPrice"
          >
            <label class="label has-text-grey-dark">
              Price
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionPrice" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionPrice" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionPrice" class="field accordion-content is-clearfix">
            <label class="text price">
              Min
              <input
                v-model="min_price"
                class="input is-width-limited"
                type="number"
                min="0"
                max="1000"
                maxlength="4"
                placeholder="Min"
              />
            </label>
            <label class="text price">
              Max
              <input
                v-model="max_price"
                class="input is-width-limited"
                type="number"
                min="0"
                max="1000"
                maxlength="4"
                placeholder="Max"
              />
            </label>
          </div>
        </div>

        <!-- gender -->
        <div class="accordion" :class="{ active: accordionGender }">
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionGender = !accordionGender"
          >
            <label class="label has-text-grey-dark">
              Gender
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionGender" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionGender" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionGender" class="field accordion-content">
            <label class="checkbox">
              <input v-model="gender" type="checkbox" :value="1" />
              Men's
            </label>
            <label class="checkbox">
              <input v-model="gender" type="checkbox" :value="2" />
              Women's
            </label>
            <label class="checkbox">
              <input v-model="gender" type="checkbox" :value="3" />
              Unisex's
            </label>
            <label class="checkbox">
              <input v-model="gender" type="checkbox" :value="4" />
              Kids
            </label>
          </div>
        </div>

        <!-- rating -->
        <div class="accordion" :class="{ active: accordionRating }">
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionRating = !accordionRating"
          >
            <label class="label has-text-grey-dark">
              Average Rating
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionRating" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionRating" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionRating" class="field accordion-content is-clearfix">
            <label class="text rating">
              Min
              <input
                v-model="min_rating"
                class="input is-width-limited"
                type="number"
                min="0"
                max="5"
                maxlength="1"
                placeholder="Min"
              />
            </label>
            <label class="text rating">
              Max
              <input
                v-model="max_rating"
                class="input is-width-limited"
                type="number"
                min="0"
                max="5"
                maxlength="1"
                placeholder="Max"
              />
            </label>
          </div>
        </div>

        <!-- most common fit -->
        <div class="accordion" :class="{ active: accordionMostCommonFit }">
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionMostCommonFit = !accordionMostCommonFit"
          >
            <label class="label has-text-grey-dark">
              Most Common Fit
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionMostCommonFit" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionMostCommonFit" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionMostCommonFit" class="field accordion-content">
            <label class="checkbox">
              <input v-model="mostCommonFit" type="checkbox" value="Normal" />
              Normal
            </label>
            <label class="checkbox">
              <input v-model="mostCommonFit" type="checkbox" value="Comfortable" />
              Comfortable
            </label>
            <label class="checkbox">
              <input v-model="mostCommonFit" type="checkbox" value="Aggressive" />
              Aggressive
            </label>
          </div>
        </div>

        <!-- most common shape -->
        <div
          v-if="include_recommended_shape"
          class="accordion"
          :class="{ active: accordionRecommendedFootShape }"
        >
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionRecommendedFootShape = !accordionRecommendedFootShape"
          >
            <label class="label has-text-grey-dark">
              Recommended Foot Shape
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionRecommendedFootShape" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionRecommendedFootShape" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionRecommendedFootShape" class="field accordion-content">
            <label class="checkbox">
              <input v-model="recommendedFootShape" type="checkbox" value="Egyptian" />
              Egyptian
            </label>
            <label class="checkbox">
              <input v-model="recommendedFootShape" type="checkbox" value="Roman" />
              Roman
            </label>
            <label class="checkbox">
              <input v-model="recommendedFootShape" type="checkbox" value="Greek" />
              Greek
            </label>
            <label class="checkbox">
              <input v-model="recommendedFootShape" type="checkbox" value="Germanic" />
              Germanic
            </label>
            <label class="checkbox">
              <input v-model="recommendedFootShape" type="checkbox" value="Celtic" />
              Celtic
            </label>
          </div>
        </div>

        <!-- rating by foot shape -->
        <div
          v-if="include_rating_by_shape"
          class="accordion"
          :class="{ active: accordionRatingFootShape }"
        >
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionRatingFootShape = !accordionRatingFootShape"
          >
            <label class="label has-text-grey-dark">
              Rating By Foot Shape
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionRatingFootShape" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionRatingFootShape" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionRatingFootShape" class="field accordion-content is-clearfix">
            <div class="field">
              <label class="has-text-grey-dark">Foot Shape</label>
              <div class="control">
                <div class="select is-fullwidth">
                  <select id="sortSelect" v-model="rating_by_foot_shape_shape">
                    <option :value="1">Egyptian</option>
                    <option :value="2">Roman</option>
                    <option :value="3">Greek</option>
                    <option :value="4">Germanic</option>
                    <option :value="5">Celtic</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label class="text price">
                  Min
                  <input
                    v-model="rating_by_foot_shape_min_rating"
                    class="input is-width-limited"
                    type="number"
                    min="0"
                    max="5"
                    maxlength="4"
                    placeholder="Min"
                  />
                </label>
                <label class="text price">
                  Max
                  <input
                    v-model="rating_by_foot_shape_max_rating"
                    class="input is-width-limited"
                    type="number"
                    min="0"
                    max="5"
                    maxlength="4"
                    placeholder="Max"
                  />
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="column">
        <!-- Brands -->
        <div
          v-if="include_brands"
          class="accordion custom-margin"
          :class="{ active: accordionBrands }"
        >
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionBrands = !accordionBrands"
          >
            <label class="label has-text-grey-dark">
              Brand
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionBrands" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionBrands" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionBrands" class="field accordion-content">
            <label v-for="brandItem in sortedBrands" :key="brandItem.id" class="checkbox">
              <input v-model="brand" type="checkbox" :value="brandItem.id" />
              {{ brandItem.name | titleCase }}
            </label>
          </div>
        </div>

        <!-- retailers -->
        <div v-if="include_pricing" class="accordion" :class="{ active: accordionRetailers }">
          <div
            class="field accordion-header"
            @click.prevent.stop="accordionRetailers = !accordionRetailers"
          >
            <label class="label has-text-grey-dark">
              Retailers
              <span class="is-pulled-right icon-wrapper-accordion">
                <svg-icon v-show="!accordionRetailers" icon="fi-plus"></svg-icon>
                <svg-icon v-show="accordionRetailers" icon="fi-minus"></svg-icon>
              </span>
            </label>
          </div>
          <div v-show="accordionRetailers" class="field accordion-content">
            <label v-for="(retailerName, index) in allRetailers" :key="index" class="checkbox">
              <input v-model="retailer" type="checkbox" :value="retailerName" />
              {{ retailerName }}
            </label>
          </div>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column">
        <a class="button is-text" type="button" @click="resetAllFilters">Clear All Filters</a>
      </div>
      <div class="column">
        <a class="button is-info is-fullwidth" type="button" @click="emitFilter">Filter</a>
      </div>
    </div>
  </form>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import SvgIcon from '@/components/SvgIcon';

export default {
  name: 'ItemListFiltersServer',
  components: { SvgIcon },
  filters: {
    titleCase,
  },
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
      allRetailers: [
        'Adidas Outdoor / Five Ten',
        'Backcountry',
        'Bent Gate',
        'Black Diamond Equipment',
        'Camp Saver',
        'Eastern Mountain Sports',
        'La Sportiva',
        'LeftLane Sports',
        'Moosejaw',
        'Mountain Steals',
        'Outdoor Gear Exchange',
        'REI',
        'The Clymb',
      ],

      accordionType: true,
      accordionGender: true,
      accordionRating: true,
      accordionSale: true,
      accordionPrice: true,
      accordionRetailers: true,

      accordionBrands: this.queryParams.brand.length > 0,
      accordionMostCommonFit: this.queryParams.mostCommonFit.length > 0,
      accordionRecommendedFootShape: this.queryParams.recommendedFootShape.length > 0,
      accordionRatingFootShape:
        !!this.queryParams.rating_by_foot_shape_max_rating ||
        !!this.queryParams.rating_by_foot_shape_min_rating,

      include_pricing: false,
      include_brands: false,
      include_rating_by_shape: false,

      min_price: this.queryParams.min_price,
      max_price: this.queryParams.max_price,
      percent_off: this.queryParams.percent_off,
      brand: this.queryParams.brand,
      gender: this.queryParams.gender,
      max_rating: this.queryParams.max_rating,
      min_rating: this.queryParams.min_rating,
      mostCommonFit: this.queryParams.mostCommonFit,
      recommendedFootShape: this.queryParams.recommendedFootShape,
      rating_by_foot_shape_max_rating: this.queryParams.rating_by_foot_shape_max_rating,
      rating_by_foot_shape_min_rating: this.queryParams.rating_by_foot_shape_min_rating,
      rating_by_foot_shape_shape: this.queryParams.rating_by_foot_shape_shape || 1,
      shoe_type: this.queryParams.shoe_type,
      retailer: this.queryParams.retailer,
    };
  },
  computed: {
    ...mapGetters(['allbrands']),

    sortedBrands() {
      function compare(a, b) {
        if (a.name < b.name) return -1;
        if (a.name > b.name) return 1;
        return 0;
      }
      const sortedBrandsArray = this.allbrands;
      return sortedBrandsArray.sort(compare);
    },
  },
  created() {
    const vm = this;

    this.$store
      .dispatch('GET_ALL_BRANDS')
      .then(() => {
        this.isComponentLoaded = true;
      })
      .catch(() => {
        this.$store.dispatch('SHOW_FLASH_MESSAGE', {
          class: 'has-background-danger',
          message: 'There has been a fatal server error. Please reload the page.',
        });
        this.isComponentLoaded = false;
      });

    if (vm.pagetype === 'browse') {
      vm.include_pricing = false;
      vm.include_brands = true;
      vm.include_rating_by_shape = true;
      vm.include_recommended_shape = true;
    }
    if (vm.pagetype === 'sales') {
      vm.include_pricing = true;
      vm.include_brands = true;
      vm.include_rating_by_shape = false;
      vm.include_recommended_shape = true;
    }
  },
  methods: {
    emitFilter() {
      this.$parent.$parent.$emit('allFilterValues', {
        brand: this.brand,
        gender: this.gender,
        max_rating: this.max_rating,
        min_rating: this.min_rating,
        mostCommonFit: this.mostCommonFit,
        recommendedFootShape: this.recommendedFootShape,
        rating_by_foot_shape_max_rating: this.rating_by_foot_shape_max_rating,
        rating_by_foot_shape_min_rating: this.rating_by_foot_shape_min_rating,
        rating_by_foot_shape_shape: this.rating_by_foot_shape_shape,
        shoe_type: this.shoe_type,
        percent_off: this.percent_off,
        min_price: this.min_price,
        max_price: this.max_price,
        retailer: this.retailer,
      });
    },
    resetAllFilters() {
      this.$parent.$parent.$emit('resetAll');
    },
  },
};
</script>

<style scoped lang="scss">
.accordion {
  margin: 1em 0em;
  .accordion-header {
    padding-right: 1em;
    label {
      cursor: pointer;
    }
  }
}
.column {
  padding-top: 0;
  padding-bottom: 0;
}
.custom-margin {
  margin-top: 1em;
  @media (min-width: 768px) {
    margin-top: 0;
  }
}
form label.checkbox,
form label.radio {
  clear: both;
  display: block;
  margin-bottom: 0.25em;
}
.radio + .radio {
  margin-left: 0em;
}
.is-width-limited {
  max-width: 150px;
  clear: both;
  display: block;
}
label.text.rating,
label.text.price {
  width: 40%;
  margin-right: 5%;
  float: left;
  input {
    max-width: 75px;
  }
}
</style>
