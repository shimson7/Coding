import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();	// 조사한 시간
		int m = scan.nextInt();	// 터널안 차량 수
		int temp = m;
		int result = m;
		
		for(int i=0; i<n; i++) {
			int in = scan.nextInt();	// 입구 통과한 차의 수
			int out = scan.nextInt();	// 출구 통과한 차의 수
			temp = temp + in - out;
			
			// 터널안 차량의 수가 0보다 작은경우 0 출력, 0보다 큰경우 -> 이전의 최댓값과 비교
			result = (temp < 0) ? 0 : Math.max(temp, result);
			if(result == 0)	break;
		}
		System.out.println(result);
		scan.close();
	}

}
