class Solution {
fun solution(common: IntArray): Int {
    var answer: Int = 0

    if (common[2] - common[1] == common[1] - common[0]) {
        //등차
        answer = common[common.size - 1] + (common[1] - common[0])
    } else {
        answer = common[common.size - 1] * (common[1] / common[0])
    }


    return answer
}
}