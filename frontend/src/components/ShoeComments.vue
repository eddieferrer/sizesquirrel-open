<template>
  <ComponentLoader :loading-component="false" :failed-to-load="false">
    <div class="columns">
      <div class="column">
        <h5 class="has-text-weight-bold">User Comments</h5>
        <hr />
        <div v-if="getComments.length == 0">
          <span class="has-text-grey">No Comments</span>
        </div>
        <template v-if="getComments.length != 0">
          <div class="columns">
            <div class="column">
              <ItemListSearchSort pagetype="comments" :sort-order="sort_order"></ItemListSearchSort>
            </div>
          </div>
          <div
            v-for="(comment, index) in paginatedComments"
            :key="`comment-${index}`"
            class="columns is-multiline is-clearfix"
          >
            <div class="column is-narrow has-text-centered size_gender">
              <span class="size">{{ comment.size }}</span>
              <span class="is-size-7"
                >{{ comment.size_standard }} {{ shoe.gender['name_pretty'] }}</span
              >
            </div>
            <div class="column comment_info_block">
              <div class="columns">
                <div class="column">
                  <p>
                    &quot;
                    <em>{{ comment.comments }}</em
                    >&quot;
                    <br />
                    <RouterLink
                      :to="{
                        name: 'profile',
                        params: { username: comment.user.username },
                      }"
                      >{{ comment.user.username }}</RouterLink
                    >
                  </p>
                </div>
              </div>
              <div class="columns is-mobile">
                <div class="column is-narrow is-no-top-padding">
                  <span class="icon-wrapper">
                    <svg-icon icon="fi-star"></svg-icon>
                  </span>
                  <div class="info">
                    <span class="info_label has-text-grey">Rating&nbsp;</span>
                    <span>
                      <strong>{{ comment.rating }}</strong>
                      <span class="has-text-grey">/ 5</span>
                    </span>
                  </div>
                </div>
                <div class="column is-narrow is-no-top-padding">
                  <span class="icon-wrapper">
                    <img src="/static/images/icon_fit.png" alt="shoe fit icon" />
                  </span>
                  <div class="info">
                    <span class="info_label has-text-grey">Fit&nbsp;</span>
                    <span>
                      <strong>{{ comment.fit_descriptor }}</strong>
                    </span>
                  </div>
                </div>
                <div class="column is-narrow is-no-top-padding">
                  <span class="icon-wrapper">
                    <img
                      src="/static/images/icon_footshape.png"
                      alt="foot shape icon"
                      class="footshape"
                    />
                  </span>
                  <div class="info">
                    <span class="info_label has-text-grey">Foot shape&nbsp;</span>
                    <span>
                      <strong>{{ comment.user.get_foot_shape }}</strong>
                      <span class="has-text-grey"></span>
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div class="column is-12 is-no-top-padding">
              <hr />
            </div>
          </div>
          <div v-if="numberOfPages > 1" class="columns is-centered">
            <div class="column is-10 has-text-centered">
              Showing {{ startIndex + 1 }} - {{ endIndex }} of {{ getComments.length }} comments
              <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                <ul class="pagination-list">
                  <li>
                    <a
                      class="pagination-link"
                      aria-label="Go to previous"
                      :disabled="active_page == 1 ? true : false"
                      @click.prevent.stop="
                        active_page != 1 ? (active_page = active_page - 1) : (active_page = 1)
                      "
                      >&laquo;</a
                    >
                  </li>
                  <li v-for="page_number in numberOfPages" :key="page_number">
                    <a
                      class="pagination-link"
                      :class="{ 'is-current': page_number == active_page }"
                      :aria-label="'Goto page ' + page_number"
                      @click.prevent.stop="active_page = page_number"
                      >{{ page_number }}</a
                    >
                  </li>
                  <li>
                    <a
                      class="pagination-link"
                      aria-label="Go to next"
                      :disabled="active_page == numberOfPages ? true : false"
                      @click.prevent.stop="active_page = active_page + 1"
                      >&raquo;</a
                    >
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </template>
      </div>
    </div>
  </ComponentLoader>
</template>

<script>
import { mapGetters } from 'vuex';

import SvgIcon from '@/components/SvgIcon';
import ComponentLoader from '@/components/ComponentLoader';

import ItemListSearchSort from '@/components/ItemListSearchSort';

export default {
  name: 'ShoeComments',
  components: { ItemListSearchSort, ComponentLoader, SvgIcon },
  props: {
    comments: {
      type: Array,
      default() {
        return [];
      },
    },
    shoe: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      sort: 'rating',
      sort_order: 'desc',
      active_page: 1,
    };
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.getComments.length / 10);
    },
    ...mapGetters(['urlContextModelIdList']),
    startIndex() {
      return (this.active_page - 1) * 10;
    },
    endIndex() {
      if (this.startIndex + 10 > this.getComments.length) {
        return this.getComments.length;
      }
      return this.startIndex + 10;
    },
    paginatedComments() {
      return this.getComments.slice(this.startIndex, this.endIndex);
    },
    getComments() {
      let commentsFiltered = this.comments;

      // Sorting
      if (this.sort !== '') {
        const vueSort = this.sort;
        if (this.sort_order === 'desc') {
          if (vueSort === 'user.get_foot_shape' || vueSort === 'fit_descriptor') {
            // sort alpha
            commentsFiltered = commentsFiltered.sort((a, b) => {
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA > textB) return -1;
              if (textA < textB) return 1;
              return 0;
            });
          } else {
            commentsFiltered = commentsFiltered.sort((a, b) => b[vueSort] - a[vueSort]);
          }
        }
        if (this.sort_order === 'asc') {
          if (vueSort === 'user.get_foot_shape' || vueSort === 'fit_descriptor') {
            // sort alpha
            commentsFiltered = commentsFiltered.sort((a, b) => {
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA < textB) return -1;
              if (textA > textB) return 1;
              return 0;
            });
          } else {
            commentsFiltered = commentsFiltered.sort((a, b) => a[vueSort] - b[vueSort]);
          }
        }
      }

      this.resetPages();

      return commentsFiltered;
    },
  },
  created() {
    this.$on('sortOrder', (value) => {
      this.sort_order = value;
    });
    this.$on('sortItems', (value) => {
      this.sort = value;
    });
  },
  methods: {
    resetPages() {
      this.active_page = 1;
    },
  },
};
</script>

<style scoped lang="scss">
.pagination {
  margin-top: 0.65em;
}
.is-no-top-padding {
  padding-top: 0px;
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
}
.size_gender {
  // padding: 0px;
  .size {
    height: 55px;
    width: 55px;
    line-height: 55px;
    padding: 0px;
    font-size: 24px;
  }
}
// fms block & result_item_block & comment blocks
.item_block_info.fms_block,
.item_block_info.result_item_block,
.comment_info_block,
.user_details {
  .info_label {
    font-size: 90%;
    margin-bottom: 0px;
  }
  .icon-wrapper {
    .footshape {
      height: 34px;
    }
  }
  .info {
    float: left;
    margin-left: 0.65em;
  }
  span.info_label {
    display: block;
    clear: both;
  }
}
</style>
