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
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Change Password',
  },
};
</script>
