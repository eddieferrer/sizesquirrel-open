const AUTH_LOGOUT = (state) => {
  state.token = '';
  state.user = {};
};

const AUTH_SUCCESS = (state, token) => {
  state.token = token;
};

const SET_ALL_BRANDS = (state, payload) => {
  state.allbrands = payload.brands;
};

const SET_BRAND = (state, payload) => {
  state.brand = payload.brand;
};

const SET_FLASH_MESSAGE = (state, payload) => {
  state.context_flash_message = payload;
};

const SET_MATCH_INFO = (state, { key, shoe }) => {
  state.match[key] = shoe;
};

const SET_MATCH_SIZE = (state, payload) => {
  state.match.size = payload;
};

const SET_PROFILE = (state, payload) => {
  state.profile = payload.user_details;
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

const SET_USER = (state, payload) => {
  state.user = payload.user;
};

const STATE_INIT_DONE = (state) => {
  state.init = 'success';
};

const STATE_INIT_ERROR = (state) => {
  state.init = 'error';
};

const STATE_INIT_LOADING = (state) => {
  state.init = 'loading';
};

export default {
  AUTH_LOGOUT,
  AUTH_SUCCESS,
  SET_ALL_BRANDS,
  SET_BRAND,
  SET_FLASH_MESSAGE,
  SET_MATCH_INFO,
  SET_MATCH_SIZE,
  SET_PROFILE,
  SET_SHOE,
  SET_USER,
  STATE_INIT_DONE,
  STATE_INIT_ERROR,
  STATE_INIT_LOADING,
};
