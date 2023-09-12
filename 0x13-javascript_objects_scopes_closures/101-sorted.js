#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dict1 = {};
for (let key in dict) {
  if (dict1[dict[key]] === undefined) {
    dict1[dict[key]] = [key];
  } else {
    dict1[dict[key]] = dict1[dict[key]].concat(key);
  }
}
console.log(dict1);
