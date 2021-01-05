<template>
  <multiselect
    v-model="multiSelectValue"
    :allow-empty="false"
    :options="size_option_groups"
    :placeholder="placeholder"
    :multiple="false"
    :group-select="false"
    group-values="sizes"
    group-label="standard"
    track-by="value"
    label="text"
    :show-labels="false"
    name="size"
    :max-height="170"
    @input="updateValue"
  ></multiselect>
</template>

<script>
import Multiselect from 'vue-multiselect';
import SizeOptions from '@/mixins/SizeOptions';

export default {
  name: 'MultiSelectSize',
  components: { Multiselect },
  mixins: [SizeOptions],
  props: {
    value: {
      type: Object,
      default() {
        return {};
      },
    },
    placeholder: {
      type: String,
      default: 'Search for a Size',
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
