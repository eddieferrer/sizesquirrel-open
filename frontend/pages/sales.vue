<template>
  <div class="columns">
    <div class="column">
      <h2 class="is-size-4 has-text-centered has-text-primary">Sales</h2>
      <h5 class="is-size-5 has-text-centered">
        These shoes are currently on sale
      </h5>
      <hr />
      <ItemListServer v-cloak target="sales" pagetype="sales"></ItemListServer>
    </div>
  </div>
</template>

<script>
import ItemListServer from '@/components/ItemListServer';

export default {
  name: 'Sales',
  components: {
    ItemListServer,
  },
  layout: 'homepageForm',
  head() {
    return {
      // title will be injected into parent titleTemplate
      title: 'Rock Climbing Shoes On Sale',
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: 'Rock Climbing Shoes On Sale | SizeSquirrel',
        },
      ],
    };
  },
};
</script>
