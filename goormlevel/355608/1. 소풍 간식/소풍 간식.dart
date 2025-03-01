import 'dart:io';
	/*
	홀수일때 / 2 + 1 * 몫
	짝수일때 / 2  * 몫
	*/
void main() {
	int N = int.parse(stdin.readLineSync()!);
	int quotient = N~/2;
	if (N%2==1){
		print((quotient+1)*quotient); 
	} else if (N%2==0){
		print((quotient)*quotient);
	}
}