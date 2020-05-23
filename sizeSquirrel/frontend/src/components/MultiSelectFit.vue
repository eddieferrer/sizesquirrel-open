<template>
  <multiselect
    v-model="multiSelectValue"
    :allow-empty="false"
    :options="fit_options"
    :placeholder="placeholder"
    :multiple="false"
    track-by="id"
    label="text"
    :show-labels="false"
    name="rating"
    :max-height="140"
    :open-direction="openDirection"
    @input="updateValue"
  ></multiselect>
</template>

<script>
import Multiselect from 'vue-multiselect';
import FitOptions from '@/mixins/FitOptions';

export default {
  name: 'MultiSelectFit',
  components: { Multiselect },
  mixins: [FitOptions],
  props: {
    value: {
      type: Object,
      default() {
        return {};
      },
    },
    placeholder: {
      type: String,
      default: 'Select Fit',
    },
    openDirection: {
      type: String,
      default: 'bottom',
    },
  },
  data() {
    return {
      multiSelectValue: this.value,
    };
  },
  watch: {
    value(value) {
      this.multiSelectValue = value;
    },
  },
  methods: {
    updateValue() {
      this.$emit('input', this.multiSelectValue);
    },
  },
};
</script>

<style lang="scss">
@import '~vue-multiselect/dist/vue-multiselect.min.css';
@import '../scss/custom_multiselect.scss';
</style>
