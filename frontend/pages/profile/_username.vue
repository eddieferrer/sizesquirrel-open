<template>
  <ProfilePage v-cloak></ProfilePage>
</template>

<script>
import ProfilePage from '@/components/ProfilePage';

export default {
  name: 'Profile',
  components: {
    ProfilePage,
  },
  layout: 'homepage-form',
  asyncData(context) {
    return context.store
      .dispatch('INITIALIZE_APP', {
        url: context.route.fullPath,
      })
      .then(() => {
        if (context.store.getters.hasProfile) {
        } else {
          context.redirect(`/404`);
        }
      })
      .catch(() => {
        context.store.commit('STATE_INIT_ERROR');
      });
  },
};
</script>
