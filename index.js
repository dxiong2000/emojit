const express = require('express')
const app = express()
const port = 3000

const endpoints = require('./endpoints.js')

app.get('/', (req, res) => {
  res.send('Hello World!')
})

/**
 * localhost:3000/getEmoji?search=[SearchText]
 */
app.get('/getEmoji', endpoints.getEmoji);

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})