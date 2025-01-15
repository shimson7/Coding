import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String search = scanner.nextLine();
        
        if (search.equals("N")) {
            System.out.println("Naver D2");
        } else if (search.equals("n")) {
            System.out.println("Naver D2");
        } else {
            System.out.println("Naver Whale");
        }
    }
}