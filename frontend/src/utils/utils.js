const isEmpty = (obj) => {
  if (Object.keys(obj).length === 0) {
    return true;
  }
  return false;
};

// eslint-disable-next-line import/prefer-default-export
export { isEmpty };
