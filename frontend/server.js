const express = require('express');
const history = require('connect-history-api-fallback');

const app = express();

app.use(history());
app.use(express.static('dist'));

app.listen(5555, () => {
  // eslint-disable-next-line no-console
  console.log('SizeSquirrel UI listening on port 5555!');
});
