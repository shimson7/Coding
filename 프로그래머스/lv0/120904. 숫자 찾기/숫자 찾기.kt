class Solution {
fun solution(num: Int, k: Int): Int {
    var answer: Int = 0
    var temp=num.toString()
    for (i in 0 until temp.length){
        println(temp[i].digitToInt())
        if (temp[i].digitToInt()==k){
            answer=i+1
            break
        }else{
            answer=-1
        }
    }

    return answer
}
}