class Solution {
fun solution(n: Int, t: Int): Int {
    var answer: Int = n
    for (i in 0 until t) {
        answer*=2
    }
    return answer
}
}