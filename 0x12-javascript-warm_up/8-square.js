#!/usr/bin/node
if (parseInt(process.argv[2])){
    for (let i = 0; i < parseInt(process.argv[2]); i++){
        let charType = "";
        for (let i = 0; i < parseInt(process.argv[2]); i++){
            charType = charType + "X";
        }
        console.log(charType);
    }
}
else{
    console.log("Missing size");
}