#!/usr/bin/node
const fs = require("fs");

const filePath = process.argv[2];

// Check if a file path is provided
if (!filePath) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

// Read the file with utf-8 encoding and handle errors
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

