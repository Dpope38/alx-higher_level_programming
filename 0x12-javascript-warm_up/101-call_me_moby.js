#!/usr/bin/node

const callMeMoby = (x, theFunction) => {
    if(x > 0){
        theFunction();
        callMeMoby(x-1, theFunction);
  }
};

module.export.callMeMoby = callMeMoby;
