#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];

// Check for episode ID argument
if (!episodeId) {
  console.error('Please provide an episode ID as the first argument.');
  process.exit(1);
}

// Build the API endpoint URL
const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

// Send GET request to Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Movie not found.');
    }
  }
});

