class Solution {
    fun solution(emergency: IntArray): IntArray {
        val list = emergency.copyOf()
        list.sortDescending()
        for (i in list.indices) {
            emergency[i] = list.indexOf(emergency[i]) + 1
        }

        return emergency
    }
}