#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let n = 0;
  while (len > 0 && len > n) {
    const node = list[len];
    list[len] = list[n];
    list[n] = node;
    n++;
    len--;
  }
  return list;
};
