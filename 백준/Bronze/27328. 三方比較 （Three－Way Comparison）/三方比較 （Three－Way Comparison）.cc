#include <iostream>
using namespace std;

int A, B;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> A >> B;
	if (A < B) cout << -1;
	else if (A > B) cout << 1;
	else cout << 0;
}