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
  layout: 'no-homepage-form',
  head() {
    return {
      title: 'Reset Password',
    };
  },
};
</script>
