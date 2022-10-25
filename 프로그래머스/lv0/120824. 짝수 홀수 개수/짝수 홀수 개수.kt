class Solution {
    fun solution(num_list: IntArray): IntArray {
    var odd: IntArray = intArrayOf()
    var even: IntArray = intArrayOf()
    var answer: IntArray = intArrayOf()
    for (i in 0 until num_list.size){
        if (num_list[i]%2==0){
            even=even.plus(num_list[i])
        }else{
            odd=odd.plus(num_list[i])
        }
    }
    answer=answer.plus(even.size)
    answer=answer.plus(odd.size)
    return answer
}
}