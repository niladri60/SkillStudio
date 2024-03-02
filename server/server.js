// Import required modules
const express = require('express');
const userroutes= require('./routes/useroutes')
const database= require('./configDB/database')
// Create an instance of Express
const app = express();
// Define the port number
const PORT = 3000;

// Define a route
app.use(express.json)
//signup 
app.use('/api',userroutes)
// Start the server
app.get('/home',(req,res)=>{
    res.json({ message: "hello" });
})
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
