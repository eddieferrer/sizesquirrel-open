<template>
  <LoginForm></LoginForm>
</template>

<script>
import LoginForm from '@/components/LoginForm';

export default {
  name: 'Login',
  components: {
    LoginForm,
  },
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Login',
  },
};
</script>
