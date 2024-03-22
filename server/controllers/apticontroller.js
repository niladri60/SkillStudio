// Import required modules
const pool = require('../configDB/database');
const asyncHandler = require('express-async-handler');

// Function to get a single aptitude question
const getAptitudeQuestion = asyncHandler(async (req, res) => {
  try {
    // Query the database to get a single aptitude question
    const [row] = await pool.query('SELECT * FROM aptitude_questions ORDER BY RAND() LIMIT 1');
    
    // Send the single aptitude question as response
    res.status(200).json(row[0]); // Assuming the query returns an array with a single row
  } catch (error) {
    // Handle database errors
    console.error('Error fetching aptitude question:', error);
    res.status(500).json({ error: 'Failed to fetch aptitude question' });
  }
});
// Function to insert a question uploaded by the user
const insertUploadedQuestion = asyncHandler(async (req, res) => {
    const { question, optionA, optionB, optionC, optionD, correctOption } = req.body;
  
    try {
      // Insert the uploaded question into the database
      await pool.query('INSERT INTO uploaded_questions (question, option_a, option_b, option_c, option_d, correct_option) VALUES (?, ?, ?, ?, ?, ?)', [question, optionA, optionB, optionC, optionD, correctOption]);
  
      res.status(201).json({ message: 'Question uploaded successfully' });
    } catch (error) {
      // Handle database errors
      console.error('Error uploading question:', error);
      res.status(500).json({ error: 'Failed to upload question' });
    }
  });

// Export the getAptitudeQuestion function
module.exports = {
  getAptitudeQuestion,
  insertUploadedQuestion
};
