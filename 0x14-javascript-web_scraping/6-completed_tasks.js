#!/usr/bin/node

const request = require("request");
const API_URL = process.argv[2];

request(API_URL, function (error, response, body) {
	let content = JSON.parse(body);
	let userCount = {}
	let usercount = content.length;
	for (i = 0; i < usercount; i++){
		if (!userCount.hasOwnProperty(content[i]["userId"].toString())){
			userCount[content[i]["userId"].toString()] = 0;
		}
		else if (userCount.hasOwnProperty(content[i]["userId"].toString())
 && content[i]["completed"]){
			userCount[content[i]["userId"].toString()] += 1
		}
	}

	console.log(userCount);
});
