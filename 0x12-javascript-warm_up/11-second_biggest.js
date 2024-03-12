#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));

if(numbers.lenght < 2){
    console.log(0);
} else {
    const sortNumbers = numbers.sort((a, b) => b - a );
    console.log(sortNumbers);
}
