#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int h1, b1, h2, b2; cin >> h1 >> b1 >> h2 >> b2;

  int player1Score = 3 * h1 + b1,
      player2Score = 3 * h2 + b2;

  string ans = "NO SCORE";
  if (player1Score > player2Score)
    ans = "1 " + to_string((player1Score - player2Score));
  else if (player2Score > player1Score)
    ans = "2 " + to_string((player2Score - player1Score));
  cout << ans << "\n";

  return 0;
}