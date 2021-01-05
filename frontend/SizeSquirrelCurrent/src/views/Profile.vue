<template>
  <ProfilePage v-cloak></ProfilePage>
</template>

<script>
import ProfilePage from '@/components/ProfilePage';
import store from '@/store/store';

const getData = (to, from, next) => {
  return store
    .dispatch('INITIALIZE_APP', {
      url: to.fullPath,
    })
    .then(() => {
      if (store.getters.hasProfile) {
        next();
      } else {
        next(`/404`);
      }
    })
    .catch(() => {
      store.commit('STATE_INIT_ERROR');
    });
};

export default {
  name: 'Profile',
  components: {
    ProfilePage,
  },
  beforeRouteEnter(to, from, next) {
    getData(to, from, next);
  },
  beforeRouteUpdate(to, from, next) {
    getData(to, from, next);
  },
};
</script>
