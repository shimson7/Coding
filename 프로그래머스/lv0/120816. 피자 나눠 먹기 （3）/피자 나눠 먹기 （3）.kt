class Solution {
    fun solution(slice: Int, n: Int): Int {
    var answer: Int = 0
    var cal = n%slice
    if (cal==0){
        answer=n/slice
    }else{
        answer=(n/slice)+1
    }
    return answer
}
}