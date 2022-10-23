class Solution {
    fun solution(angle: Int): Int {
    var answer: Int = 0
    if (angle<90){
        answer=1
    }else if(angle==90) {
        answer=2
    }else if(angle in 91 until 180) {
        answer=3
    }else{
        answer=4
    }
    return answer
}
}