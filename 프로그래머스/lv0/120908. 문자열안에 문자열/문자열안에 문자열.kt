class Solution {
fun solution(str1: String, str2: String): Int {
    var answer: Int = 0
    if (str2 in str1){
        answer=1
    }else{
        answer=2
    }

    return answer
}
}