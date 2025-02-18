const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 2105;

// Replace <username> and <password> with your MongoDB Atlas credentials
const mongoURI = process.env.MONGO_URI || 'mongodb+srv://2215016135:KlAZEpfj64MG3tCz@sbdprakt10.lug5lx3.mongodb.net/?retryWrites=true&w=majority&appName=sbdPrakt10';

// Middleware to parse JSON bodies
app.use(express.json());

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch(err => {
    console.error('Failed to connect to MongoDB', err);
  });

// Sample endpoint to ensure server is running
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

// Endpoint to verify MongoDB connection
app.get('/status', async (req, res) => {
  try {
    const dbStatus = await mongoose.connection.db.admin().ping();
    res.json({ status: 'Connected to MongoDB', dbStatus });
  } catch (err) {
    res.status(500).json({ status: 'Error', message: err.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});