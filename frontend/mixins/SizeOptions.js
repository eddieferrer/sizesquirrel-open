import { sizeOptions } from '@/utils/utils';

const SizeOptions = {
  data() {
    return {
      get size_option_groups() {
        return sizeOptions();
      },
    };
  },
};
export default SizeOptions;
