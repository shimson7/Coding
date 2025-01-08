import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner ns = new Scanner(System.in);
        int N = Integer.parseInt(ns.nextLine());
        for (int i = 0; i < N; i++) {
            String s = ns.nextLine();
            String[] values = s.split(" ");
            int a = Integer.parseInt(values[0]);
            int b = Integer.parseInt(values[1]);
            if (a<b){
                System.out.println("NO BRAINS");
            }else {
                System.out.println("MMM BRAINS");
            }
        }
    }
}