class Solution {
fun solution(array: IntArray): Int {
    var answer = 0
    var ary = Array<Int>(1001,{0})

    for (i in 0 until array.size){
        ary[array[i]]++
    }

    var max=0
    var maxIndex=0

    for (j in 0 until ary.size){
        if(ary[j]>max){
            max = ary[j]
            maxIndex=j
        }
    }

    var count = 0
    for (k in 0 until ary.size){
        if (ary[k]==max) count++
    }

    if (count>1) return -1
    answer=maxIndex
    return answer
}
}