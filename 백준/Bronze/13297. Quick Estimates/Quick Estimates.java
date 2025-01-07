import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int N = Integer.parseInt(ns.nextLine());
        for (int i = 0; i < N; i++) {
            String s = ns.nextLine(); // 문자열 입력받기
            System.out.println(s.length());
        }
    }
}

