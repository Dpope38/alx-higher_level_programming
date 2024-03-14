#!/usr/bin/node

const supSquare = require("./5-square.js");

class Square extends supSquare{
    charPrint(c) {
        if(c === undefined){
            c = "X";
        }
        for(let i = 0; i < this.width; i++) {
            for(let j = 0; j < this.height; j++{
                console.log(c);
            }
        }
    }
}

module.exports = Square;
