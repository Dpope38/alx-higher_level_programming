#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[1]).pipe(fs.createWriteStream(process.argv[3]));
