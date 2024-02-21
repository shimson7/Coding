import java.util.*;

class Solution {
    public int[] solution() {
        int[] a = new int[3];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < a.length; i++) {
            int num = sc.nextInt();
            a[i]=num;
        }
//        System.out.println(Arrays.toString(a));
        int cal = a[0] * a[1] * a[2];
        String str = Integer.toString(cal);
        for (int i = 0; i < 10; i++) {
            int count = 0;
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) - '0' == i) {
                    count++;
                }
            }
            System.out.println(count);
        }

        return a;
    }
}

public class Main {
    public static void main(String[] ars) {
        Solution s = new Solution();
        s.solution();
    }
}