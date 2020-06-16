<template>
  <NotFoundBlock></NotFoundBlock>
</template>

<script>
import NotFoundBlock from '@/components/NotFoundBlock';

export default {
  name: 'NotFound',
  components: {
    NotFoundBlock,
  },
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Page Not Found',
  },
};
</script>
