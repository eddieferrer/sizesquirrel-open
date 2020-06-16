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
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Register',
  },
};
</script>
