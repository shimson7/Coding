#include <iostream>
using namespace std;

int main() {
  while (1) {
    double x, y;
    cin >> x >> y;

    if (x == 0 && y == 0) {
      cout << "AXIS";
      break;
    }

    if (x > 0 && y > 0) {
      cout << "Q1\n";
    } else if (x > 0 && y < 0) {
      cout << "Q4\n";
    } else if (x < 0 && y > 0) {
      cout << "Q2\n";
    } else if (x < 0 && y < 0) {
      cout << "Q3\n";
    } else {
      cout << "AXIS\n";
    }
  }

  return 0;
}