class Solution {
fun solution(my_string: String, letter: String): String {
    var answer: String = ""
    for (i in 0 until my_string.length){
        if(my_string[i].toString()==letter){
            continue
        }
        answer+=my_string[i]
    }
    return answer
}
}