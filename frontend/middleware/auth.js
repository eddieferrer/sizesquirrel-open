export default async function ({ app, store, redirect, route, $cookies }) {
  if ($cookies.get('user-token')) {
    app.$axios.setToken($cookies.get('user-token'), 'Bearer');
    store.commit('AUTH_SUCCESS', $cookies.get('user-token'));
    await store.dispatch('GET_USER');
  } else if (!store.getters.isAuthenticated) {
    return redirect({ name: 'login', query: { redirect: route.fullPath } });
  }
}
