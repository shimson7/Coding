class Solution {
fun solution(s1: Array<String>, s2: Array<String>): Int {
    var answer: Int = 0
    for (i in 0 until s1.size){
        if (s2.contains(s1[i])){
            answer+=1
        }
    }
    return answer
}
}