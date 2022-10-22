class Solution {
fun solution(num_list: IntArray): IntArray {
    var answer: IntArray = intArrayOf()
    for (i in 0 until num_list.size){
        answer = answer.plus((num_list[i])*2)
    }
    return answer
}
}