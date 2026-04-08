const http = require('http');

const PORT = 1245;
const HOST = 'localhost';

/**
 * Create the HTTP server.
 * The callback is executed every time an HTTP request hits the server.
 */
const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  
  res.end('Hello Holberton School!');
});

app.listen(PORT, HOST);

module.exports = app;
