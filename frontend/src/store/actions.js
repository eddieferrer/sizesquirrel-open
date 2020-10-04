import axios from 'axios';
import { isEmpty } from '@/utils/utils';

const ADD_PROFILE_ITEM = async (context, { itemId, rating, comments, fit, size }) => {
  try {
    const addProfileItem = await axios({
      url: '/apiv2/item/add/',
      method: 'POST',
      data: { itemId, rating, comments, fit, size },
    });
    await context.dispatch('GET_PROFILE', context.state.profile.id);
    return addProfileItem;
  } catch (error) {
    throw error;
  }
};

const AUTH_FB_LOGIN = async (context, payload) => {
  try {
    const authFBLogin = await axios({
      url: '/apiv2/auth/facebooklogin/',
      data: payload,
      method: 'POST',
    });
    // store the authFBLogin.data.token in localstorage
    localStorage.setItem('user-token', authFBLogin.data.token);
    axios.defaults.headers.common.Authorization = `Bearer ${authFBLogin.data.token}`;
    context.commit('AUTH_SUCCESS', authFBLogin.data.token);
    return authFBLogin;
  } catch (error) {
    // if the request fails, remove any possible user token if possible
    localStorage.removeItem('user-token');
    throw error;
  }
};

const AUTH_LOGOUT = async (context) => {
  try {
    const authLogout = await axios({
      url: '/apiv2/auth/logout/',
      method: 'GET',
    });
    context.commit('AUTH_LOGOUT');
    // clear your user's token from localstorage
    localStorage.removeItem('user-token');
    delete axios.defaults.headers.common.Authorization;
    return authLogout;
  } catch (error) {
    // if the request fails, remove any possible user token if possible
    localStorage.removeItem('user-token');
    throw error;
  }
};

const AUTH_REQUEST = async (context, payload) => {
  try {
    const authRequest = await axios({
      url: '/apiv2/auth/login/',
      data: payload,
      method: 'POST',
    });
    // store the authRequest.data.token in localstorage
    localStorage.setItem('user-token', authRequest.data.token);
    axios.defaults.headers.common.Authorization = `Bearer ${authRequest.data.token}`;
    context.commit('AUTH_SUCCESS', authRequest.data.token);
    return authRequest;
  } catch (error) {
    // if the request fails, remove any possible user token if possible
    localStorage.removeItem('user-token');
    throw error;
  }
};

const CHANGE_PASSWORD = async (context, { currentPassword, newPassword, newPasswordConfirm }) => {
  try {
    const changePassword = await axios({
      url: '/apiv2/user/changepassword/',
      method: 'POST',
      data: { currentPassword, newPassword, newPasswordConfirm },
    });
    return changePassword;
  } catch (error) {
    throw error;
  }
};

const DELETE_ACCOUNT = async (context, accountId) => {
  try {
    const deleteAccount = await axios({
      url: `/apiv2/user/deleteaccount/`,
      method: 'POST',
      data: {
        user_id: accountId,
      },
    });
    return deleteAccount;
  } catch (error) {
    throw error;
  }
};

const EDIT_PROFILE_ITEM = async (context, { userItemId, rating, size, fit, comments }) => {
  try {
    const editProfileItem = await axios({
      url: `/apiv2/item/edit/`,
      method: 'POST',
      data: { userItemId, rating, size, fit, comments },
    });
    return editProfileItem;
  } catch (error) {
    throw error;
  }
};

const EDIT_USER_DETAILS = async (
  context,
  {
    username,
    email,
    streetShoeSize,
    footShape,
    splitShoeInfo,
    gender,
    climbingBoulder,
    climbingSport,
    climbingTrad,
  }
) => {
  try {
    const editUserDetails = await axios({
      url: `/apiv2/user/details/change/`,
      method: 'POST',
      data: {
        username,
        email,
        streetShoeSize,
        footShape,
        splitShoeInfo,
        gender,
        climbingBoulder,
        climbingSport,
        climbingTrad,
      },
    });
    return editUserDetails;
  } catch (error) {
    throw error;
  }
};

const FB_REGISTER = async (context, payload) => {
  try {
    const fbRegister = await axios({
      url: '/apiv2/auth/facebookregister/',
      data: payload,
      method: 'POST',
    });
    // store the authFBLogin.data.token in localstorage
    localStorage.setItem('user-token', fbRegister.data.token);
    axios.defaults.headers.common.Authorization = `Bearer ${fbRegister.data.token}`;
    context.commit('AUTH_SUCCESS', fbRegister.data.token);
    return fbRegister;
  } catch (error) {
    // if the request fails, remove any possible user token if possible
    localStorage.removeItem('user-token');
    throw error;
  }
};

const FORGOT_PASSWORD = async (context, { email }) => {
  try {
    const forgotPassword = await axios({
      url: '/apiv2/user/forgotpassword/',
      method: 'POST',
      data: { email },
    });
    return forgotPassword;
  } catch (error) {
    throw error;
  }
};

const FORGOT_USERNAME = async (context, { email }) => {
  try {
    const forgotUsername = await axios({
      url: '/apiv2/user/forgotusername/',
      method: 'POST',
      data: { email },
    });
    return forgotUsername;
  } catch (error) {
    throw error;
  }
};

const GET_ADMIN_STATS = async () => {
  try {
    const adminStats = await axios({
      url: `/apiv2/admin/stats/`,
      method: 'GET',
    });
    return adminStats;
  } catch (error) {
    throw error;
  }
};

const GET_ALL_BRANDS = async (context) => {
  try {
    if (context.state.allbrands.length === 0) {
      const getAllBrands = await axios({
        url: '/apiv2/brands/',
        method: 'GET',
      });
      context.commit('SET_ALL_BRANDS', getAllBrands.data);
      return getAllBrands;
    }
    return { data: context.state.allbrands };
  } catch (error) {
    throw error;
  }
};

const GET_BRAND = async (context, payload) => {
  try {
    const getBrand = await axios({
      url: `/apiv2/brand/${payload}`,
      method: 'GET',
    });
    context.commit('SET_BRAND', getBrand.data);
    return getBrand;
  } catch (error) {
    throw error;
  }
};

const GET_LIST_ITEMS = async (context, { target }) => {
  try {
    const getListItems = await axios({
      url: `/apiv2/items/${target}/`,
      method: 'GET',
    });
    return getListItems;
  } catch (error) {
    throw error;
  }
};

const GET_MATCH_INFO = async (context, { key, id }) => {
  try {
    const getMatchInfo = await axios({
      url: `/apiv2/item/details/${id}`,
      method: 'GET',
    });
    context.commit('SET_MATCH_INFO', { key, shoe: getMatchInfo.data.shoe });
    return getMatchInfo;
  } catch (error) {
    throw error;
  }
};

const GET_POPULAR_SHOES = async () => {
  try {
    const popularShoes = await axios({
      url: `/apiv2/items/popular/`,
      method: 'GET',
    });
    return popularShoes;
  } catch (error) {
    throw error;
  }
};

const GET_PROFILE = async (context, payload) => {
  try {
    const getProfile = await axios({
      url: `/apiv2/user/details/${payload}`,
      method: 'GET',
    });
    context.commit('SET_PROFILE', getProfile.data);
    return getProfile;
  } catch (error) {
    throw error;
  }
};

const GET_SHOE_BUDDIES = async (context, payload) => {
  try {
    const getShoeBuddies = await axios({
      url: `/apiv2/user/shoebuddies/${payload}`,
      method: 'GET',
    });
    return getShoeBuddies;
  } catch (error) {
    throw error;
  }
};

const GET_SHOE = async (context, payload) => {
  try {
    const responses = [];
    const promiseArray = [];
    payload.forEach((element) => {
      promiseArray.push(
        // eslint-disable-next-line no-shadow
        new Promise((resolve, reject) => {
          axios({ url: `/apiv2/item/details/${element}`, method: 'GET' })
            .then((resp) => {
              responses.push(resp.data);
              resolve(resp);
            })
            .catch((error) => {
              reject(error);
            });
        })
      );
    });
    const getShoe = await Promise.all(promiseArray);
    context.commit('SET_SHOE', responses);
    return getShoe;
  } catch (error) {
    throw error;
  }
};

const GET_USER = async (context) => {
  try {
    if (isEmpty(context.state.user)) {
      const getUser = await axios({
        url: '/apiv2/auth/user/',
        method: 'GET',
      });
      context.commit('SET_USER', getUser.data);
      return getUser;
    }
    return {
      data: context.state.user,
    };
  } catch (error) {
    throw error;
  }
};

const INITIALIZE_APP = async (context, { url }) => {
  try {
    const initializeApp = await axios({
      url: '/apiv2/context/',
      data: { url },
      method: 'POST',
    });
    const promiseArray = [];

    if (initializeApp.data.model_id_list) {
      promiseArray.push(context.dispatch('GET_SHOE', initializeApp.data.model_id_list));
    }
    if (initializeApp.data.profile_id) {
      promiseArray.push(context.dispatch('GET_PROFILE', initializeApp.data.profile_id));
    }
    if (initializeApp.data.brand_id) {
      promiseArray.push(context.dispatch('GET_BRAND', initializeApp.data.brand_id));
    }
    return await Promise.all(promiseArray);
  } catch (error) {
    throw error;
  }
};

const ITEM_SEARCH = async (context, { query }) => {
  try {
    const itemSearch = await axios({
      url: `/apiv2/items/search/`,
      method: 'POST',
      data: {
        search: query,
      },
    });
    return itemSearch;
  } catch (error) {
    throw error;
  }
};

const POST_ADMIN_MATCH_TEST = async (context, matchTestItemId) => {
  try {
    const adminMatchTest = await axios({
      url: `/apiv2/admin/matchtest/`,
      method: 'POST',
      data: matchTestItemId,
    });
    return adminMatchTest;
  } catch (error) {
    throw error;
  }
};

const POST_LIST_ITEMS = async (context, { target, queryParams }) => {
  try {
    const postListItems = await axios({
      url: `/apiv2/items/${target}/`,
      method: 'POST',
      data: queryParams,
    });
    return postListItems;
  } catch (error) {
    throw error;
  }
};

const PRIVATE_MATCH = async (context, { wantItemId }) => {
  try {
    const privateMatch = await axios({
      url: '/apiv2/match/private/',
      method: 'POST',
      data: { wantItemId },
    });
    return privateMatch;
  } catch (error) {
    throw error;
  }
};

const PUBLIC_MATCH = async (context, { wantItemId, haveItemId, size }) => {
  try {
    const privateMatch = await axios({
      url: '/apiv2/match/public/',
      method: 'POST',
      data: { wantItemId, haveItemId, size },
    });
    return privateMatch;
  } catch (error) {
    throw error;
  }
};

const RECOMMEND_A_SHOE = async (context, { footShape, gender }) => {
  try {
    const recommendAShoe = await axios({
      url: `/apiv2/recommend/`,
      method: 'POST',
      data: {
        footShape,
        gender,
      },
    });
    return recommendAShoe;
  } catch (error) {
    throw error;
  }
};

const REGISTER = async (context, payload) => {
  try {
    const register = await axios({
      url: '/apiv2/auth/register/',
      data: payload,
      method: 'POST',
    });
    // store the register.data.token in localstorage
    localStorage.setItem('user-token', register.data.token);
    axios.defaults.headers.common.Authorization = `Bearer ${register.data.token}`;
    context.commit('AUTH_SUCCESS', register.data.token);
    return register;
  } catch (error) {
    // if the request fails, remove any possible user token if possible
    localStorage.removeItem('user-token');
    throw error;
  }
};

const REMOVE_PROFILE_ITEM = async (context, itemId) => {
  try {
    const removeProfileItem = await axios({
      url: `/apiv2/item/remove/`,
      method: 'POST',
      data: {
        user_item_id: itemId,
      },
    });
    await context.dispatch('GET_PROFILE', context.state.profile.id);
    return removeProfileItem;
  } catch (error) {
    throw error;
  }
};

const RESET_FLASH_MESSAGE = (context) => {
  context.commit('SET_FLASH_MESSAGE', {});
};

const RESET_PASSWORD = async (context, { password, confirmPassword, token }) => {
  try {
    const resetPassword = await axios({
      url: '/apiv2/user/resetpassword/',
      method: 'POST',
      data: { password, confirmPassword, token },
    });
    return resetPassword;
  } catch (error) {
    throw error;
  }
};

const SHOW_FLASH_MESSAGE = (context, payload) => {
  window.scrollTo(0, 0);
  context.commit('SET_FLASH_MESSAGE', payload);
};

// Utility action that waits
const WAIT = async (context, { time }) => {
  // await this.$store.dispatch('WAIT', {
  //   time: 5,
  // });
  try {
    await new Promise((resolve) => {
      setTimeout(resolve, time * 1000);
    });
  } catch (error) {
    throw error;
  }
};

export default {
  ADD_PROFILE_ITEM,
  AUTH_FB_LOGIN,
  AUTH_LOGOUT,
  AUTH_REQUEST,
  CHANGE_PASSWORD,
  DELETE_ACCOUNT,
  EDIT_PROFILE_ITEM,
  EDIT_USER_DETAILS,
  FB_REGISTER,
  FORGOT_PASSWORD,
  FORGOT_USERNAME,
  GET_ADMIN_STATS,
  GET_ALL_BRANDS,
  GET_BRAND,
  GET_LIST_ITEMS,
  GET_MATCH_INFO,
  GET_POPULAR_SHOES,
  GET_PROFILE,
  GET_SHOE_BUDDIES,
  GET_SHOE,
  GET_USER,
  INITIALIZE_APP,
  ITEM_SEARCH,
  POST_ADMIN_MATCH_TEST,
  POST_LIST_ITEMS,
  PRIVATE_MATCH,
  PUBLIC_MATCH,
  RECOMMEND_A_SHOE,
  REGISTER,
  REMOVE_PROFILE_ITEM,
  RESET_FLASH_MESSAGE,
  RESET_PASSWORD,
  SHOW_FLASH_MESSAGE,
  WAIT,
};
