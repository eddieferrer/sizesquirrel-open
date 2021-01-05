import Vue from 'vue';
import Vuex from 'vuex';

import actions from './actions';
import getters from './getters';
import mutations from './mutations';

Vue.use(Vuex);

const userToken = process.browser
  ? localStorage.getItem('user-token') || ''
  : '';

const state = () => {
  return {
    context_flash_message: {
      class: '',
      message: '',
    },
    token: userToken,

    init: '',

    user: {},
    profile: {},
    shoe: [],
    brand: {},
    allitems: [],
    allbrands: [],
    match: {
      want: null,
      have: null,
      size: null,
    },
  };
};

const store = {
  state,
  actions,
  getters,
  mutations,
};

export default store;
