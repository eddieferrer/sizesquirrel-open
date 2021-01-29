<template>
  <ForgotPasswordForm></ForgotPasswordForm>
</template>

<script>
import ForgotPasswordForm from '@/components/ForgotPasswordForm';

export default {
  name: 'ForgotPassword',
  components: {
    ForgotPasswordForm,
  },
  layout: 'no-homepage-form',
  head() {
    return {
      title: 'Forgot Password',
    };
  },
};
</script>
