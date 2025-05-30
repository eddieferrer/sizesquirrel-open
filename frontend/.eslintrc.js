module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  extends: [
    '@nuxtjs',
    'prettier',
    'plugin:prettier/recommended',
    'plugin:nuxt/recommended',
  ],
  plugins: ['prettier'],
  // add your custom rules here
  rules: {
    'import/no-unresolved': 0,
    'import/extensions': ['error', 'never'],
    'no-plusplus': 0,
    'no-useless-catch': 0,
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
    'vue/no-mutating-props': 'warn',
    'vue/multi-word-component-names': 0,
  },
  globals: {
    FB: true,
    _: true,
    workbox: true,
  },
};
