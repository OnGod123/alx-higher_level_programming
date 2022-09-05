#!/usr/bin/node
const fileArgs = process.argv;
if (fileArgs[2]){
    console.log(fileArgs[2]);
}
else{
    console.log("No argument");
}