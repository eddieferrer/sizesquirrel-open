<template>
  <RegistrationForm></RegistrationForm>
</template>

<script>
import RegistrationForm from '@/components/RegistrationForm';

export default {
  name: 'Register',
  layout: 'no-homepage-form',
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
