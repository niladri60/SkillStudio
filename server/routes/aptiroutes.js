const express= require('express')
const {getAptitudeQuestion, insertUploadedQuestion}= require('../controllers/apticontroller')
//Initializing app router
const router= express.Router()
router.get('/aptitude',getAptitudeQuestion)
router.post('/upload',insertUploadedQuestion)
//Export Router
module.exports= router