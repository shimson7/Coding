import 'dart:io';
void main() {
	var line = stdin.readLineSync()!;
	var number = 0;
	List< String > parts = line.split(' ');
	for (int i = 0; i < parts.length; i++) {
		if (parts[i] != ''){
			   number++;
		}
	}
	// print(parts);
	print(number);
}