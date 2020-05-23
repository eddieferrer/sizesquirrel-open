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
    status: '',
    init: '',
    url_context: {
      profile_id: '',
      brand_id: '',
      model_id_list: [],
      match: {
        want_item: null,
        have_item: null,
        size: '',
      },
    },
    user: {},
    profile: {},
    shoe: [],
    brand: {},
    allitems: [],
    allbrands: [],
  },
  actions,
  getters,
  mutations,
});

export default store;
