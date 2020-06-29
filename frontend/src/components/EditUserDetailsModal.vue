<template>
  <Modal :modal-size="modalSize" :show="show" @close="closeAndReset">
    <header class="modal-card-head">
      <p class="modal-card-title">Change User Details</p>
      <span class="close-button is-size-4" aria-label="close" @click.prevent.stop="closeAndReset"
        >&#215;</span
      >
    </header>
    <form id="edit_user_details_form" class="modal_form" @submit.prevent="editUser">
      <section class="modal-card-body">
        <div v-if="formErrors && showAlert" class="columns">
          <div class="column">
            <div class="level box is-marginless has-background-danger">
              <span class="has-text-white">There was an error changing your account details.</span>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column is-4">
            <h4 class="is-size-6 has-text-weight-bold">User</h4>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Username</label>
              <div class="control">
                <input v-model="user.username" class="input" type="text" name="username" required />
              </div>
              <p v-if="error_username != ''" class="help is-danger">{{ error_username }}</p>
            </div>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Email</label>
              <div class="control">
                <input v-model="user.email" class="input" type="email" name="email" required />
              </div>
              <p v-if="error_email != ''" class="help is-danger">{{ error_email }}</p>
            </div>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Gender</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentGender"
                  :options="gender_options"
                  placeholder="Gender"
                  name="gender"
                ></MultiSelectMinimal>
              </div>
            </div>
            <h4 class="is-size-6 has-text-weight-bold">More</h4>
            <div class="field">
              <p>
                <small v-if="user.provider_id_short == 'ss'">
                  <a type="button" @click.prevent.stop="openChangePasswordModal()"
                    >Change Password</a
                  >
                </small>
                <small v-if="user.provider_id_short == 'fb'"
                  >You registered for SizeSquirrel using your Facebook account.</small
                >
                <br />
                <small>
                  <a type="button" @click.prevent.stop="openDeleteAccountModal()">Delete Account</a>
                </small>
              </p>
            </div>
          </div>

          <div class="column is-5">
            <h4 class="is-size-6 has-text-weight-bold">Sizing</h4>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Street Shoe Size</label>
              <div class="control">
                <MultiSelectSize v-model="streetShoeSize"></MultiSelectSize>
                <p class="help is-info">
                  <span v-if="user.street_shoe_size_in">
                    <span>
                      <strong>{{ user.street_shoe_size['EUR'] }} EUR</strong>&nbsp;|&nbsp;
                    </span>
                    <span>
                      <strong>{{ user.street_shoe_size['USM'] }} USM</strong>&nbsp;|&nbsp;
                    </span>
                    <span>
                      <strong>{{ user.street_shoe_size['USW'] }} USW</strong>&nbsp;|&nbsp;
                    </span>
                    <span>
                      <strong>{{ user.street_shoe_size['UK'] }} UK</strong>&nbsp;
                    </span>
                  </span>
                  <span v-if="!user.street_shoe_size_in">
                    <span>
                      <strong>None</strong>
                    </span>
                  </span>
                </p>
              </div>
            </div>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Foot Shape</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentFootShape"
                  :options="foot_shape_options"
                  placeholder="Foot Shape"
                  name="foot_shape"
                ></MultiSelectMinimal>
                <p class="help is-info">
                  <a type="button" @click.prevent.stop="openFootShapeModal()"
                    >More information about foot shapes</a
                  >
                </p>
              </div>
            </div>

            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Split Shoe Sizing?</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentSplitShoeSizing"
                  :options="split_shoe_sizing_options"
                  placeholder="Split Shoe Sizing"
                  name="split_shoe_info"
                ></MultiSelectMinimal>
                <p class="help">
                  If you wear split shoe sizing, we recommend that you add the larger of the two
                  sizes to your profile
                </p>
              </div>
            </div>
          </div>

          <div class="column is-3">
            <h4 class="is-size-6 has-text-weight-bold">Climbing</h4>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Boulder</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentBoulderingSkill"
                  :options="boulder_options"
                  placeholder="Bouldering"
                  name="climbing_boulder"
                ></MultiSelectMinimal>
              </div>
            </div>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Sport</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentSportSkill"
                  :options="sport_trad_options"
                  placeholder="Sport"
                  name="climbing_sport"
                ></MultiSelectMinimal>
              </div>
            </div>
            <div class="field">
              <label class="label has-text-grey has-text-weight-normal">Trad</label>
              <div class="control">
                <MultiSelectMinimal
                  v-model="currentTradSkill"
                  :options="sport_trad_options"
                  placeholder="Trad"
                  name="climbing_trad"
                ></MultiSelectMinimal>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="modal-card-body">
        <button type="submit" :disabled="isFormSubmitting" class="button is-pulled-right is-info">
          Save<span v-if="isFormSubmitting" class="loading"></span>
        </button>
        <button class="button is-pulled-left" @click.prevent.stop="closeAndReset">Cancel</button>
      </section>
    </form>
  </Modal>
</template>

<script>
import SportTradOptions from '@/mixins/SportTradOptions';
import BoulderOptions from '@/mixins/BoulderOptions';
import SplitShoeSizingOptions from '@/mixins/SplitShoeSizingOptions';
import FootShapeOptions from '@/mixins/FootShapeOptions';
import GenderOptions from '@/mixins/GenderOptions';
import MultiSelectMinimal from './MultiSelectMinimal';
import MultiSelectSize from './MultiSelectSize';
import Modal from './Modal';

export default {
  name: 'EditUserDetailsModal',
  components: { Modal, MultiSelectSize, MultiSelectMinimal },
  mixins: [
    SportTradOptions,
    BoulderOptions,
    SplitShoeSizingOptions,
    FootShapeOptions,
    GenderOptions,
  ],
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    user: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      modalSize: 'medium',
      formErrors: false,
      showAlert: false,
      error_username: '',
      error_email: '',
      isFormSubmitting: false,

      streetShoeSize: null,
      originalUserValues: {},
    };
  },
  computed: {
    currentGender: {
      get() {
        return this.gender_options.find(
          (genderArray) => genderArray.id === this.user.gender.toString()
        );
      },
      set(value) {
        this.user.gender = value.id;
      },
    },
    currentFootShape: {
      get() {
        // In some strange cases user.foot_shape can be null.
        let currentFootShapeObj;
        try {
          currentFootShapeObj = this.foot_shape_options.find(
            (footShapeArray) => footShapeArray.id === this.user.foot_shape.toString()
          );
        } catch {
          // return the default case
          currentFootShapeObj = this.foot_shape_options.find(
            (footShapeArray) => footShapeArray.id === '0'
          );
        }
        return currentFootShapeObj;
      },
      set(value) {
        this.user.foot_shape = value.id;
      },
    },
    currentSplitShoeSizing: {
      get() {
        // In some strange cases user.split_shoe_info can be null.
        let currentSplitObj;
        try {
          currentSplitObj = this.split_shoe_sizing_options.find(
            (splitShoeArray) => splitShoeArray.id === this.user.split_shoe_info.toString()
          );
        } catch {
          // return the default case
          currentSplitObj = this.split_shoe_sizing_options.find(
            (splitShoeArray) => splitShoeArray.id === '0'
          );
        }
        return currentSplitObj;
      },
      set(value) {
        this.user.split_shoe_info = value.id;
      },
    },
    currentBoulderingSkill: {
      get() {
        return this.boulder_options.find(
          (boulderArray) => boulderArray.id === this.user.climbing_boulder.toString()
        );
      },
      set(value) {
        this.user.climbing_boulder = value.id;
      },
    },
    currentSportSkill: {
      get() {
        return this.sport_trad_options.find(
          (sportArray) => sportArray.id === this.user.climbing_sport.toString()
        );
      },
      set(value) {
        this.user.climbing_sport = value.id;
      },
    },
    currentTradSkill: {
      get() {
        return this.sport_trad_options.find(
          (tradArray) => tradArray.id === this.user.climbing_trad.toString()
        );
      },
      set(value) {
        this.user.climbing_trad = value.id;
      },
    },
  },
  created() {
    this.originalUserValues = { ...this.user };
  },
  methods: {
    closeAndReset() {
      // reset item
      this.streetShoeSize = null;
      this.user.gender = this.originalUserValues.gender;
      this.user.username = this.originalUserValues.username;
      this.user.email = this.originalUserValues.email;
      this.user.foot_shape = this.originalUserValues.foot_shape;
      this.user.split_shoe_info = this.originalUserValues.split_shoe_info;
      this.user.climbing_boulder = this.originalUserValues.climbing_boulder;
      this.user.climbing_sport = this.originalUserValues.climbing_sport;
      this.user.climbing_trad = this.originalUserValues.climbing_trad;
      this.close();
    },
    openChangePasswordModal() {
      this.closeAndReset();
      this.$root.$emit('openChangePasswordModal');
    },
    openDeleteAccountModal() {
      this.closeAndReset();
      this.$root.$emit('openDeleteAccountModal');
    },
    openFootShapeModal() {
      this.closeAndReset();
      this.$root.$emit('openFootShapeModal');
    },
    close() {
      this.formErrors = false;
      this.$emit('close');
    },
    editUser() {
      this.isFormSubmitting = true;
      const editUserDetailsModalComponent = this;
      this.formErrors = false;
      this.showAlert = true;

      this.$store
        .dispatch('EDIT_USER_DETAILS', {
          username: this.user.username,
          email: this.user.email,
          streetShoeSize: this.streetShoeSize ? this.streetShoeSize.value : null,
          footShape: this.user.foot_shape,
          splitShoeInfo: this.user.split_shoe_info,
          gender: this.user.gender,
          climbingBoulder: this.user.climbing_boulder,
          climbingSport: this.user.climbing_sport,
          climbingTrad: this.user.climbing_trad,
        })
        .then((response) => {
          if (response.data.status === 'success') {
            window.location.href = response.data.new_url;
          }
          if (response.data.status === 'error') {
            editUserDetailsModalComponent.formErrors = true;
            editUserDetailsModalComponent.error_username = response.data.username;
            editUserDetailsModalComponent.error_email = response.data.email;
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

<style scoped lang="scss">
label[for='username'],
label[for='email'],
label[for='gender'],
label[for='street_shoe_size'],
label[for='foot_shape'],
label[for='split_shoe_sizing'] {
  margin-bottom: 1em;
}
</style>
