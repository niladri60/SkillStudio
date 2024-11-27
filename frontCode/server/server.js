// Import required modules
const express = require('express');
const userroutes= require('./routes/useroutes')
const aptiroutes= require('./routes/aptiroutes')
const codingroutes= require('./routes/codingroutes')
const testroutes= require('./routes/testroutes')
const database= require('./configDB/database')
const Axios = require("axios");
const cors= require('cors')
const bodyParser = require('body-parser')
// Create an instance of Express
const app = express();
// Define the port number
const PORT = 5000;
// Define CORS options
const corsOptions = {
    origin: 'http://localhost:5173', // Allow requests from this origin
};
// Use CORS middleware with options
app.use(cors(corsOptions));
// Define a route
app.use(bodyParser.json())
//signup 
app.use('/api',userroutes)
app.use('/app',aptiroutes)
app.use('/app',codingroutes)
app.use('/app',testroutes)

app.post("/compile", (req, res) => {
    // getting the required data from the request
    let code = req.body.code;
    let language = req.body.language;
    let input = req.body.input;

    let languageMap = {
        "c": { language: "c", version: "10.2.0" },
        "cpp": { language: "c++", version: "10.2.0" },
        "python": { language: "python", version: "3.10.0" },
        "java": { language: "java", version: "15.0.2" }
    };

    if (!languageMap[language]) {
        return res.status(400).send({ error: "Unsupported language" });
    }

    let data = {
        "language": languageMap[language].language,
        "version": languageMap[language].version,
        "files": [
            {
                "name": "main",
                "content": code
            }
        ],
        "stdin": input
    };

    let config = {
        method: 'post',
        url: 'https://emkc.org/api/v2/piston/execute',
        headers: {
            'Content-Type': 'application/json'
        },
        data: data
    };

    // calling the code compilation API
    Axios(config)
        .then((response) => {
            res.json(response.data.run);  // Send the run object directly
            console.log(response.data);
        }).catch((error) => {
            console.log(error);
            res.status(500).send({ error: "Something went wrong" });
        });
});

// Start the server
app.get('/home',(req,res)=>{
    res.json({ message: "hello" });
})
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
