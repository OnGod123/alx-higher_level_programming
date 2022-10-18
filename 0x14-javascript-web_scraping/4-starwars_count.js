#!/usr/bin/node

const request = require('request')

const charID = 'https://swapi-api.hbtn.io/api/people/18/';

const movieID = process.argv[3];

const starWarsAPI = process.argv[2]

request(starWarsAPI, function (error, response, body) {
  content = JSON.parse(body);

  let num = 0;
  let count = content["count"];
  for (i = 0; i < count; i++){
	if (content["results"][i]["characters"].includes(charID)){
		num++;
	}
}
  console.log(num);
});
