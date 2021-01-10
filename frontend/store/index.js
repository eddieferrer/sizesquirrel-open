import Vue from 'vue';
import Vuex from 'vuex';

import actions from './actions';
import getters from './getters';
import mutations from './mutations';

Vue.use(Vuex);
const state = () => {
  return {
    context_flash_message: {
      class: '',
      message: '',
    },
    token: '',

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
