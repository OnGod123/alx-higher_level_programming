#!/usr/bin/node
//This file prints the content of a file//
const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, (err, inputD) => {
   if (err) throw err;
      console.log(inputD.toString());
})
