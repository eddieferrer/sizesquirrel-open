const SplitShoeSizingOptions = {
  data() {
    return {
      get split_shoe_sizing_options() {
        return [
          { id: '0', text: 'No' },
          { id: '1', text: 'Yes - Left Shoe Slightly Larger Than Right' },
          { id: '2', text: 'Yes - Right Shoe Slightly Larger Than Left' },
        ];
      },
    };
  },
};
export default SplitShoeSizingOptions;
