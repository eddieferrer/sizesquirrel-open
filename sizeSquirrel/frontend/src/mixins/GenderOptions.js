const GenderOptions = {
  data() {
    return {
      get gender_options() {
        return [
          { id: '0', text: 'Prefer not to say' },
          { id: '1', text: 'Male' },
          { id: '2', text: 'Female' },
        ];
      },
    };
  },
};
export default GenderOptions;
