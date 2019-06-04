// https://algospot.com/judge/problem/read/TILING2
// n = 1 -> 1 / n = 2 - > 2 / n = 3 -> 3 ...
// n[k] = n[k-1] + n[k-2]

#include <stdio.h>

#define MAX 101
#define MOD 1000000007

int cache[MAX] = { 0, };
int n;

void tiling() {
	cache[1] = 1;
	cache[2] = 2;

	for (int i = 3; i < MAX; i++) {
		cache[i] = (cache[i - 1] + cache[i - 2]) % MOD;
	}
}

int main() {
	int testcase;

	scanf("%d", &testcase);

	tiling();
	while (testcase--) {
		scanf("%d", &n);

		printf("%d\n", cache[n]);
	}

	return 0;
}

/*

0 or 1 만 가능
0    1

0 or 1 처럼 채워지면 다 채울 수 없음
1    0

*/