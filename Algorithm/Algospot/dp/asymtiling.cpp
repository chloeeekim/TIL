// https://algospot.com/judge/problem/read/ASYMTILING
// 대칭 고려 x : 1, 2, 3, 5, 8, 13, ...
// 대칭되는 경우 : 1, 2, 1, 3, 2, 5, ...
// Asymtile : 0, 0, 2, 2, 6, 8, ...

#include <stdio.h>
#include <string.h>

#define MAX 101
#define MOD 1000000007

int alltile[MAX];
int sym[MAX];

void tiling() {
	alltile[1] = 1;
	alltile[2] = 2;
	alltile[3] = 3;
	alltile[4] = 5;

	sym[1] = 1;
	sym[2] = 2;
	sym[3] = 1;
	sym[4] = 3;

	for (int i = 5; i < MAX; i++) {
		alltile[i] = (alltile[i - 1] + alltile[i - 2]) % MOD;
		sym[i] = (sym[i - 2] + sym[i - 4]) % MOD;
	}
}

int asymtiling(int w) {
	int res = (alltile[w] - sym[w] + MOD) % MOD;

	return res;
}

int main() {
	int testcase, n;

	tiling();
	
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		printf("%d\n", asymtiling(n));
	}

	return 0;
}