#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const fileString = process.argv[3];

fs.writeFile(fileName, fileString, (err) => {
	if (err) throw err;
})
