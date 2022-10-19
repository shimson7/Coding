class Solution {
    fun solution(numbers: IntArray): Double {
    var answer: Double = 0.0
    var plus: Double= 0.0
    for (i: Int in 0 until numbers.size)
        plus+=numbers[i]
    answer=plus/numbers.size
    return answer
    }
}