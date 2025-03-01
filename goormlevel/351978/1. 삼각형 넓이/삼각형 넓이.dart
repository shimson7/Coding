import 'dart:io';
void main() {
	var line = stdin.readLineSync()!;
	  // 공백을 기준으로 입력값 나누기
  var inputs = line.split(' '); 
  // 각각의 값을 정수로 변환하여 저장
  var w = int.parse(inputs[0]);
  var h = int.parse(inputs[1]);
	var result = w*h/2;
	print(result.toStringAsFixed(1));
}