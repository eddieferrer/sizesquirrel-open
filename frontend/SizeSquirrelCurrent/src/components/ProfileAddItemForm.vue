<template>
  <div class="columns is-centered">
    <div class="column is-three-quarters-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">Add A Shoe</h2>
      <h5 class="is-size-5 has-text-centered">Add a shoe to your profile</h5>
      <hr />
      <form id="user_item_form" @submit.prevent="addProfileItem">
        <div class="columns is-centered">
          <div class="column is-two-thirds-desktop">
            <MultiSelectItems :key="itemSelectKey" v-model="item"></MultiSelectItems>
          </div>
        </div>
        <div v-if="item" class="user_item_form_step2">
          <div class="columns">
            <div class="column">
              <div class="field">
                <label class="label has-text-weight-normal has-text-grey">Size</label>
                <div class="control">
                  <MultiSelectSize v-model="size"></MultiSelectSize>
                  <p class="help is-default">Use your keyboard to quickly input a size</p>
                </div>
              </div>
              <div class="field">
                <label class="label has-text-weight-normal has-text-grey">Rating</label>
                <div class="control">
                  <MultiSelectRating v-model="rating"></MultiSelectRating>
                </div>
                <p class="help is-default">Your subjective overall rating of these shoes</p>
              </div>
              <div class="field">
                <label class="label has-text-weight-normal has-text-grey">Fit</label>
                <div class="control">
                  <MultiSelectFit v-model="fit"></MultiSelectFit>
                </div>
              </div>
            </div>
            <div class="column">
              <div class="field">
                <label class="label has-text-weight-normal has-text-grey">Comments</label>
                <div class="control">
                  <textarea
                    v-model="comments"
                    class="textarea"
                    name="comments"
                    cols="30"
                    maxlength="700"
                    style="height: 215px"
                  ></textarea>
                </div>
              </div>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <button
                type="submit"
                name="button"
                class="button is-info is-normal is-marginless is-pulled-right"
                :disabled="isFormSubmitting || !isFormValid"
              >
                Add Shoe<span v-if="isFormSubmitting" class="loading"></span>
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import MultiSelectSize from '@/components/MultiSelectSize';
import MultiSelectRating from '@/components/MultiSelectRating';
import MultiSelectFit from '@/components/MultiSelectFit';
import MultiSelectItems from '@/components/MultiSelectItems';

export default {
  name: 'ProfileAddItemForm',
  components: {
    MultiSelectSize,
    MultiSelectRating,
    MultiSelectFit,
    MultiSelectItems,
  },
  data() {
    return {
      item: null,
      rating: null,
      comments: '',
      fit: null,
      size: null,
      isFormSubmitting: false,
      itemSelectKey: 1,
    };
  },
  computed: {
    ...mapGetters(['allitems']),
    isFormValid() {
      if (this.item && this.rating && this.comments && this.fit && this.size) {
        return true;
      }
      return false;
    },
  },
  created() {
    const vm = this;
    this.$root.$on('openFootShapeModal', () => {
      vm.showFootShapeModal = true;
    });
    this.$root.$on('openChangePasswordModal', () => {
      vm.showChangePasswordModal = true;
    });
    this.$root.$on('openDeleteAccountModal', () => {
      vm.showDeleteAccountModal = true;
    });
  },
  methods: {
    resetForm() {
      Object.assign(this.$data, this.$options.data());
    },
    addProfileItem() {
      this.isFormSubmitting = true;

      const addItemComponent = this;

      this.$store
        .dispatch('ADD_PROFILE_ITEM', {
          itemId: this.item.id,
          rating: this.rating.id,
          comments: this.comments,
          fit: this.fit.id,
          size: this.size.value,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            addItemComponent.$store.dispatch('SHOW_FLASH_MESSAGE', {
              class: 'has-background-success',
              message: response.data.message,
            });
            window.scrollTo(0, 0);
            addItemComponent.resetForm();
            addItemComponent.itemSelectKey = Math.random();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.log(error);
        })
        .finally(() => {
          this.isFormSubmitting = false;
        });
    },
  },
};
</script>

<style scoped></style>
