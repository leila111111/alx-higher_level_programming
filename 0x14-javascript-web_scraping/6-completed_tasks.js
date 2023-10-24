#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  if (response.statusCode === 200) {
    const result = {};
    const responses = JSON.parse(body);
    for (const i in responses) {
      const ji = responses[i];
      if (ji.completed) {
        if (result[ji.userId] === undefined) {
          result[ji.userId] = 1;
        } else {
          result[ji.userId]++;
        }
      }
    }
    console.log(result);
  }
});
