#!/usr/bin/node

const request = require('request')

const movieID = process.argv[2]

const starWarsAPI = `https:\/\/swapi-api.hbtn.io/api/films/${movieID}`

request(starWarsAPI, function (error, response, body) {
  console.log(JSON.parse(body).title);
});
