import java.io.*;
class Main {
	public static String changeCase(String str) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        if (Character.isUpperCase(ch)) {
            sb.append(Character.toLowerCase(ch));
        } else if (Character.isLowerCase(ch)) {
            sb.append(Character.toUpperCase(ch));
        } else {
            sb.append(ch);
        }
    }
    return sb.toString();
}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num;
		num = Integer.parseInt(br.readLine());
		String input = br.readLine();
		System.out.println(changeCase(input));
	}
}