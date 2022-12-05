//reading the txt file
var fs = require('fs');
var array = fs.readFileSync('Day1Data.txt').toString().split("\n");

//part 1
//creating an array of arrays that contain each of the elve's calories
let temp = [];
let results = [];
array.map(x => {
    if(x) {
        temp.push(x);
    }
    else {
        results.push(temp);
        temp = [];
    }
})

//iterating through the array of arrays and finding the elf with the most calories
let calories = 0;
for (x in results) {
    temp = 0;
    for (y in results[x]) {
        temp += parseInt(results[x][y]);
        if (temp > calories) {
            calories = temp;
        }
    }
}
console.log(calories);

//part 2
//summing each elves' calories
let calories2 = []
for (x in results) {
    temp = 0;
    for (y in results[x]) {
        temp += parseInt(results[x][y]);
        calories2.push(temp)
    }
}
//sorting the array numerical from largest - smallest
calories2.sort(function(a, b) {
    return b - a;
  });
//summing the top 3 elf backpacks
let top3 = calories2[0] + calories2[1] + calories2[2]
console.log(top3)
