// https://algospot.com/judge/problem/read/WEIRD

#include <stdio.h>

int div[500001];
int div_num;
int num;

bool get_subset(int sum, int start) {
	if (sum == num) return true;
	if (sum < num) return false;

	for (int i = start; i < div_num; i++) {
		if (get_subset(sum - div[i], i + 1)) {
			return true;
		}
	}

	return false;
}

int get_div() {
	div_num = 0;
	div[div_num++] = 1;
	int sum = 1;

	int i;
	for (i = 2; i * i <= num; i++) {
		if (num % i == 0) {
			sum += div[div_num++] = i;
		}
	}

	for (i = div_num - 1; i > 0; i--) {
		int d = num / div[i];
		if (d * d != num) {
			sum += div[div_num++] = d;
		}
	}

	return sum;
}

int main() {
	int testcase;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &num);

		int sum = get_div();

		if (sum <= num || get_subset(sum, 0))
			printf("not weird\n");
		else
			printf("weird\n");
	}

	return 0;
}