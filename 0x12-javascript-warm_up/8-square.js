#!/usr/bin/node

const arg = process.argv[2];
const squareSize = parserInt(arg);
const x = "x";

if(isNaN(parsedNumber)){
    console.log("Missing number of occurrences");
}else {
    for(let i = 0; i < squareSize; i++) {
        console.log(x.repeat(squareSize));
     }
}
