<template>
  <MigrateFacebookForm></MigrateFacebookForm>
</template>

<script>
import MigrateFacebookForm from '@/components/MigrateFacebookForm';

export default {
  name: 'ForgotPassword',
  components: {
    MigrateFacebookForm,
  },
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Migrate Facebook Account',
    };
  },
};
</script>
