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
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Forgot Username',
  },
};
</script>
