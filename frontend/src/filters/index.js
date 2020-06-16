const capitalize = value => {
  if (!value) return '';
  const valueString = value.toString();
  return valueString.charAt(0).toUpperCase() + valueString.slice(1);
};

const titleCase = str => {
  if (!str) return '';
  return str
    .split(' ')
    .map(item => item.charAt(0).toUpperCase() + item.substring(1))
    .join(' ');
};

export { capitalize, titleCase };
