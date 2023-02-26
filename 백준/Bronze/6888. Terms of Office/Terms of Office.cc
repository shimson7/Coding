#include <iostream>
using namespace std;

int L, R;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> L >> R;
	while (L <= R) {
		cout << "All positions change in year " << L << '\n';
		L += 60;
	}
}