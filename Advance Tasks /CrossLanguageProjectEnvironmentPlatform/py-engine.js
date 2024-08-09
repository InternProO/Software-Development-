const { spawn } = require('child_process');

class PythonEngine {
  execute(code, callback) {
    const process = spawn('python', ['-c', code]);

    process.stdout.on('data', (data) => {
      callback(data.toString());
    });

    process.stderr.on('data', (data) => {
      callback(`Error: ${data.toString()}`);
    });

    process.on('close', () => {
      callback('Execution completed');
    });
  }
}

module.exports = PythonEngine;
