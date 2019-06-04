// https://algospot.com/judge/problem/read/TRIPATHCNT

#include <stdio.h>
#include <string.h>

int arr[101][101];
int cal[101][101];

int main() {
	int testcase, n;
	int num, max, temp;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		memset(arr, 0, sizeof(int) * 101 * 101);
		memset(cal, 0, sizeof(int) * 101 * 101);
		temp = max = 0;

		scanf("%d", &arr[0][0]);
		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				scanf("%d", &num);
				if (arr[i - 1][j - 1] > arr[i - 1][j]) temp = arr[i - 1][j - 1] + num;
				else temp = arr[i - 1][j] + num;

				arr[i][j] = temp;
				if (temp > max) max = temp;
			}
		}

		for (int i = n - 1; i >= 0; i--) {
			if (arr[n - 1][i] == max) cal[n - 1][i] = 1;
			else cal[n - 1][i] = 0;
		}

		for (int i = n - 1; i > 0; i--) {
			for (int j = 0; j <= i; j++) {
				if (arr[i - 1][j - 1] < arr[i - 1][j]) cal[i - 1][j] += cal[i][j];
				else if (arr[i - 1][j - 1] > arr[i - 1][j]) cal[i - 1][j - 1] += cal[i][j];
				else {
					cal[i - 1][j - 1] += cal[i][j];
					cal[i - 1][j] += cal[i][j];
				}
			}
		}

		printf("%d\n", cal[0][0]);
	}

	return 0;
}