<template>
  <RegistrationForm></RegistrationForm>
</template>

<script>
import RegistrationForm from '@/components/RegistrationForm';

export default {
  name: 'Register',
  components: {
    RegistrationForm,
  },
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Register',
    };
  },
};
</script>
