// Import required modules
const bcrypt = require('bcrypt');
const pool = require('../configDB/database');
const { createUsersTable } = require('../model/user_schema');
const asyncHandler = require('express-async-handler');

// Function to handle user registration (sign up)
const signUp = asyncHandler(async (req, res) => {
    const { username, email, password } = req.body;
  
    try {
      // Create the users table if it doesn't exist
      await createUsersTable();
       console.log("Going to Usertable")
       console.log(username)
       console.log(password)
       console.log(email)
      // Hash the password
      const hashedPassword = await bcrypt.hash(password, 10);
  
      // Insert user into the database
      await pool.query('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', [username, email, hashedPassword]);
  
      res.status(201).json({ message: 'User created successfully' });
    } catch (error) {
      // Handle database insertion errors
      console.error('Error creating user:', error);
      res.status(500).json({ error: 'Failed to create user' });
    }
  });

// Export the signUp function
module.exports = {
  signUp
};
