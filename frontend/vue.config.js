const path = require('path');
const GitRevisionPlugin = require('git-revision-webpack-plugin');

const gitRevisionPlugin = new GitRevisionPlugin({ lightweightTags: true });

const isProd = process.env.NODE_ENV === 'production';

const d = new Date();
const nicelyFormattedDate = `${d.getMonth() + 1}${d.getDate()}${d.getFullYear()}`;
const gitHash = gitRevisionPlugin.commithash().substring(0, 7);
const nicelyFormattedHour = `0${d.getHours()}`.slice(-2);
const nicelyFormattedTime = `${nicelyFormattedHour}${d.getMinutes()}`;

process.env.VUE_APP_GITBRANCH = gitRevisionPlugin.branch();
process.env.VUE_APP_GITVERSION = gitRevisionPlugin.version();
process.env.VUE_APP_GITHASH = gitRevisionPlugin.commithash();

process.env.VUE_APP_RELEASE_TAG = isProd
  ? `${gitHash}-${nicelyFormattedDate}_${nicelyFormattedTime}`
  : 'dev';

module.exports = {
  outputDir: path.resolve(__dirname, './dist'),
  assetsDir: 'static',
  devServer: {
    proxy: {
      '^/apiv2': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true,
      },
    },
    hot: false,
    inline: false,
    liveReload: false,
  },
  pluginOptions: {
    webpackBundleAnalyzer: {
      openAnalyzer: false,
    },
  },
  chainWebpack: (config) => {
    config.module.rule('eslint').use('eslint-loader').options({
      fix: true,
    });

    // override vue's default chunks because their chunking is too big.
    config.optimization.delete('splitChunks');
    config.optimization.set('splitChunks', {
      cacheGroups: {
        // Vue modules
        vue: {
          test: /[\\/]node_modules[\\/]vue.*[\\/]/,
          name: 'vue',
          enforce: true,
          priority: 20,
          chunks: 'initial',
        },
        // all other modules modules
        vendors: {
          name: 'chunk-vendors',
          test(module) {
            // `module.resource` contains the absolute path of the file on disk.
            // Note the usage of `path.sep` instead of / or \, for cross-platform compatibility.
            return (
              module.resource &&
              !module.resource.includes(`${path.sep}node_modules${path.sep}vue`) &&
              !module.resource.includes(`${path.sep}src${path.sep}`)
            );
          },
          maxSize: 500000,
          priority: 10,
          enforce: true,
          chunks: 'all', // doesn't get created without 'all' here
        },
        // default common chunk settings from Vue
        common: {
          name: 'chunk-common',
          minChunks: 2,
          priority: 5,
          chunks: 'initial',
          reuseExistingChunk: true,
        },
      },
    });

    // Webpack includes a small piece of runtime code that gets inserted into the last bundle created. This could cause our vendor
    // bundle to change unnecessarily. So the next line causes this runtime to be put in a separate file.
    config.optimization.set('runtimeChunk', true);
  },
  css: {
    loaderOptions: {
      sass: {
        // Inject these css files into all component styles
        additionalData: `
          @import '@/scss/colors.scss';
        `,
      },
    },
  },
  pwa: {
    name: 'SizeSquirrel',
    themeColor: '#0776bc',
    msTileColor: '#131313',
    iconPaths: {
      favicon32: 'static/images/favicon/favicon-32x32.png',
      favicon16: 'static/images/favicon/favicon-16x16.png',
      appleTouchIcon: 'static/images/favicon/apple-touch-icon-152x152.png',
      maskIcon: 'static/images/favicon/safari-pinned-tab.svg',
      msTileImage: 'static/images/favicon/msapplication-icon-144x144.png',
    },
    workboxPluginMode: 'InjectManifest',
    workboxOptions: {
      importsDirectory: 'static/js',
      swSrc: './src/sw.js',
      swDest: 'service-worker.js',
    },
  },
};
