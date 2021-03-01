<template>
  <ForgotUsernameForm></ForgotUsernameForm>
</template>

<script>
import ForgotUsernameForm from '@/components/ForgotUsernameForm';

export default {
  name: 'ForgotUsername',
  components: {
    ForgotUsernameForm,
  },
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Forgot Username',
    };
  },
};
</script>
