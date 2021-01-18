<template>
  <Modal :modal-size="modalSize" :show="show" @close="closeAndReset">
    <header class="modal-card-head">
      <p class="modal-card-title">Edit Shoe</p>
      <span
        class="close-button is-size-4"
        aria-label="close"
        @click.prevent.stop="closeAndReset"
        >&#215;</span
      >
    </header>
    <form id="edit_item_form" class="modal_form" @submit.prevent="editItem">
      <section class="modal-card-body extra-padding-bottom">
        <div class="columns">
          <div class="column">
            <h3 class="is-capitalized has-text-weight-bold">
              {{ item.item.brand.name }} - {{ item.item.model }}
            </h3>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <div class="field">
              <label class="label has-text-weight-normal has-text-grey"
                >Size</label
              >
              <div class="control">
                <MultiSelectSize v-model="currentSize"></MultiSelectSize>
                <p class="help is-default">
                  Use your keyboard to quickly input a size
                </p>
              </div>
            </div>
            <div class="field">
              <label class="label has-text-weight-normal has-text-grey"
                >Rating</label
              >
              <div class="control">
                <MultiSelectRating v-model="currentRating"></MultiSelectRating>
              </div>
              <p class="help is-default">
                Your subjective overall rating of these shoes
              </p>
            </div>
            <div class="field">
              <label class="label has-text-weight-normal has-text-grey"
                >Fit</label
              >
              <div class="control">
                <MultiSelectFit
                  v-model="currentFit"
                  open-direction="top"
                ></MultiSelectFit>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="field">
              <label class="label has-text-weight-normal has-text-grey"
                >Comments</label
              >
              <div class="control">
                <textarea
                  v-model="item.comments"
                  name="comments"
                  maxlength="700"
                  style="height: 237px"
                ></textarea>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="modal-card-body">
        <button
          type="submit"
          name="button"
          class="button is-info is-pulled-right"
          :disabled="isFormSubmitting"
        >
          Save<span v-if="isFormSubmitting" class="loading"></span>
        </button>
        <button
          class="button is-pulled-left"
          @click.prevent.stop="closeAndReset"
        >
          Cancel
        </button>
      </section>
    </form>
  </Modal>
</template>

<script>
import SizeOptions from '@/mixins/SizeOptions';
import RatingOptions from '@/mixins/RatingOptions';
import FitOptions from '@/mixins/FitOptions';

import Modal from '@/components/Modal';
import MultiSelectSize from '@/components/MultiSelectSize';
import MultiSelectRating from '@/components/MultiSelectRating';
import MultiSelectFit from '@/components/MultiSelectFit';

export default {
  name: 'EditItemModal',
  components: { Modal, MultiSelectSize, MultiSelectRating, MultiSelectFit },
  mixins: [SizeOptions, RatingOptions, FitOptions],
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    item: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      modalSize: 'small',
      isFormSubmitting: false,
      originalItemValue: {},
    };
  },
  computed: {
    currentSize: {
      get() {
        if (this.item.size) {
          const reducedArray = this.size_option_groups[0].sizes.concat(
            this.size_option_groups[1].sizes
          );
          return reducedArray.filter(
            (sizeArray) => sizeArray.value === this.item.size.toString()
          )[0];
        }
        return {};
      },
      set(value) {
        this.item.size = value.value;
      },
    },
    currentRating: {
      get() {
        if (this.item.rating) {
          return this.rating_options.filter(
            (ratingArray) => ratingArray.id === this.item.rating.toString()
          )[0];
        }
        return {};
      },
      set(value) {
        this.item.rating = value.id;
      },
    },
    currentFit: {
      get() {
        if (this.item.fit) {
          return this.fit_options.filter(
            (fitArray) => fitArray.id === this.item.fit.toString()
          )[0];
        }
        return {};
      },
      set(value) {
        this.item.fit = value.id;
      },
    },
  },
  watch: {
    item(newVal) {
      // store value for reset
      this.originalItemValue = { ...newVal };
    },
  },
  methods: {
    closeAndReset() {
      // reset item
      this.item.size = this.originalItemValue.size;
      this.item.rating = this.originalItemValue.rating;
      this.item.comments = this.originalItemValue.comments;
      this.item.fit = this.originalItemValue.fit;
      this.close();
    },
    close() {
      this.$emit('close');
    },
    editItem() {
      this.isFormSubmitting = true;

      const editItemModalComponent = this;

      this.$store
        .dispatch('EDIT_PROFILE_ITEM', {
          userItemId: this.item.id,
          rating: this.item.rating,
          size: this.item.size,
          fit: this.item.fit,
          comments: this.item.comments,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            // update properties of item
            editItemModalComponent.item.fit_descriptor =
              response.data.user_item.fit_descriptor;
            editItemModalComponent.close();
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

<style scoped>
textarea {
  width: 100%;
  padding: 0.5em;
}
.extra-padding-bottom {
  padding-bottom: 3.25rem;
}
</style>
