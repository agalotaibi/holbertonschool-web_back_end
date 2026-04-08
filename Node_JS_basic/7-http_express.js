const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;
const DATABASE = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});


app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  
  try {
    const data = await countStudents(DATABASE);
    res.end(data);
  } catch (error) {
    res.end(error.message);
  }
});

app.listen(PORT);

module.exports = app;
