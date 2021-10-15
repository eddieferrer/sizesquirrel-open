<template>
  <div class="columns">
    <div class="column">
      <template v-if="isMyProfile">
        <h2 class="is-size-4 has-text-centered has-text-primary">Your Shoes</h2>
        <h5 class="is-size-5 has-text-centered">Shoes you own</h5>
        <hr />
      </template>
      <template v-if="!isMyProfile">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          {{ profile.username }}'s Shoes
        </h2>
        <h5 class="is-size-5 has-text-centered">Shoes they own</h5>
        <hr />
        <div v-if="getItems.length == 0" class="columns">
          <div class="column">
            <p>{{ profile.username }} doesn't have any shoes.</p>
          </div>
        </div>
      </template>
      <div v-if="getItems.length !== 0" class="columns">
        <div class="column">
          <ItemListSearchSort
            pagetype="profile"
            :sort-order="sort_order"
            @sortOrder="changeSortOrder"
            @sortItems="changeSortValue"
          ></ItemListSearchSort>
          <div class="columns is-multiline">
            <div
              v-for="user_item in paginatedItems"
              :id="'item_' + user_item.user_item.id"
              :key="user_item.user_item.id"
              class="column is-full"
            >
              <div class="columns">
                <div
                  class="
                    column
                    is-one-fifth-desktop is-one-quarter-tablet is-full-mobile
                  "
                >
                  <div class="item_block_image">
                    <span>
                      <v-lazy-image
                        class="lazyload"
                        loading="lazy"
                        :src-placeholder="
                          '/images/placeholder_' +
                          user_item.user_item.item.type +
                          '.png'
                        "
                        :src="user_item.user_item.item.shoe_image"
                        :alt="
                          user_item.user_item.item.brand.name +
                          user_item.user_item.item.model
                        "
                      />
                    </span>
                  </div>
                </div>
                <div class="column">
                  <div class="columns">
                    <div class="column">
                      <h2
                        class="
                          is-size-4 is-capitalized
                          has-text-centered-mobile
                        "
                      >
                        <NuxtLink
                          class="has-text-info"
                          :to="{
                            name: 'shoes-brand-model',
                            params: {
                              brand: user_item.user_item.item.brand.name_slug,
                              model: user_item.user_item.item.model_slug,
                            },
                          }"
                          >{{ user_item.user_item.item.model }}</NuxtLink
                        >
                      </h2>
                      <h4
                        class="
                          is-size-5 is-capitalized
                          has-text-centered-mobile
                        "
                      >
                        <NuxtLink
                          class="has-text-info"
                          :to="{
                            name: 'shoes-brand',
                            params: {
                              brand: user_item.user_item.item.brand.name_slug,
                            },
                          }"
                          >{{ user_item.user_item.item.brand.name }}</NuxtLink
                        >
                      </h4>
                      <h4
                        class="
                          shoe_type
                          has-text-grey
                          is-italic
                          has-text-centered-mobile
                        "
                      >
                        {{ user_item.user_item.item.gender.name_pretty }}
                        {{ user_item.user_item.item.type | capitalize }} Shoe
                      </h4>
                      <hr />
                      <div class="columns is-mobile">
                        <div
                          class="column is-narrow size_gender has-text-centered"
                        >
                          <span class="size">{{
                            user_item.user_item.size
                          }}</span>
                          <span class="is-size-7"
                            >{{ user_item.user_item.size_standard }}
                            {{
                              user_item.user_item.item.gender['name_pretty']
                            }}</span
                          >
                        </div>
                        <div class="column">
                          <p v-if="user_item.user_item.comments.length > 0">
                            &quot;
                            <em>
                              <span>{{
                                user_item.user_item.comments
                              }}</span> </em
                            >&quot;
                          </p>
                          <p v-if="user_item.user_item.comments.length == 0">
                            <em>
                              <span class="has-text-grey">No Comment</span>
                            </em>
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="columns is-multiline is-mobile">
                    <div class="column is-4">
                      <span class="icon-wrapper">
                        <svg-icon icon="fi-torso"></svg-icon>
                      </span>
                      <div class="info">
                        <span class="info-label is-size-6 has-text-grey"
                          >Rating&nbsp;</span
                        >
                        <span>
                          <strong
                            >{{ user_item.user_item.rating }}&nbsp;</strong
                          >
                          <span class="has-text-grey">/ 5</span>
                        </span>
                      </div>
                    </div>
                    <div class="column is-4">
                      <span class="icon-wrapper">
                        <img src="/images/icon_fit.png" alt="shoe fit icon" />
                      </span>
                      <div class="info">
                        <span class="has-text-grey">Fit&nbsp;</span>
                        <h5 style="clear: both">
                          <strong>{{
                            user_item.user_item.fit_descriptor
                          }}</strong>
                        </h5>
                      </div>
                    </div>
                  </div>
                  <hr class="thin_hr" />
                  <div
                    v-if="isMyProfile"
                    class="columns is-multiline is-mobile"
                  >
                    <div class="column">
                      <a
                        type="button"
                        class="link edit_item"
                        @click.prevent.stop="
                          prepareEditItemModal(user_item.user_item)
                        "
                        >Edit</a
                      >
                    </div>
                    <div class="column">
                      <a
                        type="button"
                        class="delete_item is-pulled-right"
                        @click.prevent.stop="
                          prepareConfirmDeleteModal(user_item.user_item)
                        "
                        >Delete</a
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="numberOfPages > 1" class="columns is-centered">
        <div class="column is-10 has-text-centered">
          Showing {{ startIndex + 1 }} - {{ endIndex }} of
          {{ getItems.length }} items
          <nav
            class="pagination is-centered"
            role="navigation"
            aria-label="pagination"
          >
            <ul class="pagination-list">
              <li>
                <a
                  class="pagination-link"
                  aria-label="Go to previous"
                  :disabled="active_page == 1 ? true : false"
                  @click.prevent.stop="
                    active_page != 1
                      ? (active_page = active_page - 1)
                      : (active_page = 1)
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

      <template v-if="isMyProfile">
        <ProfileAddItemForm></ProfileAddItemForm>
        <!-- modals -->
        <ConfirmDeleteModal
          :show="showConfirmDeleteModal"
          :item="selectedItem"
          @close="showConfirmDeleteModal = false"
        ></ConfirmDeleteModal>
        <EditItemModal
          :show="showEditItemModal"
          :item="selectedItem"
          @close="showEditItemModal = false"
        ></EditItemModal>
      </template>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { capitalize } from '@/filters';

import SvgIcon from '@/components/SvgIcon';
import EditItemModal from '@/components/EditItemModal';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal';
import ItemListSearchSort from '@/components/ItemListSearchSort';
import ProfileAddItemForm from '@/components/ProfileAddItemForm';

export default {
  name: 'ProfileItems',
  filters: {
    capitalize,
  },
  components: {
    EditItemModal,
    ConfirmDeleteModal,
    ItemListSearchSort,
    ProfileAddItemForm,
    SvgIcon,
  },
  props: [],
  data() {
    return {
      sort: 'model',
      sort_order: 'asc',
      active_page: 1,
      selectedItem: {
        item: {
          brand: {
            name: 'Unknown Brand',
          },
          model: 'Unknown Shoe',
        },
        id: null,
      },
      showConfirmDeleteModal: false,
      showEditItemModal: false,
    };
  },
  computed: {
    items() {
      return this.profile.items;
    },
    ...mapGetters(['profile', 'isMyProfile']),
    numberOfPages() {
      return Math.ceil(this.getItems.length / 50);
    },
    startIndex() {
      return (this.active_page - 1) * 50;
    },
    endIndex() {
      if (this.startIndex + 50 > this.getItems.length) {
        return this.getItems.length;
      }
      return this.startIndex + 50;
    },
    paginatedItems() {
      return this.getItems.slice(this.startIndex, this.endIndex);
    },
    getItems() {
      // deep copy of items
      let itemsFiltered = JSON.parse(JSON.stringify(this.items));

      // Sorting
      if (this.sort !== '') {
        const vueSort = this.sort;

        if (this.sort_order === 'desc') {
          itemsFiltered = itemsFiltered.sort((a, b) => {
            if (vueSort === 'model' || vueSort === 'brand.name') {
              // sort alpha
              const textA = this.deepFind(
                a,
                `user_item.item.${vueSort}`
              ).toUpperCase();
              const textB = this.deepFind(
                b,
                `user_item.item.${vueSort}`
              ).toUpperCase();
              if (textA > textB) return -1;
              if (textA < textB) return 1;
              return 0;
            }
            // sort numerically
            return this.deepFind(b, vueSort) - this.deepFind(a, vueSort);
          });
        }
        if (this.sort_order === 'asc') {
          itemsFiltered = itemsFiltered.sort((a, b) => {
            if (vueSort === 'model' || vueSort === 'brand.name') {
              // sort alpha
              const textA = this.deepFind(
                a,
                `user_item.item.${vueSort}`
              ).toUpperCase();
              const textB = this.deepFind(
                b,
                `user_item.item.${vueSort}`
              ).toUpperCase();
              if (textA < textB) return -1;
              if (textA > textB) return 1;
              return 0;
            }
            return this.deepFind(a, vueSort) - this.deepFind(b, vueSort);
          });
        }
      }

      this.resetPages();
      return itemsFiltered;
    },
  },
  methods: {
    prepareConfirmDeleteModal(selectedItem) {
      this.selectedItem = selectedItem;
      this.showConfirmDeleteModal = true;
    },
    prepareEditItemModal(selectedItem) {
      this.selectedItem = selectedItem;
      this.showEditItemModal = true;
    },
    resetPages() {
      this.active_page = 1;
    },
    changeSortOrder(value) {
      this.sort_order = value;
    },
    changeSortValue(value) {
      this.sort = value;
    },
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
    // float: right;
    padding: 7%;
    width: 100%;
    overflow: hidden;
  }
}

.pagination {
  margin-top: 0.65em;
}

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
// fms block & result_item_block & comment blocks
.item_block_info.fms_block,
.item_block_info.result_item_block,
.comment_info_block,
.user_details {
  .info_label {
    font-size: 90%;
    margin-bottom: 0;
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
