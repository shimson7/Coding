class Solution {
fun solution(money: Int): IntArray {
    var answer: IntArray = intArrayOf()
    answer=answer.plus(money/5500)
    answer=answer.plus(money%5500)
    return answer
}
}