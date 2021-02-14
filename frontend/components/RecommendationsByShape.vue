<template>
  <section v-if="user.recommendations_by_shape.length > 0" class="section">
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Recommended Shoes
        </h2>
        <h5 class="is-size-5 has-text-centered">
          Recommended shoes just for you
        </h5>
        <hr />
        <div class="columns">
          <div class="column">
            <p>
              These shoes that you do not own, were rated very highly by other
              users with a
              <em>{{ user.get_foot_shape }}</em> foot shape.
            </p>
          </div>
        </div>
        <div class="columns is-multiline is-mobile">
          <div
            v-for="(recommendation, index) in user.recommendations_by_shape"
            :key="index"
            class="column is-half-mobile is-half-tablet is-one-third-desktop"
          >
            <div class="columns is-vcentered">
              <div class="column is-full-mobile is-one-quarter-tablet">
                <div class="item_block_image">
                  <span>
                    <v-lazy-image
                      class="lazyload"
                      loading="lazy"
                      :src-placeholder="
                        '/images/placeholder_' +
                        recommendation.item.type +
                        '.png'
                      "
                      :src="recommendation.item.shoe_image"
                      :alt="
                        recommendation.item.brand['name'] +
                        ' ' +
                        recommendation.item.model
                      "
                    />
                  </span>
                </div>
              </div>
              <div v-if="recommendation.item.stats.count > 0" class="column">
                <h4 class="is-size-5 is-capitalized has-text-info">
                  <NuxtLink
                    class="has-text-info"
                    :to="{
                      name: 'shoes-brand-model',
                      params: {
                        brand: recommendation.item.brand['name_slug'],
                        model: recommendation.item.model_slug,
                      },
                    }"
                    >{{ recommendation.item.model }}</NuxtLink
                  >
                </h4>
                <h5 class="is-size-6 is-capitalized has-text-info">
                  <NuxtLink
                    class="has-text-info"
                    :to="{
                      name: 'shoes-brand',
                      params: {
                        brand: recommendation.item.brand['name_slug'],
                      },
                    }"
                  >
                    {{ recommendation.item.brand['name'] }}</NuxtLink
                  >
                </h5>
                <h4 class="is-size-6 is-capitalized is-italic has-text-grey">
                  {{ recommendation.item.gender.name_pretty }}
                  {{ recommendation.item.type }} Shoe
                </h4>
              </div>
              <div class="column is-narrow">
                <form
                  :id="'form_' + recommendation.item.id"
                  action="/match/"
                  method="get"
                >
                  <input
                    type="hidden"
                    name="want_item_id"
                    :value="recommendation.item.id"
                  />
                  <button
                    type="submit"
                    class="button is-info is-small is-pulled-right"
                  >
                    Find My Size
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'RecommendationsByShape',
  components: {},
  data() {
    return {};
  },
  computed: {
    ...mapGetters(['profile', 'user']),
  },
};
</script>

<style scoped lang="scss">
.icon {
  font-size: 32px;
  float: left;
  color: $aqua;
  opacity: 0.25;
  width: 25px;
}
.info {
  float: left;
  margin-left: 0.55em;
}
span.info-label {
  display: block;
  clear: both;
}
img.icon {
  margin-top: 12px;
}
.item_block_image {
  margin: 0 auto;
  margin-top: 0.25em;
  position: relative;
  // width: 160px;
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
