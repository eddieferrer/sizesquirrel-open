<template>
  <div class="columns is-multiline is-centered">
    <template v-for="(shoe, index) in shoes">
      <!-- cards -->
      <div
        :key="index"
        class="column"
        :class="{ 'is-12': index === 0, 'is-11': index === 1 }"
      >
        <h3
          v-if="index == 0"
          class="is-size-4 has-text-centered has-text-primary"
        >
          Recommended Shoe
        </h3>
        <h3
          v-if="index == 1"
          class="is-size-5 has-text-centered has-text-primary"
        >
          Also Consider
        </h3>

        <div
          class="card"
          :class="{ 'active-card': index === 0, 'scale-small': index === 1 }"
        >
          <div class="card-content">
            <div class="content">
              <!-- old card start  -->
              <div class="columns is-clearfix">
                <div class="column is-full-mobile is-one-fifth-tablet">
                  <div class="item_block_image">
                    <span>
                      <v-lazy-image
                        class="lazyload"
                        loading="lazy"
                        :src-placeholder="
                          '/images/placeholder_' + shoe.type + '.png'
                        "
                        :src="shoe.shoe_image"
                        :alt="shoe.brand.name + shoe.model"
                      />
                    </span>
                  </div>
                </div>
                <div class="column">
                  <div class="columns is-marginless">
                    <h2
                      class="is-size-4 is-capitalized has-text-centered-mobile"
                    >
                      <NuxtLink
                        class="has-text-info"
                        :to="{
                          name: 'shoe',
                          params: {
                            shoe_brand: shoe.brand.name_slug,
                            shoe_model: shoe.model_slug,
                          },
                        }"
                        >{{ shoe.model }}</NuxtLink
                      >
                    </h2>
                  </div>

                  <div class="columns is-marginless">
                    <h4
                      class="is-size-5 is-capitalized has-text-centered-mobile"
                    >
                      <NuxtLink
                        class="has-text-info"
                        :to="{
                          name: 'shoes-brand',
                          params: { brand: shoe.brand.name_slug },
                        }"
                        >{{ shoe.brand.name }}</NuxtLink
                      >
                    </h4>
                  </div>

                  <h4
                    class="is-size-6 is-capitalized is-italic has-text-grey has-text-centered-mobile"
                  >
                    {{ shoe.gender.name_pretty }} {{ shoe.type }} Shoe
                  </h4>
                  <hr class="thin-hr" />

                  <div class="columns is-clearfix is-centered">
                    <div class="column is-12">
                      <div class="columns is-multiline">
                        <div
                          class="column is-full-mobile is-narrow is-clearfix"
                        >
                          <span class="icon-wrapper">
                            <svg-icon icon="fi-torso"></svg-icon>
                          </span>
                          <div class="info">
                            <span class="info-label is-size-6 has-text-grey"
                              >Popularity</span
                            >
                            <span>
                              <strong>{{ shoe.stats.count }}</strong
                              >&nbsp;Profiles
                            </span>
                          </div>
                        </div>
                        <div
                          class="column is-full-mobile is-narrow is-clearfix"
                        >
                          <div>
                            <span class="icon-wrapper">
                              <svg-icon icon="fi-star"></svg-icon>
                            </span>
                            <div class="info">
                              <span class="info-label is-size-6 has-text-grey"
                                >Average Rating</span
                              >
                              <span>
                                <strong v-if="shoe.stats.count > 0">{{
                                  shoe.stats.avg_rating
                                }}</strong>
                                <strong v-if="shoe.stats.count == 0"
                                  >Not Available</strong
                                >
                                <span
                                  v-if="shoe.stats.count > 0"
                                  class="has-text-grey"
                                  >&nbsp;/ 5</span
                                >
                              </span>
                            </div>
                          </div>
                        </div>
                        <div
                          class="column is-full-mobile is-narrow is-clearfix"
                        >
                          <span class="icon-wrapper">
                            <img
                              src="/images/icon_fit.png"
                              alt="shoe fit icon"
                            />
                          </span>
                          <div class="info">
                            <span class="info-label is-size-6 has-text-grey"
                              >Most Common Fit</span
                            >
                            <span>
                              <strong>{{
                                shoe.stats.popular_fit_descriptor
                              }}</strong>
                            </span>
                          </div>
                        </div>
                        <div
                          class="column is-full-mobile is-narrow is-clearfix"
                        >
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
                              shoe.stats.highest_rated_foot_shape
                            }}</strong>
                            Feet
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="columns is-clearfix is-centered">
                <div
                  v-for="(comment, cindex) in shoe.best_comments"
                  :key="cindex"
                  class="column is-6"
                >
                  <p>
                    &quot;
                    <em>{{ comment.comments }}</em
                    >&quot;
                    <br />
                    <NuxtLink
                      :to="{
                        name: 'profile-username',
                        params: { username: comment.user.username },
                      }"
                      >{{ comment.user.username }}</NuxtLink
                    >
                  </p>
                </div>
              </div>
              <hr class="thin-hr" />
              <div class="columns is-clearfix is-centered">
                <div class="column is-12">
                  <!-- logged in  -->
                  <div v-if="isAuthenticated">
                    <form :id="'form_' + shoe.id" action="/match/" method="get">
                      <input
                        type="hidden"
                        name="want_item_id"
                        :value="shoe.id"
                      />
                      <button
                        type="submit"
                        class="button is-info is-normal is-marginless is-pulled-right"
                      >
                        Find My Size
                      </button>
                    </form>
                  </div>
                  <!-- anonymous -->
                  <div v-if="!isAuthenticated">
                    <NuxtLink
                      to="/register"
                      class="has-text-info is-pulled-right"
                      >Sign up now to find your size!</NuxtLink
                    >
                  </div>
                </div>
              </div>
              <!-- old card end  -->
            </div>
          </div>
        </div>
      </div>
    </template>
    <div v-if="shoes.length == 0" class="column is-12">
      <h3 class="is-size-4 has-text-centered has-text-primary">Sorry</h3>
      <div class="card active-card">
        <div class="card-content">
          <div class="content">
            <p>We could not confidently recommend a shoe for you.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import SvgIcon from '@/components/SvgIcon';

export default {
  name: 'RecommendedShoesCards',
  components: { SvgIcon },
  props: {
    shoes: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
};
</script>

<style scoped lang="scss">
.scale-small {
  transform: scale(0.975);
}
.active-card {
  box-shadow: 0 8px 12px 0 rgba(122, 122, 122, 0.2),
    0 2px 3px rgba(17, 17, 17, 0.1), 0 0 0 1px rgba(17, 17, 17, 0.1);
}
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
h3 {
  margin-bottom: 0.75rem;
}
</style>
