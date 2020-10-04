<template>
  <div class="columns is-centered">
    <div class="column">
      <!-- found a match -->
      <div v-if="matchResultsLength > 0 && streetResults.length > 0" class="columns">
        <div class="column">
          <h5 class="has-text-weight-bold">Size Based On Street Shoe Sizing</h5>
          <hr />
          <h6>
            Recommended Size:
            <strong
              >{{ streetResults[0].size_standard[targetItem.short_size_standard] }}
              {{ streetResults[0].size }} {{ targetItem.brand['sizing'] }}
              {{ targetItem.gender['name_pretty'] }}</strong
            >
          </h6>
          <h6>
            Percentage:
            <strong>{{ streetResults[0].percentage }}%</strong> of users with your same street shoe
            size wear this size.
          </h6>
          <progress
            style="margin-bottom: 0px;"
            :class="getClass(streetResults[0].percentage)"
            class="progress"
            :value="streetResults[0].percentage"
            max="100"
            >{{ streetResults[0].percentage }}%</progress
          >
          <h6>
            Accuracy:
            <strong>
              <span class="has-text-warning">Low</span>
            </strong>
          </h6>
          <small
            >Street shoe sizing varies more than we would like and we think this type of match is
            inherently not very accurate</small
          >
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <ShoeRatingsByFootShape :stats="targetItem.stats"></ShoeRatingsByFootShape>
        </div>
      </div>

      <div v-if="matchResultsLength > 0" class="columns">
        <div class="column">
          <h5 class="has-text-weight-bold">Size Based On Individual Shoes</h5>
          <hr />
          <div class="columns is-multiline">
            <div
              v-for="(grouped_result, index) in groupedMatchUsers"
              :key="index"
              class="column is-12"
            >
              <div class="box has-background-light">
                <p>
                  Based on the
                  <strong>{{ grouped_result['shoe'].model | titleCase }}</strong> you should get the
                  <strong
                    >{{ targetItem.brand['name'] | titleCase }}
                    {{ targetItem.model | titleCase }}</strong
                  >
                  in size
                  <strong
                    >{{ grouped_result.most_common_size[targetItem.short_size_standard] }}
                    {{ targetItem.brand['sizing'] }}
                    {{ targetItem.gender['name_pretty'] }}</strong
                  >
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <ShoeComments :shoe="targetItem" :comments="comments" />
        </div>
      </div>

      <!-- no match found -->
      <div v-if="matchResultsLength == 0 && streetResults.length > 0" class="columns">
        <div class="column">
          <h5>Match by Street Shoe Sizing</h5>
          <hr />
          <h6>
            <strong>Recommended Size:</strong>
            {{ streetResults[0].size }} {{ targetItem.brand['sizing'] }}
            {{ targetItem.gender['name'] }}{% if targetItem.gender['name'] == 'men' or
            targetItem.gender['name'] == 'women'%}'s{% endif %}
          </h6>
          <h6>
            <strong>Percentage:</strong>
            {{ streetResults[0].percentage }}%
          </h6>
          <div :class="getClass(streetResults[0].percentage)">
            <span class="meter" :style="{ width: streetResults[0].percentage + '%' }"></span>
          </div>
          <h6>
            <strong>Accuracy:</strong>
            <span class="span-alert">Low</span>
          </h6>
          <small
            >Street shoe sizing varies more than we would like and we think this type of match is
            inherently not very accurate</small
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { titleCase } from '@/filters';

import ShoeComments from '@/components/ShoeComments';
import ShoeRatingsByFootShape from '@/components/ShoeRatingsByFootShape';

export default {
  name: 'PrivateMatchResult',
  components: {
    ShoeComments,
    ShoeRatingsByFootShape,
  },
  filters: {
    titleCase,
  },
  props: {
    comments: {
      type: Array,
      default() {
        return [];
      },
    },
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
    groupedMatchUsers: {
      type: Array,
      default() {
        return [];
      },
    },
    streetResults: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  computed: {
    matchResultsLength() {
      if (this.matchResults) {
        return this.matchResults.length;
      }
      return 0;
    },
    ...mapGetters(['isAuthenticated']),
  },
};
</script>

<style scoped lang="scss"></style>
