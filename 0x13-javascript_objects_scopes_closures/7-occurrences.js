#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const i = 0; i < list.length; i++) {
    if (searchElement === i) {
      n++;
    }
  }
  return n;
};
