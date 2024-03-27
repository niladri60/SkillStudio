const express= require('express')
const {getAptitudeQuestion, insertUploadedQuestion,getuploadedQuestion}= require('../controllers/apticontroller')
//Initializing app router
const router= express.Router()
router.get('/aptitude',getAptitudeQuestion)
router.post('/upload',insertUploadedQuestion)
router.get('/apti_questions',getuploadedQuestion)
//Export Router
module.exports= router