import Vue from 'vue';
import Vuex from 'vuex';

import actions from './actions';
import getters from './getters';
import mutations from './mutations';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    context_flash_message: {
      class: '',
      message: '',
    },
    token: localStorage.getItem('user-token') || '',

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
  },
  actions,
  getters,
  mutations,
});

export default store;
