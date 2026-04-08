const http = require('http');
const countStudents = require('./3-read_file_async');

const DATABASE = process.argv[2];

const port = 1245;

const app = http.createServer(async (req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
	res.statusCode = 200;
	res.end('Hello Holberton School!');
    }
    else if (req.url === '/students') {
	res.statusCode = 200;
	res.write('This is the list of our students\n');
	try {
	    const studentsData = await countStudents(DATABASE);
	    res.end(studentsData);
	} catch (error) {
	    res.end(error.message);
	}
    }
    else {
	res.statusCode = 404;
	res.end('Not Found');
    }
});

app.listen(port);

module.exports = app;
