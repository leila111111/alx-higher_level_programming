#!/usr/bin/node
const a = Number(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < a) {
    console.log('C is fun');
    i++;
  }
}
