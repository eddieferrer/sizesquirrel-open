/* eslint-disable no-unused-vars */
/* eslint-disable camelcase */
function gtag_report_conversion(url) {
  const callback = function () {
    if (typeof url !== 'undefined') {
      window.location = url;
    }
  };
  // eslint-disable-next-line no-undef
  gtag('event', 'conversion', {
    send_to: 'AW-872632887/0ru2CPfGyIUBELekjaAD',
    event_callback: callback,
  });
  return false;
}
