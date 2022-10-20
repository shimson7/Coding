class Solution {
    fun solution(n: Int): Int {
    /*
    형변환해서 문자열로 만들고
    문자열 한개씩 불러와서 정수형으로 형변환하고 값을 더해줌
    */
    var answer: Int = 0
    var temp=n.toString()
    for (i in 0 until temp.length){
        //아스키코드로 반환하고 있었음
        //answer+=temp[i].toInt()
        answer+=temp[i].digitToInt()
    }
    return answer
    }
}