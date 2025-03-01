import 'dart:io';
void main() {
	int? quizs = int.parse(stdin.readLineSync()!);
  List<int> numbers = stdin.readLineSync()!.split(" ").map(int.parse).toList();
	int flag = 0;
	int score = 0;
	for (var i =0; i < quizs; i++) {
		if (numbers[i] == 1) {
			flag++;
		}
		else if (numbers[i] == 0) flag=0;
		score+=flag;
	}
	print(score);
}