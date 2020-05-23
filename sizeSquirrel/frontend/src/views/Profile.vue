<template>
  <div>
    <NotFoundBlock v-cloak v-if="profileNotFound"></NotFoundBlock>
    <ProfilePage v-cloak v-if="profile.id"></ProfilePage>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import ProfilePage from '@/components/ProfilePage';
import NotFoundBlock from '@/components/NotFoundBlock';

export default {
  name: 'Profile',
  components: {
    ProfilePage,
    NotFoundBlock,
  },
  metaInfo() {
    return {
      // title will be injected into parent titleTemplate
      title: 'My Profile',
    };
  },
  computed: {
    ...mapGetters(['isInitialized', 'profile', 'urlContextProfileId']),
    profileNotFound() {
      return (
        !this.notEmptyObject(this.profile) && this.isInitialized && this.urlContextProfileId === ''
      );
    },
  },
};
</script>
