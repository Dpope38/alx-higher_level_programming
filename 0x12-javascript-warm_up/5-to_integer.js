#!/usr/bin/node

const arg = process.argv[2];
const parseNumber = parseInt(arg);

if(isNaN(parseNumber)){
    console.log("Not a number");
}else {
    console.log(`My number: ${parseNumber}`);
}
