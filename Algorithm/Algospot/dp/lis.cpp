// https://algospot.com/judge/problem/read/LIS

#include <stdio.h>

int main() {
	int testcase;
	int N, tar;
	int arr[500];
	int cal[500];
	int res;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &N);

		res = 0;
		cal[0] = 1;
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			tar = 1;
			for (int j = 0; j < i; j++) {
				if (arr[j] < arr[i] && cal[j] >= tar) tar = cal[j] + 1;
			}
			cal[i] = tar;
			if (tar > res) res = tar;
		}

		printf("%d\n", res);
	}

	return 0;
}