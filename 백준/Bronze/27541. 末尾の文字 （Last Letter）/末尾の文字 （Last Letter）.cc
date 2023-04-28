#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;
  string input; cin >> input;

  if (input[n - 1] == 'G') input.erase(n - 1, 1);
  else input.push_back('G');

  cout << input << "\n";

  return 0;
}