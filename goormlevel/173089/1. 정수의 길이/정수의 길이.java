import java.io.*;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = br.readLine();

    int num = 0;
    for (int i = 0; i < input.length(); i++) {
      num += 1; // 또는 num++;
    }

    System.out.println(num);
  }
}