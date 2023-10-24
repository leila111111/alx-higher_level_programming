#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  const result = JSON.parse(body).characters;
  for (const i of result) {
    request(i, (error, response, body) => {
      if (error) console.log(error);
      const results = JSON.parse(body);
      console.log(results.name);
    });
  }
});
