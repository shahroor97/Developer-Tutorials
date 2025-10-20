// src/server.js
const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

// built-in JSON body parser
app.use(express.json());

// simple JSON endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: "ok" });
});

// start server
app.listen(PORT, () => {
  console.log(`API listening on http://localhost:${PORT}`);
});
