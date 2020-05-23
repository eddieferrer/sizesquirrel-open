import axios from 'axios';
import { isEmpty } from '@/utils/utils';

const INITIALIZE_APP = context =>
  new Promise((resolve, reject) => {
    context.commit('STATE_INIT_LOADING');
    axios({
      url: '/apiv2/context/',
      data: { url: window.location.href },
      method: 'POST',
    })
      .then(resp => {
        context.commit('SET_CONTEXT', resp.data);

        const promiseArray = [];

        if (resp.data.model_id_list) {
          promiseArray.push(context.dispatch('GET_SHOE', resp.data.model_id_list));
        }
        if (resp.data.profile_id) {
          promiseArray.push(context.dispatch('GET_PROFILE', resp.data.profile_id));
        }
        if (resp.data.brand_id) {
          promiseArray.push(context.dispatch('GET_BRAND', resp.data.brand_id));
        }

        return Promise.all(promiseArray);
      })
      .then(resp => {
        context.commit('STATE_INIT_DONE');
        resolve(resp);
      })
      .catch(error => {
        context.commit('STATE_INIT_ERROR', error);
        reject(error);
      });
  });

const GET_SHOE = (context, payload) =>
  new Promise(resolve => {
    const responses = [];
    const promiseArray = [];
    payload.forEach(element => {
      promiseArray.push(
        // eslint-disable-next-line no-shadow
        new Promise((resolve, reject) => {
          axios({ url: `/apiv2/item/details/${element}`, method: 'GET' })
            .then(resp => {
              responses.push(resp.data);
              resolve(resp);
            })
            .catch(error => {
              reject(error);
            });
        })
      );
    });
    Promise.all(promiseArray).then(() => {
      context.commit('SET_SHOE', responses);
      resolve();
    });
  });

const GET_BRAND = (context, payload) =>
  new Promise((resolve, reject) => {
    axios({ url: `/apiv2/brand/${payload}`, method: 'GET' })
      .then(resp => {
        context.commit('SET_BRAND', resp.data);
        resolve(resp);
      })
      .catch(error => {
        reject(error);
      });
  });

const GET_USER = context => {
  return new Promise((resolve, reject) => {
    if (isEmpty(context.state.user)) {
      axios({ url: '/apiv2/auth/user/', method: 'GET' })
        .then(resp => {
          context.commit('SET_USER', resp.data);
          resolve(resp);
        })
        .catch(error => {
          reject(error);
        });
    } else {
      resolve({
        data: context.state.user,
      });
    }
  });
};

const GET_PROFILE = (context, payload) =>
  new Promise((resolve, reject) => {
    axios({ url: `/apiv2/user/details/${payload}`, method: 'GET' })
      .then(resp => {
        context.commit('SET_PROFILE', resp.data);
        resolve(resp);
      })
      .catch(error => {
        reject(error);
      });
  });

const GET_ALL_BRANDS = context => {
  return new Promise((resolve, reject) => {
    if (context.state.allbrands.length === 0) {
      axios({ url: '/apiv2/brands/', method: 'GET' })
        .then(resp => {
          context.commit('SET_ALL_BRANDS', resp.data);
          resolve(resp);
        })
        .catch(error => {
          reject(error);
        });
    } else {
      resolve({
        data: context.state.allbrands,
      });
    }
  });
};

const GET_SHOE_BUDDIES = (context, payload) =>
  new Promise((resolve, reject) => {
    axios({ url: `/apiv2/user/shoebuddies/${payload}`, method: 'GET' })
      .then(resp => {
        resolve(resp);
      })
      .catch(error => {
        reject(error);
      });
  });

const SHOW_FLASH_MESSAGE = (context, payload) => {
  window.scrollTo(0, 0);
  context.commit('SET_FLASH_MESSAGE', payload);
};

const RESET_FLASH_MESSAGE = context => {
  context.commit('SET_FLASH_MESSAGE', {});
};

const FB_REGISTER = (context, payload) =>
  new Promise((resolve, reject) => {
    // The Promise used for router redirect in login
    axios({ url: '/apiv2/auth/facebookregister/', data: payload, method: 'POST' })
      .then(resp => {
        localStorage.setItem('user-token', resp.data.token); // store the resp.data.token in localstorage
        axios.defaults.headers.common.Authorization = `Bearer ${resp.data.token}`;
        context.commit('AUTH_SUCCESS', resp.data.token);
        resolve(resp);
      })
      .catch(error => {
        localStorage.removeItem('user-token'); // if the request fails, remove any possible user token if possible
        reject(error);
      });
  });

const AUTH_FB_LOGIN = (context, payload) =>
  new Promise((resolve, reject) => {
    // The Promise used for router redirect in login
    axios({ url: '/apiv2/auth/facebooklogin/', data: payload, method: 'POST' })
      .then(resp => {
        localStorage.setItem('user-token', resp.data.token); // store the resp.data.token in localstorage
        axios.defaults.headers.common.Authorization = `Bearer ${resp.data.token}`;
        context.commit('AUTH_SUCCESS', resp.data.token);
        resolve(resp);
      })
      .catch(error => {
        localStorage.removeItem('user-token'); // if the request fails, remove any possible user token if possible
        reject(error);
      });
  });

// eslint-disable-next-line no-unused-vars
const WAIT = (context, payload) =>
  new Promise((resolve, reject) => {
    if (payload.resolve) {
      return setTimeout(() => resolve(), payload.time * 1000);
    }
    return setTimeout(() => reject(), payload.time * 1000);
  });

const REGISTER = (context, payload) =>
  new Promise((resolve, reject) => {
    axios({ url: '/apiv2/auth/register/', data: payload, method: 'POST' })
      .then(resp => {
        localStorage.setItem('user-token', resp.data.token); // store the resp.data.token in localstorage
        axios.defaults.headers.common.Authorization = `Bearer ${resp.data.token}`;
        context.commit('AUTH_SUCCESS', resp.data.token);
        resolve(resp);
      })
      .catch(error => {
        localStorage.removeItem('user-token'); // if the request fails, remove any possible user token if possible
        reject(error);
      });
  });

const AUTH_LOGOUT = context =>
  new Promise((resolve, reject) => {
    axios({ url: '/apiv2/auth/logout/', method: 'GET' })
      .then(() => {
        context.commit('AUTH_LOGOUT');
        localStorage.removeItem('user-token'); // clear your user's token from localstorage
        delete axios.defaults.headers.common.Authorization;
        resolve();
      })
      .catch(err => {
        localStorage.removeItem('user-token'); // if the request fails, remove any possible user token if possible
        reject(err);
      });
  });

const AUTH_REQUEST = (context, payload) =>
  new Promise((resolve, reject) => {
    axios({ url: '/apiv2/auth/login/', data: payload, method: 'POST' })
      .then(resp => {
        localStorage.setItem('user-token', resp.data.token); // store the resp.data.token in localstorage
        axios.defaults.headers.common.Authorization = `Bearer ${resp.data.token}`;
        context.commit('AUTH_SUCCESS', resp.data.token);
        resolve(resp);
      })
      .catch(error => {
        localStorage.removeItem('user-token'); // if the request fails, remove any possible user token if possible
        reject(error);
      });
  });

const POST_LIST_ITEMS = (context, { target, queryParams }) =>
  new Promise((resolve, reject) => {
    axios({
      url: `/apiv2/items/${target}/`,
      method: 'POST',
      data: queryParams,
    })
      .then(resp => {
        resolve(resp);
      })
      .catch(error => {
        reject(error);
      });
  });

const GET_LIST_ITEMS = (context, { target }) =>
  new Promise((resolve, reject) => {
    axios({
      url: `/apiv2/items/${target}/`,
      method: 'GET',
    })
      .then(resp => {
        resolve(resp);
      })
      .catch(error => {
        reject(error);
      });
  });

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

export default {
  ITEM_SEARCH,
  ADD_PROFILE_ITEM,
  AUTH_FB_LOGIN,
  AUTH_LOGOUT,
  AUTH_REQUEST,
  CHANGE_PASSWORD,
  DELETE_ACCOUNT,
  EDIT_PROFILE_ITEM,
  EDIT_USER_DETAILS,
  FB_REGISTER,
  PRIVATE_MATCH,
  PUBLIC_MATCH,
  FORGOT_PASSWORD,
  FORGOT_USERNAME,
  GET_ADMIN_STATS,
  GET_ALL_BRANDS,
  GET_BRAND,
  GET_LIST_ITEMS,
  GET_PROFILE,
  GET_SHOE_BUDDIES,
  GET_SHOE,
  GET_USER,
  INITIALIZE_APP,
  POST_ADMIN_MATCH_TEST,
  POST_LIST_ITEMS,
  RECOMMEND_A_SHOE,
  REGISTER,
  REMOVE_PROFILE_ITEM,
  RESET_FLASH_MESSAGE,
  RESET_PASSWORD,
  SHOW_FLASH_MESSAGE,
  WAIT,
  GET_POPULAR_SHOES,
};
