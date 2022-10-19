#!/usr/bin/node

const request = require("request");
const API_URL = process.argv[2];

request(API_URL, function (error, response, body) {
	let content = JSON.parse(body);
	let userCount = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0}
	let usercount = content.length;
	for (i = 0; i < usercount; i++){
		if (content[i]["completed"]){
			userCount[content[i]["userId"].toString()] += 1
		}
	}

	console.log(userCount);
});
