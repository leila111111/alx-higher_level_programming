#!/usr/bin/node
const a = Number(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < a) {
    console.log('X'.repeat(a));
    i++;
  }
}
