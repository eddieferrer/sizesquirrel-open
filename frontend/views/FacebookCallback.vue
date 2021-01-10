<template>
  <FacebookAccountRedirect
    :form-type="formType"
    :state="state"
    :access-token="accessToken"
  />
</template>

<script>
import FacebookAccountRedirect from '@/components/FacebookAccountRedirect';

export default {
  name: 'FacebookCallback',
  layout: 'no-homepage-form',
  components: { FacebookAccountRedirect },
  props: {
    formType: {
      type: String,
      default: '',
    },
    accessToken: {
      type: String,
      default: '',
    },
    state: {
      type: String,
      default: '',
    },
  },
};
</script>
