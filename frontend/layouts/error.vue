<template>
  <div class="columns is-centered">
    <div v-if="error.statusCode === 404" class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        Page not found
      </h2>
      <h5 class="is-size-5 has-text-centered">We're sorry</h5>
      <hr />
      <p>We could not find the page you were looking for.</p>
      <NuxtLink to="/">Return to Homepage</NuxtLink>
    </div>
    <div
      v-else-if="error.statusCode === 401"
      class="column is-two-thirds-desktop"
    >
      <h2 class="is-size-4 has-text-centered has-text-primary">
        Not Authorized
      </h2>
      <h5 class="is-size-5 has-text-centered">We're sorry</h5>
      <hr />
      <p>You are not authorized to view this page.</p>
      <NuxtLink to="/">Return to Homepage</NuxtLink>
    </div>
    <div v-else class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        An Error Occurred
      </h2>
      <h5 class="is-size-5 has-text-centered">We're sorry</h5>
      <hr />
      <p>We could not find the page you were looking for.</p>
      <NuxtLink to="/">Return to Homepage</NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default() {
        return {
          statusCode: null,
        };
      },
    },
  },
  layout: 'no-homepage-form',
  computed: {
    pageTitle() {
      if (this.error.statusCode === 404) {
        return 'Page Not Found';
      }
      if (this.error.statusCode === 401) {
        return 'Not Authorized';
      }
      return 'Error';
    },
  },
  head() {
    return {
      title: this.pageTitle,
    };
  },
};
</script>
