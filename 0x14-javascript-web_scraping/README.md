Star Wars: Counting Wedge Antilles Appearances
This JavaScript script retrieves data from the Star Wars API (https://swapi.dev/) and calculates the number of movies where the character "Wedge Antilles" appears.

Features
Retrieves film information from the Star Wars API.
Filters characters based on their URL for efficiency.
Counts movies featuring "Wedge Antilles" (character ID 18).
Handles pagination for API results (if applicable).
Requirements
Node.js and npm installed on your system.
The request module: npm install request
Usage
Save the script as a .js file (e.g., count_wedge_movies.js).

Run the script with the Star Wars API URL for films as the first argument:

Bash
node count_wedge_movies.js https://swapi-api.alx-tools.com/api/films
Use code with caution.
content_copy
The script will output the number of movies where "Wedge Antilles" is present.

Code Structure
The script consists of two main functions:

getFilms(url):
Fetches film data from the provided URL using the request module.
Parses the JSON response and checks for pagination.
If pagination exists, recursively calls itself with the next page URL.
Iterates over each film's characters array (if present) and calls checkCharacter for each character URL.
checkCharacter(url):
Fetches character data from the provided URL.
Parses the JSON response and compares the character URL to the URL for "Wedge Antilles".
If the URLs match, increments the movieCount variable.
Additional Notes
This script utilizes asynchronous requests to handle pagination and character lookups efficiently.
The process.on('exit') event ensures the script waits for all requests to complete before printing the final count.

