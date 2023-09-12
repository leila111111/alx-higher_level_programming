#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dicti = {};
for (let key in dict) {
  if (dicti[dict[key]] === undefined) {
    dicti[dict[key]] = [key];
  } else {
    dicti[dict[key]] = dicti[dict[key]].concat(key);
  }
}
console.log(dicti);
