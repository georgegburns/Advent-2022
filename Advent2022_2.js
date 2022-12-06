//reading the txt file
var fs = require('fs');
var array = fs.readFileSync('Day2Data.txt').toString().split("\n");

for (i in array){
    array[i] = array[i].replace(/[ZC]/g,'3');
    array[i] = array[i].replace(/[YB]/g,'2');
    array[i] = array[i].replace(/[XA]/g,'1');
}

let score = 0
for (i in array){
    if (array[i]) {
        if (array[i][0] === array[i][2]){
            score += 3 + parseInt(array[i][2]);
        }
        else if ((array[i][0] === "1" && array[i][2] === "2") || (array[i][0] === "2" && array[i][2] === "3") || (array[i][0] === "3" && array[i][2] === "1")){
            score += 6 + parseInt(array[i][2]);
        }
        else {
            score += parseInt(array[i][2]);
        }
    }
}

console.log(score);

let score2 = 0

for (i in array){
    if (array[i]){
        if (array[i][2] === "2"){
            if (array[i][0] === "1"){
                score2 += 4;
                }
            else if (array[i][0] === "2"){
                score2 += 5;
                }
            else {
                score2 += 6;
                }
            }
        else if (array[i][2] === "3"){
            if (array[i][0] === "1"){
                score2 += 8;
                }
            else if (array[i][0] === "2"){
                score2 += 9;
                }
            else {
                score2 += 7;
                }
            }
        else{
            if (array[i][0] === "1"){
                    score2 += 3;
                }
            else if (array[i][0] === "2"){
                    score2 += 1;
                }
            else {
                    score2 += 2;
                }
            }
        }
    }

console.log(score2)
