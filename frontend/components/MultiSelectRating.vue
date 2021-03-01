<template>
  <multiselect
    v-model="multiSelectValue"
    :allow-empty="false"
    :options="rating_options"
    :placeholder="placeholder"
    :multiple="false"
    track-by="id"
    label="text"
    :show-labels="false"
    name="rating"
    :max-height="140"
    @input="updateValue"
  ></multiselect>
</template>

<script>
import Multiselect from 'vue-multiselect';
import RatingOptions from '@/mixins/RatingOptions';

export default {
  name: 'MultiSelectRating',
  components: { Multiselect },
  mixins: [RatingOptions],
  props: {
    value: {
      type: Object,
      default() {
        return {};
      },
    },
    placeholder: {
      type: String,
      default: 'Select A Rating',
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
