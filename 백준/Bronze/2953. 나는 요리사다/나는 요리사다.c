#include<stdio.h>
int main(void) {
	int count[5] = {};
	for (int i = 0; i < 5; i++) {
		int num1, num2, num3, num4;
		scanf("%d %d %d %d", &num1, &num2, &num3, &num4);
		int num[4] = { num1, num2, num3, num4 };
		count[i] = num1 + num2 + num3 + num4;
	}
	int max = count[0];
	int idx = 0;
	for (int j = 0; j < 5; j++) {
		if (max < count[j]) {
			max = count[j];
			idx = j;
		}
	}
	printf("%d %d", idx+1, max);
}