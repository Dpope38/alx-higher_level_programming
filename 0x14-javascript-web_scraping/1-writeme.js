#!/usr/bin/node

const fs = require('fs');
const filePath = process.agrv[1];
const content = process.argv[2];

fs.writeFile(filePath, content, 'utf-8', (err, data) => {
    if (err) {
        console.log(err)
    }
})
