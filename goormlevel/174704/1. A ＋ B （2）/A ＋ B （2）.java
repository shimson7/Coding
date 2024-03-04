import java.io.*;

import java.math.BigDecimal;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] tokens = input.split(" "); // 공백을 기준으로 문자열을 분리
        BigDecimal num1 = new BigDecimal(tokens[0]); // 첫 번째 실수
        BigDecimal num2 = new BigDecimal(tokens[1]); // 두 번째 실수

        BigDecimal sum = num1.add(num2); // 두 개의 BigDecimal 값을 더함
        System.out.println(sum.setScale(6, BigDecimal.ROUND_HALF_UP)); // 결과값을 소수 여섯 자리까지 반올림하여 출력
    }
}
