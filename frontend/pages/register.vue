<template>
  <RegistrationForm></RegistrationForm>
</template>

<script>
import RegistrationForm from '@/components/RegistrationForm';

export default {
  name: 'Register',
  layout: 'noHomepageForm',
  components: {
    RegistrationForm,
  },
  head() {
    return {
      title: 'Register',
    };
  },
};
</script>
