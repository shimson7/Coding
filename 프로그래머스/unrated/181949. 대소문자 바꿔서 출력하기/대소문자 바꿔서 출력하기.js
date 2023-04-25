const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    var answer = "";
    for(var x of str){
        if(x===x.toUpperCase()) answer += x.toLowerCase()
        else answer += x.toUpperCase();
    }
    console.log(answer);
});