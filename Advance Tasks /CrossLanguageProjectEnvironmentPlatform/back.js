const express = require('express');
const app = express();
const languageEngines = {};

// Register language engines
languageEngines.python = require('./python-engine');
languageEngines.java = require('./java-engine');
languageEngines.cpp = require('./cpp-engine');

app.post('/execute', (req, res) => {
  const { code, language } = req.body;
  const engine = languageEngines[language];

  if (!engine) {
    res.status(400).send(`Language ${language} not supported`);
    return;
  }

  engine.execute(code, (result) => {
    res.json(result);
  });
});

app.listen(3000, () => console.log('Server listening on port 3000'));
