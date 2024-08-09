import React, { useState, useEffect } from 'react';
import { MonacoEditor } from '@monaco-editor/react';

function App() {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');

  useEffect(() => {
    // Send code to backend for execution
    fetch('/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, language }),
    })
      .then(response => response.json())
      .then(result => console.log(result));
  }, [code, language]);

  return (
    <div>
      <MonacoEditor
        language={language}
        value={code}
        onChange={(value) => setCode(value)}
      />
      <button onClick={() => setLanguage('java')}>Switch to Java</button>
      <button onClick={() => setLanguage('cpp')}>Switch to C++</button>
    </div>
  );
}
