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
  layout: 'no-homepage-form',
  head() {
    return {
      title: 'Forgot Username',
    };
  },
};
</script>
