class Solution {
fun solution(array: IntArray): IntArray {
    var answer: IntArray = intArrayOf()
    var isitmax = array[0]
    for (i in 1 until array.size){
        if (isitmax<array[i]){
            isitmax=array[i]
        }
    }
    answer+=isitmax
    answer+=array.indexOf(isitmax)

    return answer
}
}