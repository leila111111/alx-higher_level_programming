#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const first = process.argv.slice(2);
  const second = first.sort((a, b) => a - b);
  console.log(second[second.length - 2]);
}
