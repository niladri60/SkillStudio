// Import required modules
const express = require('express');
const userroutes= require('./routes/useroutes')
const aptiroutes= require('./routes/aptiroutes')
const codingroutes= require('./routes/codingroutes')
const database= require('./configDB/database')
const bodyParser = require('body-parser')
// Create an instance of Express
const app = express();
// Define the port number
const PORT = 5000;

// Define a route
app.use(bodyParser.json())
//signup 
app.use('/api',userroutes)
app.use('/app',aptiroutes)
app.use('/app',codingroutes)
// Start the server
app.get('/home',(req,res)=>{
    res.json({ message: "hello" });
})
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
