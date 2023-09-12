#!/usr/bin/node
const files = require('fs');
const i = files.readFileSync(process.argv[2]);
const j = files.readFileSync(process.argv[3]);
files.writeFileSync(process.argv[4], i + j);
