const FootShapeOptions = {
  data() {
    return {
      get foot_shape_options() {
        return [
          { id: '0', text: 'Not Specified' },
          { id: '1', text: 'Egyptian' },
          { id: '2', text: 'Roman' },
          { id: '3', text: 'Greek' },
          { id: '4', text: 'Germanic' },
          { id: '5', text: 'Celtic' },
        ];
      },
    };
  },
};
export default FootShapeOptions;
