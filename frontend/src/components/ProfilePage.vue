<template>
  <div>
    <div v-if="profile.items.length == 0" class="columns">
      <div class="column">
        <div
          class="level box is-marginless has-text-centered box has-background-warning has-text-white"
        >
          <p>You don't have any shoes. Use the form below to add shoes to your profile.</p>
          <strong class="has-text-white"
            >If you do not add any shoes to your profile we will not be able to find your
            size.</strong
          >
        </div>
      </div>
    </div>

    <div class="columns reverse-row-order">
      <div class="column is-8">
        <ProfileItems v-cloak v-if="profile.id"></ProfileItems>
      </div>
      <div class="column is-4">
        <ProfileDetails
          v-cloak
          v-if="profile.id"
          @open-details="showEditUserDetailsModal = true"
        ></ProfileDetails>
      </div>
    </div>

    <div v-if="isMyProfile && profile.get_foot_shape == 'Not specified'" class="columns">
      <div class="column">
        <div class="level box is-marginless has-text-centered box has-background-light">
          <p>
            Consider adding your foot shape to your profile for better match results.
            <a type="button" @click.prevent.stop="showEditUserDetailsModal = true">
              Change Foot Shape in User Details
            </a>
          </p>
        </div>
      </div>
    </div>

    <div
      v-if="isMyProfile && profile.get_foot_shape !== 'Not specified' && hasDefaultClimbingSkill"
      class="columns"
    >
      <div class="column">
        <div class="level box is-marginless has-text-centered box has-background-light">
          <p>
            Consider adding your climbing skill to your profile.
            <a type="button" @click.prevent.stop="showEditUserDetailsModal = true">
              Change Climbing Skill in User Details
            </a>
          </p>
        </div>
      </div>
    </div>

    <div v-if="isMyProfile" class="columns">
      <div class="column">
        <RecommendationsByShape
          v-cloak
          v-if="isMyProfile && isAuthenticated && profile.id"
        ></RecommendationsByShape>
      </div>
    </div>

    <!-- modals -->

    <EditUserDetailsModal
      v-if="isMyProfile"
      :show="showEditUserDetailsModal"
      :user="user"
      @close="showEditUserDetailsModal = false"
    ></EditUserDetailsModal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import ProfileDetails from './ProfileDetails';
import ProfileItems from './ProfileItems';
import RecommendationsByShape from './RecommendationsByShape';
import EditUserDetailsModal from './EditUserDetailsModal';

export default {
  name: 'ProfilePage',
  components: {
    ProfileItems,
    ProfileDetails,
    RecommendationsByShape,
    EditUserDetailsModal,
  },
  data() {
    return {
      showEditUserDetailsModal: false,
    };
  },
  computed: {
    ...mapGetters(['profile', 'isAuthenticated', 'isMyProfile', 'user']),
    hasDefaultClimbingSkill() {
      if (
        this.profile.get_climbing_boulder === 'V0' &&
        this.profile.get_climbing_sport === '5.0' &&
        this.profile.get_climbing_trad === '5.0'
      ) {
        return true;
      }
      return false;
    },
  },
  created() {},
};
</script>

<style scoped lang="scss">
@media only screen and (min-width: 769px) {
  .reverse-row-order {
    display: flex;
    flex-direction: row-reverse;
  }
}
</style>
