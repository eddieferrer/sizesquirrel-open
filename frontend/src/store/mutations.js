const SET_FLASH_MESSAGE = (state, payload) => {
  state.context_flash_message = payload;
};
const STATE_STATUS_LOADING = (state) => {
  state.status = 'loading';
};
const STATE_STATUS_DONE = (state) => {
  state.status = 'success';
};
const STATE_STATUS_ERROR = (state) => {
  state.status = 'error';
};

const STATE_INIT_LOADING = (state) => {
  state.init = 'loading';
};
const STATE_INIT_DONE = (state) => {
  state.init = 'success';
};
const STATE_INIT_ERROR = (state) => {
  state.init = 'error';
};
const AUTH_SUCCESS = (state, token) => {
  state.status = 'success';
  state.token = token;
};

const AUTH_LOGOUT = (state) => {
  state.status = '';
  state.token = '';
  state.user = {};
};
const SET_CONTEXT = (state, payload) => {
  state.url_context.profile_id = payload.profile_id;
  state.url_context.brand_id = payload.brand_id;
  state.url_context.model_id_list = payload.model_id_list;
  state.url_context.match = payload.match;
};
const SET_USER = (state, payload) => {
  state.user = payload.user;
};
const SET_BRAND = (state, payload) => {
  state.brand = payload.brand;
};
const SET_PROFILE = (state, payload) => {
  state.profile = payload.user_details;
};
const SET_ALL_ITEMS = (state, payload) => {
  state.allitems = payload.items;
};
const SET_ALL_BRANDS = (state, payload) => {
  state.allbrands = payload.brands;
};
const SET_SHOE = (state, payload) => {
  const shoesArray = [];
  payload.forEach((item) => {
    const { shoe } = item;
    shoe.stats = item.shoe.stats;
    shoe.shoe_comments = item.shoe_comments;
    shoe.shoe_sale_links = item.shoe_sale_links;
    shoesArray.push(shoe);
  });
  state.shoe = shoesArray;
};

const SET_CONTEXT_MATCH_WANT_ITEM = (state, payload) => {
  state.url_context.match.want_item = payload;
};
const SET_CONTEXT_MATCH_HAVE_ITEM = (state, payload) => {
  state.url_context.match.have_item = payload;
};
const SET_CONTEXT_MATCH_SIZE = (state, payload) => {
  state.url_context.match.size = payload;
};

export default {
  SET_CONTEXT_MATCH_WANT_ITEM,
  SET_CONTEXT_MATCH_HAVE_ITEM,
  SET_CONTEXT_MATCH_SIZE,
  AUTH_LOGOUT,
  AUTH_SUCCESS,
  SET_BRAND,
  SET_CONTEXT,
  SET_PROFILE,
  SET_SHOE,
  SET_USER,
  SET_FLASH_MESSAGE,
  STATE_STATUS_DONE,
  STATE_STATUS_ERROR,
  STATE_STATUS_LOADING,
  STATE_INIT_DONE,
  STATE_INIT_ERROR,
  STATE_INIT_LOADING,
  SET_ALL_ITEMS,
  SET_ALL_BRANDS,
};
