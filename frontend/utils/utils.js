const isEmpty = (obj) => {
  if (Object.keys(obj).length === 0) {
    return true;
  }
  return false;
};

const sizeOptions = () => {
  const arrayOfUSUKSizes = [];
  const arrayOfEuroSizes = [];
  for (let i = 3; i < 16; i++) {
    arrayOfUSUKSizes.push(
      {
        text: `${i} US / ${i - 1} UK`,
        value: i.toString(),
      },
      {
        text: `${i}.5 US / ${i - 1}.5 UK`,
        value: (i + 0.5).toString(),
      }
    );
  }
  for (let j = 33; j < 49; j++) {
    arrayOfEuroSizes.push(
      {
        text: `${j} EUR`,
        value: j.toString(),
      },
      {
        text: `${j}.5 EUR`,
        value: (j + 0.5).toString(),
      }
    );
  }
  return [
    {
      standard: 'US / UK Sizes',
      sizes: arrayOfUSUKSizes,
    },
    {
      standard: 'European Sizes',
      sizes: arrayOfEuroSizes,
    },
  ];
};

export { isEmpty, sizeOptions };
