<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">Not Authorized</h2>
      <h5 class="is-size-5 has-text-centered">We're sorry</h5>
      <hr />
      <p>You are not authorized to view this page.</p>
      <NuxtLink to="/">Return to Homepage</NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotAuthorized',
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Not Authorized',
  },
};
</script>
