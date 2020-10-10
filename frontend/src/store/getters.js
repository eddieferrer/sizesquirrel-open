// utility functions
const isEmptyObject = (someObject) => Object.keys(someObject).length === 0;

// getters
const user = (state) => state.user;
const shoe = (state) => state.shoe;
const brand = (state) => state.brand;
const profile = (state) => state.profile;

const hasBrand = (state) => !isEmptyObject(state.brand);
const hasProfile = (state) => !isEmptyObject(state.profile);
const hasShoe = (state) => !isEmptyObject(state.shoe);

const isAuthenticated = (state) => !!state.token;

const isMyProfile = (state) => {
  if (state.user.id === state.profile.id) {
    return true;
  }
  return false;
};

const isInitialized = (state) => {
  if (state.init === 'loading') {
    return false;
  }
  return true;
};
const allitems = (state) => state.allitems;
const allbrands = (state) => state.allbrands;

const contextFlashMessage = (state) => state.context_flash_message;

const matchInfoSize = (state) => state.match.size;
const matchInfoWant = (state) => state.match.want;
const matchInfoHave = (state) => state.match.have;

export default {
  allbrands,
  allitems,
  brand,
  contextFlashMessage,
  hasBrand,
  hasProfile,
  hasShoe,
  isAuthenticated,
  isInitialized,
  isMyProfile,
  matchInfoSize,
  matchInfoWant,
  matchInfoHave,
  profile,
  shoe,
  user,
};
