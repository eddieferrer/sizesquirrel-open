<template>
  <form class="controls is-clearfix">
    <div class="column">
      <div class="columns is-mobile is-multiline">
        <div class="column is-full-tablet">
          <!-- shoe type -->
          <div class="accordion" :class="{ active: accordionType }">
            <div
              class="field accordion-header"
              @click.prevent.stop="accordionType = !accordionType"
            >
              <label class="label has-text-grey-dark">
                Shoe Type
                <span class="is-pulled-right icon-wrapper-accordion">
                  <svg-icon v-show="accordionType" icon="fi-minus"></svg-icon>
                  <svg-icon v-show="!accordionType" icon="fi-plus"></svg-icon>
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

          <!-- gender -->
          <div class="accordion" :class="{ active: accordionGender }">
            <div
              class="field accordion-header"
              @click.prevent.stop="accordionGender = !accordionGender"
            >
              <label class="label has-text-grey-dark">
                Gender
                <span class="is-pulled-right icon-wrapper-accordion">
                  <svg-icon v-show="accordionGender" icon="fi-minus"></svg-icon>
                  <svg-icon v-show="!accordionGender" icon="fi-plus"></svg-icon>
                </span>
              </label>
            </div>
            <div v-show="accordionGender" class="field accordion-content">
              <label class="checkbox">
                <input v-model="gender" type="checkbox" value="men" />
                Men's
              </label>
              <label class="checkbox">
                <input v-model="gender" type="checkbox" value="women" />
                Women's
              </label>
              <label class="checkbox">
                <input v-model="gender" type="checkbox" value="unisex" />
                Unisex's
              </label>
              <label class="checkbox">
                <input v-model="gender" type="checkbox" value="kids" />
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
                Rating
                <span class="is-pulled-right icon-wrapper-accordion">
                  <svg-icon v-show="accordionRating" icon="fi-minus"></svg-icon>
                  <svg-icon v-show="!accordionRating" icon="fi-plus"></svg-icon>
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
                  <svg-icon v-show="accordionMostCommonFit" icon="fi-minus"></svg-icon>
                  <svg-icon v-show="!accordionMostCommonFit" icon="fi-plus"></svg-icon>
                </span>
              </label>
            </div>
            <div v-show="accordionMostCommonFit" class="field accordion-content">
              <label class="checkbox">
                <input v-model="mostCommonFit" type="checkbox" value="normal" />
                Normal
              </label>
              <label class="checkbox">
                <input v-model="mostCommonFit" type="checkbox" value="comfortable" />
                Comfortable
              </label>
              <label class="checkbox">
                <input v-model="mostCommonFit" type="checkbox" value="aggressive" />
                Aggressive
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
    </div>
  </form>
</template>
<script>
import SvgIcon from '@/components/SvgIcon';

// this is only currently used in the brand page
export default {
  name: 'BrandItemListFilters',
  components: { SvgIcon },
  data() {
    return {
      accordionType: true,
      accordionGender: true,
      accordionRating: true,
      accordionMostCommonFit: false,

      shoe_type: [],
      gender: [],
      mostCommonFit: [],
      min_rating: undefined,
      max_rating: undefined,
    };
  },

  computed: {},
  created() {},
  methods: {
    emitFilter() {
      this.$parent.$parent.$emit('allFilterValues', {
        gender: this.gender,
        max_rating: this.max_rating,
        min_rating: this.min_rating,
        mostCommonFit: this.mostCommonFit,
        shoe_type: this.shoe_type,
      });
    },
    resetAllFilters() {
      this.shoe_type = [];
      this.gender = [];
      this.min_rating = undefined;
      this.max_rating = undefined;
      this.mostCommonFit = [];
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
