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
    console.log(solution(str))
});

function solution(s) {
    let answer = "";
    for(let x of s){
        if(x===x.toUpperCase()) answer += x.toLowerCase()
        else answer += x.toUpperCase();
    }

    return answer;
}