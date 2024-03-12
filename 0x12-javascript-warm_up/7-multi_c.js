#!/usr/bin/node

const arg = process.argv[2];
const parsedNumber = parserInt(arg);

if(isNaN(parsedNumber)){
    console.log("Missing number of occurrences");
}else {
    for(let i = 0; i < parsedNumber; i++) {
        console.log("C is fun");
     }
}
