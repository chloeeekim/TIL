// https://algospot.com/judge/problem/read/POLY

#include <stdio.h>
#include <string.h>

#define MAX 10000000

int arr[100][100];

int polyomino(int rest, int before) {
	int ans = 0, count;

	if (arr[rest][before] != 0) return arr[rest][before];
	if (rest == before) return 1;

	for (int i = 1; i <= (rest - before); i++) {
		count = before + i - 1;
		if (!before) count = 1;
		count *= polyomino(rest - before, i);
		ans += (count%MAX);
		ans %= MAX;
	}

	return arr[rest][before] = ans;
}

int main() {
	int testcase;
	int n;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		memset(arr, 0, sizeof(int) * 100 * 100);
		printf("%d\n", polyomino(n, 0));
	}

	return 0;
}