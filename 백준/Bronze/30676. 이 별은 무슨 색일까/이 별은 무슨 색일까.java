import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int i = Integer.parseInt(br.readLine());
        if (i >= 620 && i <= 780) {
            bw.write("Red\n");
        } else if (i >= 590 && i < 620) {
            bw.write("Orange\n");
        } else if (i >= 570 && i < 590) {
            bw.write("Yellow\n");
        } else if (i >= 495 && i < 570) {
            bw.write("Green\n");
        } else if (i >= 450 && i < 495) {
            bw.write("Blue\n");
        } else if (i >= 425 && i < 450) {
            bw.write("Indigo\n");
        } else if (i >= 380 && i < 425) {
            bw.write("Violet\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
