import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};
    students.forEach((line) => {
      const columns = line.split(',');
      if (columns.length >= 4) {
        const firstName = columns[0].trim();
        const field = columns[3].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }
    });

    resolve(fields);
  });
});

export default readDatabase;
