#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[1];

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data.toString());
    }
})

