import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // System.setIn(new FileInputStream("src/input.txt"));

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());

            int N = Integer.parseInt(br.readLine());
            for (int i = 0; i < N; ++i) {
                st = new StringTokenizer(br.readLine());
                double z = Double.parseDouble(st.nextToken());
                String q = st.nextToken();

                double multiplier = (q.equals("A") ? y / x : x / y);
                bw.write(Double.toString(z * multiplier));
                bw.newLine();
            }

            bw.flush();
        }
    }
}