#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const results = JSON.parse(body).characters;
    printresult(results, 0);
  }
});
function printresult (results, i) {
  request(results[i], (error, response, body) => {
    if (error) console.error(error);
    else {
      console.log(JSON.parse(body).name);
      if (i + 1 < results.length) {
        printresult(results, i + 1);
      }
    }
  });
}
