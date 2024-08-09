const { Java } = require('java');

class JavaEngine {
  execute(code, callback) {
    const java = new Java();

    java.compile(code, (err, result) => {
      if (err) {
        callback(`Error: ${err}`);
        return;
      }

      java.run(result, (output) => {
        callback(output);
      });
    });
  }
}

module.exports = JavaEngine;
