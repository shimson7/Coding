import java.util.*;

// 알고리즘 문제
class Solution {
    public int[] solution() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int max = 0;
        int min = 0;
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            arr[i] = num;
        }
        Arrays.sort(arr);
        min= arr[0];
        max = arr[n-1];
        System.out.println(min + " " + max);
        return null;
    }
}

public class Main {
    public static void main(String[] ars) {
        Solution s = new Solution();
        s.solution();
    }
}