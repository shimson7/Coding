import kotlin.math.sqrt
import kotlin.math.pow

class Solution {
    fun solution(n: Long): Long {
        return if(sqrt(n.toDouble()) % 1 == 0.0) (sqrt(n.toDouble())+1).pow(2).toLong() else -1
    }
}