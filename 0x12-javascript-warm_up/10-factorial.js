#!/usr/bin/node
function factorial(num){
    if (num === 0){
        return(1);
    }
    return num * factorial(num - 1);
}
const factNum = parseInt(process.argv[2]) ? parseInt(process.argv[2]) : 0;
console.log(factorial(factNum));