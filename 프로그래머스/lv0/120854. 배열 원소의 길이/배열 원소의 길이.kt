class Solution {
fun solution(strlist: Array<String>): IntArray {
    var answer: IntArray = intArrayOf()
    for (i in 0 until strlist.size){
        answer+=strlist[i].length
    }
    
    return answer
}
}