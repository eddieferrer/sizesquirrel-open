<template>
  <LoginForm :redirect="redirect"></LoginForm>
</template>

<script>
import LoginForm from '@/components/LoginForm';

export default {
  name: 'Login',
  layout: 'noHomepageForm',
  components: {
    LoginForm,
  },
  data() {
    return {
      redirect: this.$route.query.redirect,
    };
  },
  head() {
    return {
      title: 'Login',
    };
  },
};
</script>
