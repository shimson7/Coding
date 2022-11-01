class Solution {
fun solution(n: Int, numlist: IntArray): MutableList<Int> {
    var answer: MutableList<Int> = mutableListOf<Int>()
    for (i in 0 until numlist.size){
        if (numlist[i]%n==0){
            answer.add(numlist[i])
        }
    }
    return answer
}
}