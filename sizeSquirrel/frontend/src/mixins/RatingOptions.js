const RatingOptions = {
  data() {
    return {
      get rating_options() {
        return [
          { id: '5', text: '5 - Best' },
          { id: '4', text: '4 - Good' },
          { id: '3', text: '3 - Ok' },
          { id: '2', text: '2 - Bad' },
          { id: '1', text: '1 - Worst' },
        ];
      },
    };
  },
};
export default RatingOptions;
