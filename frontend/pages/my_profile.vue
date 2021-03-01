<script>
export default {
  middleware: [
    'auth',
    function ({ store, redirect }) {
      // redirect to profile page
      // is this necessary with auth middleware
      return store.dispatch('GET_USER').then(() => {
        // the above state is not available here, since it
        // it is resolved asynchronously in the store action
        const { username } = store.getters.user;
        return redirect(`/profile/${username}`);
      });
    },
  ],
};
</script>
