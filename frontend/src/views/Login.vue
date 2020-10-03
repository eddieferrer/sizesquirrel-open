<template>
  <LoginForm :redirect="redirect"></LoginForm>
</template>

<script>
import LoginForm from '@/components/LoginForm';

export default {
  name: 'Login',
  components: {
    LoginForm,
  },
  props: {
    redirect: {
      type: String,
      default: '',
    },
  },
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Login',
  },
};
</script>
