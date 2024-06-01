#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

// Check for URL argument
if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

// Send the GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

