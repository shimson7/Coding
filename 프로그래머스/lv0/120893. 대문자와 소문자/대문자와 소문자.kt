class Solution {
fun solution(my_string: String): String {
    var answer: String = ""
    for (i in 0 until my_string.length) {
        if (my_string[i].isUpperCase()){
            answer+=my_string[i].lowercase()
        }else if (my_string[i].isLowerCase()){
            answer+=my_string[i].uppercase()
        }
    }

    return answer
}
}