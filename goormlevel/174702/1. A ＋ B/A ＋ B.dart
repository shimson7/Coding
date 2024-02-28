import 'dart:io';
void main() {
	var line = stdin.readLineSync()!;
	List<String> values = line.split(' ');
	int A = int.parse(values[0]);
	int B = int.parse(values[1]);
	print(A+B);
}