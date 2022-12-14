class Solution {
fun solution(array: IntArray): Int {
    array.sort()
    var answer: Int = array.size/2
    return array[answer]
}
}