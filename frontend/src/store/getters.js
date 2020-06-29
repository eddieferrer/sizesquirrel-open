const status = (state) => state.status;
const urlContextBrandId = (state) => state.url_context.brand_id;
const urlContextMatch = (state) => state.url_context.match;
const urlContextModelIdList = (state) => state.url_context.model_id_list;
const urlContextProfileId = (state) => state.url_context.profile_id;

const user = (state) => state.user;
const shoe = (state) => state.shoe;
const brand = (state) => state.brand;
const profile = (state) => state.profile;

const isAuthenticated = (state) => !!state.token;
const isAdmin = (state) => {
  if (state.user.id === 1 && !!state.token && state.user.email === 'eferrer@gmail.com') {
    return true;
  }
  return false;
};
const isMyProfile = (state) => {
  if (state.user.id === state.profile.id) {
    return true;
  }
  return false;
};
const isLoading = (state) => {
  if (state.status === 'loading') {
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

export default {
  allitems,
  allbrands,
  brand,
  contextFlashMessage,
  isAdmin,
  isAuthenticated,
  isInitialized,
  isLoading,
  isMyProfile,
  profile,
  shoe,
  status,
  urlContextBrandId,
  urlContextMatch,
  urlContextModelIdList,
  urlContextProfileId,
  user,
};
