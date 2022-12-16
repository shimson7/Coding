class Solution {
fun solution(order: Int): Int {
    var answer: Int = 0
    var orderToString = order.toString()
    for (i in 0 until orderToString.length){
        if(orderToString[i]=='3'||orderToString[i]=='6'||orderToString[i]=='9') answer+=1
    }
    return answer
}
}