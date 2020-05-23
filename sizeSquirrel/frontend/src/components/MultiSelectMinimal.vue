<template>
  <multiselect
    v-model="multiSelectValue"
    :allow-empty="false"
    :options="options"
    :placeholder="placeholder"
    :multiple="false"
    track-by="id"
    label="text"
    :show-labels="false"
    :name="name"
    :max-height="maxHeight"
    :searchable="false"
    :open-direction="openDirection"
    @input="updateValue"
  ></multiselect>
</template>

<script>
import Multiselect from 'vue-multiselect';

export default {
  name: 'MultiSelectMinimal',
  components: { Multiselect },
  props: {
    value: {
      type: Object,
      default() {
        return {};
      },
    },
    maxHeight: {
      type: Number,
      default: 140,
    },
    options: {
      type: Array,
      default() {
        return [];
      },
    },
    placeholder: {
      type: String,
      default: 'Select',
    },
    name: {
      type: String,
      default: '',
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
