<template>
  <div class="columns">
    <div class="column">
      <h5 class="has-text-weight-bold">Foot Shape Information</h5>
      <hr />
      <div class="columns is-multiline is-mobile">
        <template v-for="ratings in stats.ratings">
          <div :key="ratings.foot_shape_descriptor_id" class="column is-narrow">
            <div
              class="card has-equal-height"
              :class="{
                'your-size-card':
                  userFootShape == ratings.foot_shape_descriptor_id,
              }"
            >
              <div class="card-content content">
                <div class="columns is-mobile">
                  <div class="column is-narrow">
                    <div
                      class="foot_shape_img"
                      :style="{
                        backgroundImage:
                          'url(/images/footshape/shape' +
                          ratings.foot_shape_descriptor_id +
                          '.jpg)',
                      }"
                    ></div>
                  </div>
                  <div class="column">
                    <h4>{{ ratings.foot_shape_descriptor }}</h4>
                    <h5 class="is-size-7 has-text-grey">Popularity</h5>
                    <h6 class="is-size-7">
                      <strong>{{ ratings.count }}</strong> Users
                    </h6>
                    <h5 class="is-size-7 has-text-grey">Avg. Rating</h5>
                    <h6 class="is-size-7">
                      <strong>{{ ratings.avg_rating }}</strong>
                      <span class="has-text-grey">&nbsp;/ 5</span>
                    </h6>
                  </div>
                </div>
              </div>
              <footer
                v-if="userFootShape == ratings.foot_shape_descriptor_id"
                class="card-footer"
              >
                <h6
                  class="
                    card-footer-item
                    is-size-7
                    has-text-centered
                    is-paddingless
                  "
                >
                  Your Shape
                </h6>
              </footer>
            </div>
          </div>
        </template>
      </div>
      <small class="modal_link is-pulled-left">
        <a type="button" @click.prevent.stop="showFootShapeModal = true"
          >More information about foot shapes</a
        >
      </small>
    </div>
    <!-- modals -->
    <FootShapeModal
      :show="showFootShapeModal"
      @close="showFootShapeModal = false"
    ></FootShapeModal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import FootShapeModal from '@/components/FootShapeModal';

export default {
  name: 'ShoeRatingsByFootShape',
  components: { FootShapeModal },
  props: {
    stats: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      showFootShapeModal: false,
    };
  },
  computed: {
    ...mapGetters(['user']),
    userFootShape() {
      return this.user.foot_shape;
    },
  },
};
</script>

<style scoped lang="scss">
.card-footer {
  color: $white;
  background-color: $aqua;
}

.your-size-card {
  border: 1px solid $aqua;
}

.card-content.content {
  padding: 0.75em;
}

.card .column {
  padding: 0.5em;
}

.foot_shape_img {
  height: 60px;
  width: 22px;
  background-position-x: -18px;
  background-size: cover;
  background-position-y: -3px;
  background-repeat: no-repeat;
}
</style>
