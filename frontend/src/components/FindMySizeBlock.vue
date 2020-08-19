<template>
  <div>
    <div class="columns is-clearfix">
      <div class="column is-full-mobile is-one-fifth-tablet">
        <div class="item_block_image">
          <span>
            <v-lazy-image
              class="lazyload"
              loading="lazy"
              :src-placeholder="'/static/images/placeholder_' + shoe.type + '.png'"
              :src="shoe.shoe_image"
              :alt="shoe.brand.name + shoe.model"
            />
          </span>
        </div>
      </div>
      <div class="column">
        <div class="columns is-marginless">
          <h2 class="is-size-4 is-capitalized has-text-centered-mobile">
            <RouterLink
              class="has-text-info"
              :to="{
                name: 'shoe',
                params: { shoe_brand: shoe.brand.name_slug, shoe_model: shoe.model_slug },
              }"
              >{{ shoe.model }}</RouterLink
            >
          </h2>
        </div>

        <div class="columns is-marginless">
          <h4 class="is-size-5 is-capitalized has-text-centered-mobile">
            <RouterLink
              class="has-text-info"
              :to="{
                name: 'brand',
                params: { shoe_brand: shoe.brand.name_slug },
              }"
              >{{ shoe.brand.name }}</RouterLink
            >
          </h4>
        </div>

        <h4 class="is-size-6 is-capitalized is-italic has-text-grey has-text-centered-mobile">
          {{ shoe.gender.name_pretty }} {{ shoe.type }} Shoe
        </h4>
      </div>
    </div>
    <hr class="thin-hr" />

    <div class="columns is-multiline is-clearfix">
      <!-- add this to make full screen -->
      <!-- column is-clearfix is-half-tablet is-one-quarter-desktop -->
      <div class="column is-clearfix is-6">
        <span class="icon-wrapper">
          <svg-icon icon="fi-torso" :has-fill="true"></svg-icon>
        </span>
        <div class="info">
          <span class="info-label is-size-6 has-text-grey">Popularity</span>
          <span>
            <strong>{{ shoe.stats.count }}</strong
            >&nbsp;Profiles
          </span>
        </div>
      </div>
      <div class="column is-clearfix is-6">
        <div>
          <span class="icon-wrapper">
            <svg-icon icon="fi-star" :has-fill="true"></svg-icon>
          </span>
          <div class="info">
            <span class="info-label is-size-6 has-text-grey">Average Rating</span>
            <span>
              <strong v-if="shoe.stats.count > 0">{{ shoe.stats.avg_rating }}</strong>
              <strong v-if="shoe.stats.count == 0">Not Available</strong>
              <span v-if="shoe.stats.count > 0" class="has-text-grey">&nbsp;/ 5</span>
            </span>
          </div>
        </div>
      </div>
      <div class="column is-clearfix is-6">
        <span class="icon-wrapper">
          <img src="/static/images/icon_fit.png" alt="shoe fit icon" />
        </span>
        <div class="info">
          <span class="info-label is-size-6 has-text-grey">Most Common Fit</span>
          <span>
            <strong>{{ shoe.stats.popular_fit_descriptor }}</strong>
          </span>
        </div>
      </div>
      <div class="column is-clearfix is-6">
        <span class="icon-wrapper">
          <img src="/static/images/icon_footshape.png" alt="foot shape icon" class="footshape" />
        </span>
        <div class="info">
          <span class="info-label is-size-6 has-text-grey">Recommended For</span>
          <strong>{{ shoe.stats.highest_rated_foot_shape }}</strong> Feet
        </div>
      </div>
      <!-- data feeds -->
      <div v-if="shoe.datafeeds" class="column is-no-top-padding is-12">
        <template v-for="(datafeed, index) in shoe.datafeeds">
          <!--  if loop.first  -->
          <div v-if="index === 0" :key="index + '_1'" class="columns is-marginless">
            <div class="column is-paddingless is-12">
              <h6 class="is-pulled-right">
                <strong>Retail Price&nbsp;</strong>
                ${{ datafeed.Product.Retail_Price }}
              </h6>
            </div>
          </div>
          <!--  endif  -->
          <div :key="index + '_2'" class="column is-12 is-paddingless">
            <AffiliatePriceBlock
              v-if="retailers.length == 0 || retailers.indexOf(datafeed.Retailer_Name) > -1"
              :key="index + '_2'"
              :datafeed="datafeed"
            ></AffiliatePriceBlock>
          </div>
          <!--  if loop.last  -->
          <div v-if="index === shoe.datafeeds.length - 1" :key="index + '_3'" class="columns">
            <div class="column is-12">
              <hr class="thin-hr" />
            </div>
          </div>
          <!--  endif  -->
        </template>
      </div>
      <!-- shoe stats -->
      <div v-if="showShapeStats" class="column is-no-top-padding is-12">
        <span class="icon-wrapper">
          <img src="/static/images/icon_footshape.png" alt="foot shape icon" class="footshape" />
        </span>
        <div class="info_footshape">
          <span class="info-label is-size-6 has-text-grey">Rating by Foot shape&nbsp;</span>
          <ul class="is-clearfix">
            <li v-for="(rating, index) in shoe.stats.ratings" :key="index">
              <div class="shape">
                <strong>{{ rating.foot_shape_descriptor }}</strong>
              </div>
              <div class="bar" :title="titleString(rating)">
                <progress
                  class="progress"
                  :title="titleString(rating)"
                  :value="rating.avg_rating"
                  :class="progressBarClass(rating)"
                  max="5"
                  >{{ rating.avg_rating }}%</progress
                >
              </div>
              <div class="rating">
                <span class="is-size-7 has-text-grey">&nbsp;{{ rating.avg_rating }}</span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <hr class="thin-hr" />
    <div class="columns">
      <div class="column">
        <!-- logged in  -->
        <div v-if="isAuthenticated">
          <form :id="'form_' + shoe.id" action="/match/" method="get">
            <input type="hidden" name="want_item_id" :value="shoe.id" />
            <button type="submit" class="button is-info is-normal is-marginless is-pulled-right">
              Find My Size
            </button>
          </form>
        </div>
        <!-- anonymous -->
        <div v-if="!isAuthenticated">
          <RouterLink to="/register" class="has-text-info is-pulled-right"
            >Sign up now to find your size!</RouterLink
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import SvgIcon from '@/components/SvgIcon';
import AffiliatePriceBlock from './AffiliatePriceBlock';

export default {
  name: 'FindMySizeBlock',
  components: { AffiliatePriceBlock, SvgIcon },
  props: {
    showShapeStats: {
      type: Boolean,
      default: false,
    },
    shoe: {
      type: Object,
      default() {
        return {};
      },
    },
    retailers: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  methods: {
    titleString(rating) {
      if (this.shoe.stats.highest_rated_foot_shape.includes(rating.foot_shape_descriptor)) {
        return 'Recommended Foot Shape';
      }
      if (rating.count <= 5) {
        return 'Not Enough Data';
      }
      return rating.avg_rating;
    },
    progressBarClass(rating) {
      if (this.shoe.stats.highest_rated_foot_shape.includes(rating.foot_shape_descriptor)) {
        return 'is-success';
      }
      if (rating.count <= 5) {
        return '';
      }
      if (rating.avg_rating >= 4) {
        return 'is-link';
      }
      if (rating.avg_rating >= 2) {
        return 'is-primary';
      }
      if (rating.avg_rating >= 0) {
        return 'is-warning';
      }
      return '';
    },
  },
};
</script>

<style scoped lang="scss">
.info,
.info_footshape {
  float: left;
  width: 80%;
}
.info {
  max-width: 85%;
  margin-left: 0.55em;
}
.info_footshape {
  margin-left: 0.65em;
  li {
    display: flex;
    .shape {
      width: 71px;
      padding-right: 5px;
    }
    .rating {
      flex: 0.25;
    }
    .bar {
      flex: 0.75;
      padding-top: 3px;
      padding-right: 3px;
    }
  }
}
span.info-label {
  display: block;
  clear: both;
}
.item_block_image {
  margin: 0 auto;
  margin-top: 0.5em;
  position: relative;
  width: 160px;
  border: 1px solid $gray;
  background-color: white;
  max-width: 150px;
  padding: 1%;
  float: none;
  & > span {
    position: absolute;
    display: block;
    width: 86%;
  }
  &:after {
    content: '';
    display: block;
    padding-bottom: 100%;
  }
  @media (min-width: 768px) {
    float: right;
    padding: 7%;
    width: 100%;
    overflow: hidden;
  }
}
</style>
