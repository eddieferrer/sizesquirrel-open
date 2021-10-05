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
  components: { FacebookAccountRedirect },
  layout: 'noHomepageForm',
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
