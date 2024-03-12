#!/usr/bin/node

const addMeMaybe = (number, callBack) => {
    number++;
    callBack(number);
}

module.export.addMeMaybe = addMeMaybe;
