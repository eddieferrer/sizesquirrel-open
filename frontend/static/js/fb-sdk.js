/* eslint-disable prefer-const */
window.fbAsyncInit = function () {
  // prod appId
  let appId = '943851385727348';
  if (window.location.hostname === 'localhost') {
    // dev appId
    appId = '944781472301006';
  }
  FB.init({
    appId,
    autoLogAppEvents: true,
    xfbml: true,
    version: 'v5.0',
  });
  FB.AppEvents.logPageView();
};

(function (d, s, id) {
  let js;
  const fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {
    return;
  }
  js = d.createElement(s);
  js.id = id;
  js.src = '//connect.facebook.net/en_US/sdk.js';
  fjs.parentNode.insertBefore(js, fjs);
})(document, 'script', 'facebook-jssdk');
