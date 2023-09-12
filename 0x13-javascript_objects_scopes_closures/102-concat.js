#!/usr/bin/node
const files = require('files');
const i = files.readFile(process.argv[2]);
const j = files.readFile(process.argv[3]);
files.writeFile(process.argv[4], i + j);
