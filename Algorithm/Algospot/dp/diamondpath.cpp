// https://algospot.com/judge/problem/read/DIAMONDPATH

#include <stdio.h>

int arr[200][200];

int main() {
	int testcase;
	int n, num;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		scanf("%d", &arr[0][0]);

		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				scanf("%d", &num);
				if (arr[i - 1][j - 1] < arr[i - 1][j]) arr[i][j] = arr[i - 1][j] + num;
				else arr[i][j] = arr[i - 1][j - 1] + num;
			}
		}
		for (int i = n; i < n * 2 - 1; i++) {
			for (int j = 0; j < (n * 2 - 1 - i); j++) {
				scanf("%d", &num);
				if (arr[i - 1][j] > arr[i - 1][j + 1]) arr[i][j] = arr[i - 1][j] + num;
				else arr[i][j] = arr[i - 1][j + 1] + num;
			}
		}

		printf("%d\n", arr[2 * n - 2][0]);
	}

	return 0;
}