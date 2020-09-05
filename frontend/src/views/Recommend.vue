<template>
  <div>
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">Recommend</h2>
        <h5 class="is-size-5 has-text-centered">Let us recommend a shoe for you</h5>
        <hr />
      </div>
    </div>
    <div class="columns is-centered">
      <div class="column">
        <ul class="steps is-narrow is-medium is-centered has-content-centered">
          <li
            class="steps-segment"
            :class="{ 'is-active': currentStep == 1, 'has-gaps': currentStep <= 1 }"
          >
            <span class="steps-marker">
              1
            </span>
            <div class="steps-content">
              <h4 class="step-heading">Gender</h4>
            </div>
          </li>
          <li
            class="steps-segment"
            :class="{ 'is-active': currentStep == 2, 'has-gaps': currentStep <= 2 }"
          >
            <span class="steps-marker">
              2
            </span>
            <div class="steps-content">
              <h4 class="step-heading">Foot Shape</h4>
            </div>
          </li>
          <!-- <li
            class="steps-segment"
            :class="{ 'is-active': currentStep == 3, 'has-gaps': currentStep <= 3 }"
          >
            <span class="steps-marker">
              3
            </span>
            <div class="steps-content">
              <h4 class="step-heading">Climbing Skill</h4>
            </div>
          </li> -->
          <li
            class="steps-segment"
            :class="{ 'is-active': currentStep == 3, 'has-gaps': currentStep <= 3 }"
          >
            <span class="steps-marker">
              <span>
                <svg-icon icon="fi-check"></svg-icon>
              </span>
            </span>
            <div class="steps-content">
              <h4 class="step-heading">Your Shoe</h4>
            </div>
          </li>
        </ul>
        <form
          id="recommend_a_shoe_form"
          class="columns is-centered"
          @submit.prevent="recommendShoe"
        >
          <!-- Step 1 -->
          <div v-show="currentStep == 1" class="column is-full-mobile is-three-quarters-tablet">
            <h3 class="is-size-5 has-text-centered has-text-primary">Step 1</h3>
            <section class="card modal-card-body">
              <div class="columns">
                <div class="column is-narrow">
                  <div class="field">
                    <label class="label has-text-weight-normal">Select a Gender</label>
                    <div class="control">
                      <MultiSelectMinimal
                        v-model="gender"
                        :options="gender_options"
                        placeholder="Gender"
                        name="gender"
                      ></MultiSelectMinimal>
                    </div>
                  </div>
                </div>
                <div class="is-divider-vertical"></div>
                <div class="column why-text">
                  <p>Why?</p>
                  <p>
                    Some models of shoes are designed with a specific gender in mind.
                  </p>
                  <p>
                    Male shoes typically tend to accomodate a higher volume foot. Some models will
                    additionally have the 'HV' designation for 'High Volume'. Womens shoes are
                    typically designed for lower volume and will sometimes have the designation 'LV'
                    for 'Low Volume'.
                  </p>
                </div>
              </div>
              <div class="columns">
                <div class="column">
                  <button
                    type="button"
                    :disabled="!gender"
                    class="button is-pulled-right is-info"
                    @click="goToStep(2)"
                  >
                    Next
                  </button>
                </div>
              </div>
            </section>
          </div>
          <!-- Step 2 -->
          <div v-show="currentStep == 2" class="column is-full-mobile is-three-quarters-tablet">
            <h3 class="is-size-5 has-text-centered has-text-primary">Step 2</h3>
            <section class="card modal-card-body">
              <div class="columns">
                <div class="column is-narrow">
                  <div class="field">
                    <label class="label has-text-weight-normal">Foot Shape</label>
                    <div class="control">
                      <MultiSelectMinimal
                        v-model="footShape"
                        :options="foot_shape_options"
                        placeholder="Foot Shape"
                        name="foot_shape"
                        :max-height="250"
                      ></MultiSelectMinimal>
                    </div>
                  </div>
                </div>
                <div class="is-divider-vertical"></div>
                <div class="column why-text">
                  <p>Why?</p>
                  <p>
                    A combination of the last shape, toe box shape, and shoe volume will affect the
                    way a shoe fits for each foot shape.
                  </p>
                  <p>
                    There are five basic foot shapes: Egyptian, Roman, Greek, Germanic and Celtic.
                  </p>
                  <p>
                    Egyptian, Roman and Greek are by far the most popular foot shapes. If your feet
                    are Germanic or Celtic shaped, we may have trouble recommending a shoe.
                  </p>
                  <p class="is-info">
                    <a type="button" @click.prevent.stop="openFootShapeModal()"
                      >More information about foot shapes</a
                    >
                  </p>
                </div>
              </div>
              <div class="columns">
                <div class="column level">
                  <a
                    class="is-pulled-left previous-link"
                    type="button"
                    @click.prevent.stop="goToStep(1)"
                    >Previous</a
                  >
                  <button
                    type="submit"
                    :disabled="isFormSubmitting"
                    class="button is-pulled-right is-info"
                  >
                    Recommend A Shoe<span v-if="isFormSubmitting" class="loading"></span>
                  </button>
                  <!-- <button
                    type="button"
                    :disabled="!footShape"
                    class="button is-pulled-right is-info"
                    @click="goToStep(3)"
                  >
                    Next
                  </button> -->
                </div>
              </div>
            </section>
          </div>
          <!-- Step 3 
          <div v-show="currentStep == 3" class="column is-full-mobile is-three-quarters-tablet">
            <h3 class="is-size-5 has-text-centered has-text-primary">Step 3</h3>
            <section class="card modal-card-body">
              <div class="columns">
                <div class="column is-narrow">
                  <h4 class="is-size-6 has-text-weight-bold">Climbing</h4>
                  <div class="field">
                    <label class="label has-text-weight-normal">Boulder</label>
                    <div class="control">
                      <MultiSelectMinimal
                        v-model="boulderingSkill"
                        :options="boulder_options"
                        placeholder="Bouldering"
                        name="climbing_boulder"
                      ></MultiSelectMinimal>
                    </div>
                  </div>
                  <div class="field">
                    <label class="label has-text-weight-normal">Sport</label>
                    <div class="control">
                      <MultiSelectMinimal
                        v-model="sportSkill"
                        :options="sport_trad_options"
                        placeholder="Sport"
                        name="climbing_sport"
                      ></MultiSelectMinimal>
                    </div>
                  </div>
                  <div class="field">
                    <label class="label has-text-weight-normal">Trad</label>
                    <div class="control">
                      <MultiSelectMinimal
                        v-model="tradSkill"
                        :options="sport_trad_options"
                        placeholder="Trad"
                        name="climbing_trad"
                      ></MultiSelectMinimal>
                    </div>
                  </div>
                </div>
                <div class="is-divider-vertical"></div>
                <div class="column why-text">
                  <p>Why?</p>
                  <p>
                    Climbing Skill
                  </p>
                  <p>
                    Climbing Skill
                  </p>
                </div>
              </div>
              <div class="columns">
                <div class="column">
                  <a
                    class="is-pulled-left previous-link"
                    type="button"
                    @click.prevent.stop="goToStep(2)"
                    >Previous</a
                  >
                  <button
                    type="submit"
                    :disabled="isFormSubmitting"
                    class="button is-pulled-right is-info"
                  >
                    Recommend A Shoe<span v-if="isFormSubmitting" class="loading"></span>
                  </button>
                </div>
              </div>
            </section>
          </div>
          -->
          <!-- Step 4 -->
          <div v-show="currentStep == 3" class="column is-full-mobile is-three-quarters-tablet">
            <section>
              <recommended-shoes-cards :shoes="recommendedShoes" />
              <div class="has-text-centered">
                <button
                  type="button"
                  :disabled="false"
                  class="button is-info is-medium"
                  @click="startOver"
                >
                  Start Over
                </button>
              </div>
            </section>
          </div>
        </form>
        <!-- modals -->
        <FootShapeModal
          :show="showFootShapeModal"
          @close="showFootShapeModal = false"
        ></FootShapeModal>
      </div>
    </div>
  </div>
</template>

<script>
import FootShapeModal from '@/components/FootShapeModal';

import MultiSelectMinimal from '@/components/MultiSelectMinimal';
import RecommendedShoesCards from '@/components/RecommendedShoesCards';
import SvgIcon from '@/components/SvgIcon';

import SportTradOptions from '@/mixins/SportTradOptions';
import BoulderOptions from '@/mixins/BoulderOptions';
import FootShapeOptions from '@/mixins/FootShapeOptions';
import GenderOptions from '@/mixins/GenderOptions';

export default {
  name: 'Recommend',
  components: { MultiSelectMinimal, FootShapeModal, RecommendedShoesCards, SvgIcon },
  mixins: [SportTradOptions, BoulderOptions, FootShapeOptions, GenderOptions],
  data() {
    return {
      isFormSubmitting: false,
      showFootShapeModal: false,
      footShape: null,
      gender: null,
      currentStep: 1,
      recommendedShoes: [],
      // TODO
      boulderingSkill: null,
      sportSkill: null,
      tradSkill: null,
    };
  },
  metaInfo() {
    return {
      // title will be injected into parent titleTemplate
      title: 'Recommend A Shoe',
    };
  },
  methods: {
    startOver() {
      this.goToStep(1);
      this.footShape = null;
      this.gender = null;
      this.boulderingSkill = null;
      this.sportSkill = null;
      this.tradSkill = null;
      this.recommendedShoes = [];
    },
    goToStep(step) {
      this.currentStep = step;
    },
    openFootShapeModal() {
      this.showFootShapeModal = true;
    },
    recommendShoe() {
      this.isFormSubmitting = true;

      this.$store
        .dispatch('RECOMMEND_A_SHOE', {
          footShape: this.footShape,
          gender: this.gender,
        })
        .then((response) => {
          this.recommendedShoes = response.data.items;
          this.goToStep(3);
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

<style scoped lang="scss">
label[for='username'],
label[for='email'],
label[for='gender'],
label[for='street_shoe_size'],
label[for='foot_shape'],
label[for='split_shoe_sizing'] {
  margin-bottom: 1em;
}
h4.step-heading {
  // margin-top: 1px;
  letter-spacing: 1px;
  text-transform: uppercase;
  font-size: 0.85rem;
}
.why-text {
  p {
    margin-bottom: 1em;
  }
}
.multiselect {
  width: 220px;
}
.previous-link {
  margin-top: 0.65em;
}
h3 {
  margin-bottom: 0.75rem;
}
.is-active {
  .steps-marker {
    color: $white;
    fill: $white;
  }
}
</style>
