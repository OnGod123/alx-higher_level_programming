#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

// Check for required arguments
if (!filePath || !content) {
  console.error('Please provide both file path and content to write.');
  process.exit(1);
}

// Write the file with utf-8 encoding and handle errors
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote content to ${filePath}`);
  }
});

