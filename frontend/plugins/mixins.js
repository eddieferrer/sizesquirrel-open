import Vue from 'vue';

if (!Vue.__my_mixin__) {
  Vue.__my_mixin__ = true;
  // Vue Mixins
  // TODO move these out of this file
  Vue.mixin({
    methods: {
      deepFind(obj, path) {
        const paths = path.split('.');
        let current = obj;
        let i;

        for (i = 0; i < paths.length; ++i) {
          if (Array.isArray(current)) {
            [current] = current;
          }
          if (current[paths[i]] === undefined) {
            return undefined;
          }
          current = current[paths[i]];
        }

        return current;
      },
      getClass(percentage) {
        if (percentage > 50) {
          return 'is-success';
        }
        if (percentage < 50) {
          return 'is-warning';
        }
        // if (percentage === 50) {
        return 'is-danger';
      },
      notEmptyObject(someObject) {
        return Object.keys(someObject).length !== 0;
      },
      getParameterByName(name) {
        if (process.browser) {
          const match = RegExp(`[?&]${name}=([^&]*)`).exec(
            window.location.search
          );
          return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
        } else {
          return undefined;
        }
      },
      openFbLoginDialog(formType, redirect) {
        if (process.browser) {
          // prod appId
          let appId = '943851385727348';
          let protocol = 'https';
          let port = '';
          if (window.location.hostname === 'localhost') {
            // dev appId
            protocol = 'http';
            port = ':3000';
            appId = '944781472301006';
          }
          const redirecturi = `${protocol}://${window.location.hostname}${port}/facebookcallback_${formType}/`;
          const stateParams = {
            redirect,
            time: new Date().getTime(), // Not currently used
          };

          const facebookURL = `https://www.facebook.com/v5.0/dialog/oauth?client_id=${appId}&redirect_uri=${redirecturi}&response_type=token&scope=email&state=${JSON.stringify(
            stateParams
          )}`;
          window.location.href = facebookURL;
        }
      },
    },
  });
}
