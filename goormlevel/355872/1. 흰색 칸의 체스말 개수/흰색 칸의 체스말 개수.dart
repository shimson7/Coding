import 'dart:io';
void main() {
  List<List<int>> board = [];
  for (int i = 0; i < 8; i++) {
    String line = stdin.readLineSync()!;
    board.add(line.split('').map(int.parse).toList());
  }
  int count = 0;
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      // 하얀 칸은 (i + j) % 2 == 0인 칸
      if ((i + j) % 2 == 0 && board[i][j] == 1) {
        count++;
      }
    }
  }
  print(count);
}