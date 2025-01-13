import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 입력: 새의 수
        int N = scanner.nextInt();
        scanner.close();

        int time = 0; // 총 걸린 시간
        int song = 1; // 현재 부를 노래 숫자

        while (N > 0) {
            if (N < song) {
                // 남은 새 수가 현재 부를 노래 수보다 작으면 초기화
                song = 1;
            }
            N -= song; // 노래를 부르고 새들이 날아감
            song++;    // 다음 노래 번호
            time++;    // 1초 추가
        }

        // 출력: 총 걸린 시간
        System.out.println(time);
    }
}
