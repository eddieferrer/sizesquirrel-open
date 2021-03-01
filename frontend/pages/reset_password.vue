<template>
  <ChangePasswordForm></ChangePasswordForm>
</template>

<script>
import ChangePasswordForm from '@/components/ChangePasswordForm';

export default {
  name: 'ResetPassword',
  components: {
    ChangePasswordForm,
  },
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Reset Password',
    };
  },
};
</script>
