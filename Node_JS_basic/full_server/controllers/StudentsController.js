import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((fields) => {
        const lines = ['This is the list of our students'];
        const sorted = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        sorted.forEach((field) => {
          lines.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        });
        res.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((fields) => {
        const students = fields[major] || [];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
