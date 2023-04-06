#include <bits/stdc++.h>

using namespace std;

constexpr int SUN = 0;
constexpr int MOON = 1;

struct YEARS {
  int lsatCorrectPosYear,
      backToCorrectPosYear;
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  YEARS years[2];

  cin >> years[SUN].lsatCorrectPosYear >> years[SUN].backToCorrectPosYear;
  cin >> years[MOON].lsatCorrectPosYear >> years[MOON].backToCorrectPosYear;

  int nextSunEclipse = -years[SUN].lsatCorrectPosYear + years[SUN].backToCorrectPosYear,
      nextMoonEclipse = -years[MOON].lsatCorrectPosYear + years[MOON].backToCorrectPosYear;

  vector<int> sunEclipses, moonEclipses;
  sunEclipses.push_back(nextSunEclipse);
  moonEclipses.push_back(nextMoonEclipse);

  const int MAX_YEAR = 5000;
  while (true) {
    if (nextSunEclipse > MAX_YEAR && nextMoonEclipse > MAX_YEAR) break ;

    if (nextSunEclipse <= MAX_YEAR) {
      nextSunEclipse += years[SUN].backToCorrectPosYear;
      sunEclipses.push_back(nextSunEclipse);
    }

    if (nextMoonEclipse <= MAX_YEAR) {
      nextMoonEclipse += years[MOON].backToCorrectPosYear;
      moonEclipses.push_back(nextMoonEclipse);
    }
  }

  unordered_set<int> sunSet(sunEclipses.begin(), sunEclipses.end());

  for (auto& element : moonEclipses) {
    if (sunSet.find(element) != sunSet.end()) {
      cout << element << "\n";
      break ;
    }
  }

  return 0;
}