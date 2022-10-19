#!/usr/bin/node

const request = require("request");
const fs = require("fs");

const URL = process.argv[2];
const fileName = process.argv[3];

request(URL, function (error, response, body) {
  fs.writeFile(fileName, body, (err) => {
	if (err) throw err;
  })
});
