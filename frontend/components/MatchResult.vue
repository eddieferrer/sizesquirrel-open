<template>
  <div>
    <div class="columns is-centered">
      <div class="column">
        <div v-if="matchResultsLength > 0" class="columns">
          <div class="column">
            <h2 class="is-size-4 has-text-centered has-text-primary">
              Found Your Size!
            </h2>
            <h5 class="is-size-5 has-text-centered">Recommended Size</h5>
            <hr />
          </div>
        </div>
        <div v-if="matchResultsLength == 0" class="columns">
          <div class="column">
            <h2 class="is-size-4 has-text-centered has-text-primary">
              No Size Found
            </h2>
            <h5 class="is-size-5 has-text-centered">Oh No.</h5>
            <hr />
          </div>
        </div>
      </div>
    </div>

    <div v-if="matchResultsLength > 0" class="columns is-centered">
      <template v-for="(result, index) in matchResults">
        <div
          v-if="matchResults[0].percentage == result.percentage"
          :key="index"
          class="column is-narrow match_size_wrapper has-text-centered"
        >
          <span class="size">{{
            result.size_standard[targetItem.short_size_standard]
          }}</span>
          <span class="ss_color_aqua standard_gender"
            >{{ targetItem.brand['sizing'] }}
            {{ targetItem.gender['name_pretty'] }}</span
          >
        </div>
      </template>
    </div>
    <div v-if="matchResultsLength > 0" class="columns is-centered">
      <template v-for="(result, index) in matchResults">
        <div
          v-if="
            index === matchResultsLength - 1 &&
            matchResultsLength > 1 &&
            matchResults[0].percentage == matchResults[1].percentage
          "
          :key="index"
          class="size_line has-text-centered"
        >
          <span>
            <br />
            <em>We're unsure which of the sizes above will work.</em>
          </span>
        </div>
      </template>
    </div>

    <div class="columns is-centered">
      <div class="column is-two-thirds-desktop is-full-tablet">
        <div class="columns is-clearfix">
          <div class="column is-full-mobile is-one-quarter-tablet">
            <div class="item_block_image">
              <span>
                <v-lazy-image
                  class="lazyload"
                  loading="lazy"
                  :src-placeholder="
                    '/images/placeholder_' + targetItem.type + '.png'
                  "
                  :src="targetItem.shoe_image"
                  :alt="targetItem.brand['name'] + ' ' + targetItem.model"
                />
              </span>
            </div>
          </div>
          <div class="column">
            <div class="columns is-marginless">
              <h2 class="is-size-4 is-capitalized has-text-centered-mobile">
                <NuxtLink
                  class="has-text-info"
                  :to="{
                    name: 'shoes-brand-model',
                    params: {
                      brand: targetItem.brand['name_slug'],
                      model: targetItem.model_slug,
                    },
                  }"
                  >{{ targetItem.model }}</NuxtLink
                >
              </h2>
            </div>
            <div class="columns is-marginless">
              <h4 class="is-size-5 is-capitalized has-text-centered-mobile">
                <NuxtLink
                  class="has-text-info"
                  :to="{
                    name: 'shoes-brand',
                    params: { brand: targetItem.brand['name_slug'] },
                  }"
                  >{{ targetItem.brand['name'] | titleCase }}</NuxtLink
                >
              </h4>
            </div>
            <h4
              class="is-size-6 is-capitalized is-italic has-text-grey has-text-centered-mobile"
            >
              {{ targetItem.gender['name_pretty'] }}
              {{ targetItem.type | capitalize }} Shoe
            </h4>
            <hr class="thin-hr" />
            <div class="columns is-multiline">
              <div class="column is-clearfix is-6">
                <span class="icon-wrapper">
                  <svg-icon icon="fi-torso"></svg-icon>
                </span>
                <div class="info">
                  <span class="info-label muted">Popularity</span>
                  <span>
                    <strong>{{ targetItem.stats.count }}</strong> Profiles
                  </span>
                </div>
              </div>
              <div class="column is-clearfix is-6">
                <span class="icon-wrapper">
                  <svg-icon icon="fi-star"></svg-icon>
                </span>
                <div class="info">
                  <span class="info-label muted">Average Rating</span>
                  <span>
                    <strong v-if="targetItem.stats.count > 0">{{
                      targetItem.stats.avg_rating
                    }}</strong>
                    <strong v-if="targetItem.stats.count == 0"
                      >Not Available</strong
                    >
                    <span
                      v-if="targetItem.stats.count > 0"
                      class="has-text-grey"
                      >&nbsp;/ 5</span
                    >
                  </span>
                </div>
              </div>
              <div class="column is-clearfix is-6">
                <span class="icon-wrapper">
                  <img src="/images/icon_fit.png" alt="shoe fit icon" />
                </span>
                <div class="info">
                  <span class="info-label muted">Most Common Fit</span>
                  <span>
                    <strong>{{
                      targetItem.stats.popular_fit_descriptor
                    }}</strong>
                  </span>
                </div>
              </div>
              <div class="column is-clearfix is-6">
                <span class="icon-wrapper">
                  <img
                    src="/images/icon_footshape.png"
                    alt="foot shape icon"
                    class="footshape"
                  />
                </span>
                <div class="info">
                  <span class="info-label is-size-6 has-text-grey"
                    >Recommended For</span
                  >
                  <strong>{{
                    targetItem.stats.highest_rated_foot_shape
                  }}</strong>
                  Feet
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="columns is-centered" style="margin-top: 1em">
      <div class="column is-full-tablet is-three-quarters-desktop">
        <div v-if="matchResultsLength > 0" class="columns is-centered">
          <div class="column">
            <h5 class="has-text-weight-bold">Sizing Information</h5>
            <hr />
            <template v-for="(result, index) in matchResults">
              <div :key="index">
                <div
                  v-if="matchResults[0].percentage == result.percentage"
                  style="margin-top: 0.5em"
                >
                  <h6>
                    Recommended Size:
                    <strong
                      >{{
                        result.size_standard[targetItem.short_size_standard]
                      }}
                      {{ targetItem.brand['sizing'] }}
                      {{ targetItem.gender['name_pretty'] }}</strong
                    >
                  </h6>
                  <h6>
                    Percentage:
                    <span>
                      <strong>{{ result.percentage }}%</strong>&nbsp;of
                      <strong>{{ result.total_matches }}</strong
                      >&nbsp;matched users
                    </span>
                  </h6>
                  <progress
                    :class="getClass(result.percentage)"
                    class="progress"
                    :value="result.percentage"
                    max="100"
                  >
                    {{ result.percentage }}%
                  </progress>
                </div>
                <template v-if="index === matchResultsLength - 1">
                  <h6
                    v-if="
                      matchResultsLength > 1 &&
                      matchResults[0].percentage ==
                        matchResults[1].percentage &&
                      matchResults[1].percentage
                    "
                  >
                    Accuracy:
                    <strong>
                      <span class="has-text-danger">None</span>
                    </strong>
                  </h6>
                  <h6
                    v-else-if="
                      matchResults[0].occurences <= 10 &&
                      matchResults[0].percentage < 45
                    "
                  >
                    Accuracy:
                    <strong>
                      <span class="has-text-danger">Low</span>
                    </strong>
                  </h6>
                  <h6
                    v-else-if="
                      matchResults[0].occurences > 10 &&
                      matchResults[0].occurences < 15 &&
                      matchResults[0].percentage > 30 &&
                      matchResults[0].percentage < 70
                    "
                  >
                    Accuracy:
                    <strong>
                      <span class="has-text-warning">Medium</span>
                    </strong>
                  </h6>
                  <h6
                    v-else-if="
                      matchResults[0].occurences >= 15 &&
                      matchResults[0].percentage > 70
                    "
                  >
                    Accuracy:
                    <strong>
                      <span class="has-text-success">High</span>
                    </strong>
                  </h6>
                  <h6 v-else>
                    Accuracy:
                    <strong>
                      <span class="has-text-warning">Medium</span>
                    </strong>
                  </h6>
                  <em
                    v-if="
                      matchResultsLength > 1 &&
                      matchResults[0].percentage ==
                        matchResults[1].percentage &&
                      matchResults[1].percentage
                    "
                    >We're unsure which of the sizes above will work.</em
                  >
                </template>
              </div>
            </template>
          </div>
        </div>
        <div v-if="matchResultsLength == 0" class="columns is-centered">
          <div class="column">
            <p>
              We just don't have enough data to find your size! Here are some
              things you can do to help:
            </p>

            <ul>
              <li v-if="isAuthenticated">
                <strong>
                  Add shoes to your
                  <NuxtLink to="/my_profile">profile</NuxtLink>&nbsp;!
                </strong>
              </li>
              <li v-if="isAuthenticated">
                <strong>
                  Add your
                  <NuxtLink to="/my_user_details"
                    >street shoe size in your user details</NuxtLink
                  >&nbsp;!
                </strong>
              </li>
              <li v-if="!isAuthenticated">
                <NuxtLink to="/register">Sign up</NuxtLink>
                &nbsp;for an account and fill out your profile.
              </li>
              <li>
                Like us on
                <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>
              </li>
              <li>
                Follow us on
                <a href="https://www.instagram.com/sizesquirrel/">Instagram</a>
              </li>
              <li>Let everyone at your climbing gym know about SizeSquirrel</li>
              <li>
                Tell everyone at the crag how you used SizeSquirrel to get a
                sweet deal on your shoes
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { capitalize, titleCase } from '@/filters';
import SvgIcon from '@/components/SvgIcon';

export default {
  name: 'MatchResult',
  components: { SvgIcon },
  filters: {
    capitalize,
    titleCase,
  },
  props: {
    matchResults: {
      type: Array,
      default() {
        return [];
      },
    },
    targetItem: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  computed: {
    matchResultsLength() {
      return this.matchResults.length;
    },
    ...mapGetters(['isAuthenticated']),
  },
};
</script>

<style scoped lang="scss">
.info {
  float: left;
  margin-left: 0.55em;
}

span.info-label {
  display: block;
  clear: both;
}

.item_block_image {
  margin: 0 auto;
  margin-top: 0.5em;
  position: relative;
  // width: 160px;
  border: 1px solid $gray;
  background-color: white;
  max-width: 120px;
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

.size_gender,
.match_size_wrapper {
  .size {
    background-color: $aqua;
    height: 85px;
    width: 85px;
    border-radius: 50%;
    clear: both;
    display: block;
    color: $white;
    padding: 10px;
    margin: 0 auto;
    float: none;
    text-align: center;
    line-height: 60px;
    font-weight: bold;
    font-size: 32px;
  }
  // @media only screen and (min-width: 648px) and (max-width: 775px) {
  //   .size {
  //     height: 65px;
  //     width: 65px;
  //     font-size: 29px;
  //     line-height: 46px;
  //   }
  // }
}

.size_gender {
  // padding: 0;
  .size {
    height: 55px;
    width: 55px;
    line-height: 55px;
    padding: 0;
    font-size: 24px;
  }
}

ul {
  list-style: inherit;
  margin-left: 1.5em;
  margin-top: 1em;
}
// fms block & result_item_block & comment blocks
.item_block_info.fms_block,
.item_block_info.result_item_block,
.comment_info_block,
.user_details {
  .info {
    float: left;
    margin-left: 0.65em;
  }
}
</style>
