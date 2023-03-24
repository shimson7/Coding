#include <bits/stdc++.h>

using namespace std;

const string shortFrom[12] = {"CU", ":-)", ":-(", ";-)", ":-P", "(~.~)", "TA",
                              "CCC", "CUZ", "TY", "YW", "TTYL"};
const string translation[12] = {"see you", "I’m happy", "I’m unhappy", "wink",
                                "stick out my tongue", "sleepy", "totally awesome",
                                "Canadian Computing Competition", "because", "thank-you",
                                "you’re welcome", "talk to you later"};

string translate(const string& str) {
  for (int i = 0; i < 12; i++) {
    if (str == shortFrom[i])
      return translation[i];
  }
  return str;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  while (true){
    string input; cin >> input;
    cout << translate(input) << "\n";
    if (input == "TTYL") break ;
  }

  return 0;
}