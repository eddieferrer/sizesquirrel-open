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
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Forgot Password',
  },
};
</script>
