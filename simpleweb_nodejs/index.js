const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('How are you doing');
});

app.listen(5050, () => {
  console.log('Listening on port 5050');
});
