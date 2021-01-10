export default function ({ store, redirect, route }) {
  // If the user is not authenticated
  if (!store.getters.isAuthenticated) {
    return redirect({ name: 'login', query: { redirect: route.fullPath } });
  } else if (store.getters.isAuthenticated) {
    // Get user info in state
    store.dispatch('GET_USER').then(() => {});
  }
}
