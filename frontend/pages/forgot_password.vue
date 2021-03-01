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
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Forgot Password',
    };
  },
};
</script>
