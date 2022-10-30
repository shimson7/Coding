class Solution {
fun solution(my_str: String, n: Int): ArrayList<String> {
    var answer: ArrayList<String> = arrayListOf<String>()
    var word = ""
    var cnt = 0
    for (i in 0 until  my_str.length){
        if (cnt==n){
            answer.add(word)
            cnt=0
            word=""
        }
        word+=my_str[i]
        if (i==my_str.length-1){
            answer.add(word)
        }
        cnt+=1
    }


    return answer
}
}