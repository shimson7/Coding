class Solution {
    fun solution(n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        for (num in 1 .. n){
            if (n%num==0){
                answer+=num
            }
        }
        return answer
    }
}