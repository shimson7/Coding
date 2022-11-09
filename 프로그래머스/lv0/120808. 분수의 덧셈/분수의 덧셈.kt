class Solution {
fun solution(denum1: Int, num1: Int, denum2: Int, num2: Int): IntArray {
    //분자
    var topNum = num1*denum2 + num2*denum1
    //분모
    var botNum = num1*num2
    // 최소 공배수
    var maximum = 1
    // 약분
    for (i in 1 .. topNum){
        if(topNum%i == 0 && botNum % i ==0){
            maximum = i
        }
    }

    return intArrayOf(topNum/maximum, botNum/maximum)
}
}