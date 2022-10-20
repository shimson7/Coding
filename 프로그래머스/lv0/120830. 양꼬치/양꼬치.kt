class Solution {
    fun solution(n: Int, k: Int): Int {
        var sheep=n*12000
        var service=n/10
        var drink=k*2000
        var answer: Int = sheep+drink-service*2000
        return answer
    }
}