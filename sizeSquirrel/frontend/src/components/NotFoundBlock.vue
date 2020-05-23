<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">Page not found</h2>
      <h5 class="is-size-5 has-text-centered">We're sorry</h5>
      <hr />
      <p>We could not find the page you were looking for.</p>
      <RouterLink to="/">Return to Homepage</RouterLink>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFoundBlock',
  components: {},
  data() {
    return {};
  },
};
</script>

<style scoped></style>
