#!/usr/bin/node
const request = require('request');

const filmsUrl = process.argv[2];
const characterId = 18; // Wedge Antilles ID

// Check for API URL argument
if (!filmsUrl) {
  console.error('Please provide the Star Wars API URL as the first argument.');
  process.exit(1);
}

let movieCount = 0; // Count of movies with Wedge Antilles

function getFilms(url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const data = JSON.parse(body);
      // Check for next page URL
      if (data.next) {
        getFilms(data.next); // Recursively call for next page
      }
      // Process films from current page
      data.results.forEach((film) => {
        const characterUrls = film.characters;
        // Check if character URLs exist
        if (characterUrls) {
          characterUrls.forEach((characterUrl) => {
            checkCharacter(characterUrl); // Check for Wedge Antilles in each character URL
          });
        }
      });
    }
  });
}

function checkCharacter(url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const characterData = JSON.parse(body);
      if (characterData.url === `https://swapi-api.alx-tools.com/api/people/${characterId}/`) {
        movieCount++; // Increment count if character ID matches Wedge Antilles
      }
    }
  });
}

getFilms(filmsUrl);

// After all requests are complete, print the movie count
process.on('exit', () => {
  console.log(movieCount);
});

