<template>
  <div class="columns">
    <div class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">Browse</h2>
      <h5 class="is-size-5 has-text-centered">Find your perfect shoe</h5>
      <hr />
      <ItemListServer
        v-cloak
        target="browse"
        pagetype="browse"
      ></ItemListServer>
    </div>
  </div>
</template>

<script>
import ItemListServer from '@/components/ItemListServer';

export default {
  name: 'Browse',
  layout: 'homepageForm',
  middleware: ['auth'],
  components: {
    ItemListServer,
  },
  head() {
    return {
      title: 'Browse',
    };
  },
};
</script>
