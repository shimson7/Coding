class Solution {
fun solution(my_string: String): IntArray {
    var answer: IntArray = intArrayOf()
    for (i in 0 until my_string.length){
        if(my_string[i].isDigit()){
            answer=answer.plus(my_string[i].digitToInt())
        }
    }
    answer.sort()
    return answer
}
}