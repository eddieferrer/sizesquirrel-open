<template>
  <div class="column is-12">
    <a id="user_details" name="user_details"></a>
    <h2 class="is-size-4 has-text-centered has-text-primary">User Details</h2>
    <h5 v-if="isMyProfile" class="is-size-5 has-text-centered">
      Information about your account
    </h5>
    <h5 v-if="!isMyProfile" class="is-size-5 has-text-centered">
      Information about this user
    </h5>
    <hr />

    <div v-if="isMyProfile" class="columns">
      <div class="column is-narrow">
        <span class="icon-wrapper">
          <svg-icon icon="fi-torso"></svg-icon>
        </span>
      </div>
      <div class="column">
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Username</label
          >
          <div class="control">
            <strong>{{ user.username }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey">Name</label>
          <div class="control">
            <strong>{{ user.name }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Email</label
          >
          <div class="control">
            <strong>{{ user.email }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Member Since</label
          >
          <div class="control">
            <strong>{{ user.date_created_readable }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Gender</label
          >
          <div class="control">
            <strong>{{ user.get_gender }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Number Of Shoes</label
          >
          <div class="control">
            <strong>{{ itemCount }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Foot Shape</label
          >
          <div class="control">
            <div class="columns">
              <div v-if="user.foot_shape > 0" class="column is-narrow">
                <img
                  class="profile_foot_shape_img"
                  :src="'/images/footshape/shape' + user.foot_shape + '.jpg'"
                  alt
                />
              </div>
              <div class="column is-6">
                <strong>{{ user.get_foot_shape }}</strong>
                <br />
                <small>
                  <a
                    type="button"
                    @click.prevent.stop="showFootShapeModal = true"
                    >More information about foot shapes</a
                  >
                </small>
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Street Shoe Size</label
          >
          <div class="control">
            <span v-if="user.street_shoe_size_in">
              <span>
                <strong>{{ user.street_shoe_size['EUR'] }} EUR</strong
                >&nbsp;|&nbsp;
              </span>
              <span>
                <strong>{{ user.street_shoe_size['USM'] }} USM</strong
                >&nbsp;|&nbsp;
              </span>
              <span>
                <strong>{{ user.street_shoe_size['USW'] }} USW</strong
                >&nbsp;|&nbsp;
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
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Split shoe sizing?</label
          >
          <div class="control">
            <strong>{{ user.get_split_shoe_info }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Climbing Skill</label
          >
          <div class="control">
            <span>
              <strong>Boulder {{ user.get_climbing_boulder }}</strong
              >&nbsp;|&nbsp;
            </span>
            <span>
              <strong>Sport {{ user.get_climbing_sport }}</strong
              >&nbsp;|&nbsp;
            </span>
            <span>
              <strong>Trad {{ user.get_climbing_trad }}</strong>
            </span>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <hr />
            <p>
              <a type="button" @click.prevent.stop="$emit('open-details')"
                >Change User Details</a
              >
            </p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!isMyProfile" class="columns">
      <div class="column is-narrow">
        <span class="icon-wrapper">
          <svg-icon icon="fi-torso"></svg-icon>
        </span>
      </div>
      <div class="column">
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Username</label
          >
          <div class="control">
            <strong>{{ profile.username }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Member Since</label
          >
          <div class="control">
            <strong>{{ profile.date_created_readable }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Gender</label
          >
          <div class="control">
            <strong>{{ profile.get_gender }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Number Of Shoes</label
          >
          <div class="control">
            <strong>{{ itemCount }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Foot Shape</label
          >
          <div class="control">
            <div class="columns">
              <div v-if="profile.foot_shape > 0" class="column is-narrow">
                <img
                  class="profile_foot_shape_img"
                  :src="'/images/footshape/shape' + profile.foot_shape + '.jpg'"
                  alt
                />
              </div>
              <div class="column is-6">
                <strong>{{ profile.get_foot_shape }}</strong>
                <br />
                <small>
                  <a
                    type="button"
                    @click.prevent.stop="showFootShapeModal = true"
                    >More information about foot shapes</a
                  >
                </small>
              </div>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Street Shoe Size</label
          >
          <div class="control">
            <span v-if="profile.street_shoe_size_in">
              <span>
                <strong>{{ profile.street_shoe_size['EUR'] }} EUR</strong
                >&nbsp;|&nbsp;
              </span>
              <span>
                <strong>{{ profile.street_shoe_size['USM'] }} USM</strong
                >&nbsp;|&nbsp;
              </span>
              <span>
                <strong>{{ profile.street_shoe_size['USW'] }} USW</strong
                >&nbsp;|&nbsp;
              </span>
              <span>
                <strong>{{ profile.street_shoe_size['UK'] }} UK</strong>&nbsp;
              </span>
            </span>
            <span v-if="!profile.street_shoe_size_in">
              <span>
                <strong>None</strong>
              </span>
            </span>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Split shoe sizing?</label
          >
          <div class="control">
            <strong>{{ profile.get_split_shoe_info }}</strong>
          </div>
        </div>
        <div class="field">
          <label class="label has-text-weight-normal has-text-grey"
            >Climbing Skill</label
          >
          <div class="control">
            <span>
              <strong>Boulder {{ profile.get_climbing_boulder }}</strong
              >&nbsp;|&nbsp;
            </span>
            <span>
              <strong>Sport {{ profile.get_climbing_sport }}</strong
              >&nbsp;|&nbsp;
            </span>
            <span>
              <strong>Trad {{ profile.get_climbing_trad }}</strong>
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- modals -->
    <FootShapeModal
      :show="showFootShapeModal"
      @close="showFootShapeModal = false"
    ></FootShapeModal>
    <ChangePasswordModal
      :show="showChangePasswordModal"
      @close="showChangePasswordModal = false"
    ></ChangePasswordModal>
    <DeleteAccountModal
      :show="showDeleteAccountModal"
      :user-id="user.id"
      @close="showDeleteAccountModal = false"
    ></DeleteAccountModal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import SvgIcon from '@/components/SvgIcon';
import FootShapeModal from '@/components/FootShapeModal';
import ChangePasswordModal from '@/components/ChangePasswordModal';
import DeleteAccountModal from '@/components/DeleteAccountModal';

export default {
  name: 'ProfileDetails',
  components: {
    FootShapeModal,
    ChangePasswordModal,
    DeleteAccountModal,
    SvgIcon,
  },
  data() {
    return {
      showFootShapeModal: false,
      showChangePasswordModal: false,
      showDeleteAccountModal: false,
    };
  },
  computed: {
    ...mapGetters(['profile', 'isMyProfile', 'user']),
    itemCount() {
      return this.profile.items.length || 0;
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
  width: 160px;
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

.profile_foot_shape_img {
  height: 75px;
  border: 1px solid #ddd;
}
</style>
