<template>
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
            <ItemListSearchSort
              pagetype="comments"
              :sort-order="sort_order"
              @sortOrder="changeSortOrder"
              @sortItems="changeSortValue"
            ></ItemListSearchSort>
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
              >{{ comment.size_standard }}
              {{ shoe.gender['name_pretty'] }}</span
            >
          </div>
          <div class="column comment_info_block">
            <div class="columns">
              <div class="column">
                <p>
                  &quot;<em>{{ comment.comments }}</em
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
            <div
              class="is-flex is-flex-direction-row is-flex-wrap-wrap is-justify-content-space-between"
            >
              <div class="is-flex-shrink-0">
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
              <div class="is-flex-shrink-0">
                <span class="icon-wrapper">
                  <img src="/images/icon_fit.png" alt="shoe fit icon" />
                </span>
                <div class="info">
                  <span class="info_label has-text-grey">Fit&nbsp;</span>
                  <span>
                    <strong>{{ comment.fit_descriptor }}</strong>
                  </span>
                </div>
              </div>
              <div class="is-flex-shrink-0">
                <span class="icon-wrapper">
                  <img
                    src="/images/icon_footshape.png"
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

        <Pagination
          :total="getComments.length"
          :per-page="10"
          noun="comments"
          :current-page="currentPage"
          @pagechanged="onPageChange"
        />
      </template>
    </div>
  </div>
</template>

<script>
import SvgIcon from '@/components/SvgIcon';
import ItemListSearchSort from '@/components/ItemListSearchSort';
import Pagination from '@/components/Pagination';

export default {
  name: 'ShoeComments',
  components: { ItemListSearchSort, SvgIcon, Pagination },
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
      currentPage: 1,
      startIndex: 0,
      endIndex: 9,
    };
  },
  computed: {
    paginatedComments() {
      return this.getComments.slice(this.startIndex, this.endIndex + 1);
    },
    getComments() {
      // deep copy of comments
      let commentsFiltered = JSON.parse(JSON.stringify(this.comments));

      // Sorting
      if (this.sort !== '') {
        const vueSort = this.sort;
        if (this.sort_order === 'desc') {
          if (
            vueSort === 'user.get_foot_shape' ||
            vueSort === 'fit_descriptor'
          ) {
            // sort alpha
            commentsFiltered = commentsFiltered.sort((a, b) => {
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA > textB) return -1;
              if (textA < textB) return 1;
              return 0;
            });
          } else {
            commentsFiltered = commentsFiltered.sort(
              (a, b) => b[vueSort] - a[vueSort]
            );
          }
        }
        if (this.sort_order === 'asc') {
          if (
            vueSort === 'user.get_foot_shape' ||
            vueSort === 'fit_descriptor'
          ) {
            // sort alpha
            commentsFiltered = commentsFiltered.sort((a, b) => {
              const textA = this.deepFind(a, vueSort).toUpperCase();
              const textB = this.deepFind(b, vueSort).toUpperCase();
              if (textA < textB) return -1;
              if (textA > textB) return 1;
              return 0;
            });
          } else {
            commentsFiltered = commentsFiltered.sort(
              (a, b) => a[vueSort] - b[vueSort]
            );
          }
        }
      }

      this.resetPages();

      return commentsFiltered;
    },
  },
  methods: {
    resetPages() {
      this.currentPage = 1;
      this.startIndex = 0;
      this.endIndex = 9;
    },
    changeSortOrder(value) {
      this.sort_order = value;
    },
    changeSortValue(value) {
      this.sort = value;
    },
    onPageChange(page, startIndex, endIndex) {
      this.currentPage = page;
      this.startIndex = startIndex;
      this.endIndex = endIndex;
    },
  },
};
</script>

<style scoped lang="scss">
.is-no-top-padding {
  padding-top: 0;
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
  // padding: 0;
  .size {
    height: 55px;
    width: 55px;
    line-height: 55px;
    padding: 0;
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
    margin-bottom: 0;
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
