#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const results = JSON.parse(body).results;
    count = results.reduce((acc, obj) => {
      return acc + obj.characters.filter(character => character.includes('18')).length;
    }, count);
  }
  console.log(count);
});
