#include <iostream>
using namespace std;

int N;
int arr[100];
int T;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	while (N) {
		for (int i = 0; i < N; i++) cin >> arr[i];
		T++;
		cout << "Case " << T << ": ";
		int ans;
		if (N & 1) ans = arr[N / 2] * 10;
		else ans = (arr[N / 2 - 1] + arr[N / 2]) * 5;
		cout << ans / 10 << '.' << ans % 10 << '\n';

		cin >> N;
	}
}