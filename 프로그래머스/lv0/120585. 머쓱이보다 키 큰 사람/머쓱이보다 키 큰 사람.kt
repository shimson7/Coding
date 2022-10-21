class Solution {
    fun solution(array: IntArray, height: Int): Int {
        var answer: Int = 0
        for (i in 0 until array.size){
            if (array[i]>height){
                answer+=1
            }
        }
        return answer
    }
}