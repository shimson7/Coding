import 'dart:io';
void main() {
  var line = stdin.readLineSync()!;
  List<String> items = line.split(' ');
  List<int> reversedItems = items.map((item) {
    String reversedString = item.split('').reversed.join('');
    return int.parse(reversedString);
  }).toList();
  int a = reversedItems[0];
  int b = reversedItems[1];

  // 삼항 연산자를 사용하여 a와 b 중 더 큰 값을 answer에 할당
  var answer = (a > b) ? items[0] : items[1];
  print(answer);
}