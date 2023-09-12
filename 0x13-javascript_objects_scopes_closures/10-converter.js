#!/usr/bin/node
exports.converter = function (base) {
  return function (node) {
    return node.toString(base);
  };
};
