module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
  },
  extends: [
    'airbnb-base',
    'plugin:vue/recommended',
    'plugin:prettier/recommended',
    'prettier',
    'prettier/vue',
  ],
  rules: {
    'import/no-unresolved': 0,
    'no-plusplus': 0,
    'no-underscore-dangle': 0,
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'warn',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'warn',
    'no-param-reassign': [
      'error',
      {
        props: true,
        ignorePropertyModificationsFor: [
          'state',
          'acc',
          'e',
          'ctx',
          'req',
          'request',
          'res',
          'response',
          '$scope',
        ],
      },
    ],
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  globals: {
    FB: true,
    _: true,
    workbox: true,
  },
};
