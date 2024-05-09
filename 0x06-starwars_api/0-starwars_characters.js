#!/usr/bin/node

const request = require('request');
const util = require('util')
const url = 'https://swapi-api.alx-tools.com/api/films/';
/// pass cmd line arg to url which is the movie id

const requestPromise = util.promisify(request);
async function getCharacterName(character) {
  const response = await requestPromise(character);
  if (response.statusCode === 200) {
    const data = JSON.parse(response.body);
    console.log(data.name);
  }
}

request(url + process.argv[2], async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const character of data.characters) {
      await getCharacterName(character);
    }
  }
});
