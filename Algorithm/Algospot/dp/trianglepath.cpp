// https://algospot.com/judge/problem/read/TRIANGLEPATH

#include <stdio.h>
#include <string.h>

int arr[100][100];

int main() {
	int testcase;
	int n, num;
	int res, temp;

	scanf("%d", &testcase);

	while (testcase--) {
		scanf("%d", &n);

		memset(arr, 0, sizeof(int) * 100 * 100);
		res = 0;

		scanf("%d", &arr[0][0]);
		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				scanf("%d", &num);
				if (arr[i - 1][j - 1] > arr[i - 1][j]) temp = arr[i - 1][j - 1] + num;
				else temp = arr[i - 1][j] + num;
				arr[i][j] = temp;
				if (temp > res) res = temp;
			}
		}
		printf("%d\n", res);
	}

	return 0;
}