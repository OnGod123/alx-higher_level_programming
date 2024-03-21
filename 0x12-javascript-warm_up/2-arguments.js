#!/usr/bin/node
/**
 * Prints a message depending on the number of arguments passed.
 * @param {string[]} args - An array containing command-line arguments.
 */
const printMessage = (args) => {
    
    if (args.length === 2) {
        console.log("No argument");
  
    else if (args.length === 3) {
        console.log("Argument found");
    }
    
    else {
        console.log("Arguments found");
    }
};


const args = process.argv;
printMessage(args);

