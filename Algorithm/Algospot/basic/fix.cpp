// https://algospot.com/judge/problem/read/FIX

#include <stdio.h>

int main() {
	int testcase;
	int N, nanido;
	int res;

	scanf("%d", &testcase);
	while (testcase--) {
		res = 0;
		scanf("%d", &N);
		for (int i = 1; i <= N; i++) {
			scanf("%d", &nanido);
			if (nanido == i) res++;
		}

		printf("%d\n", res);
	}

	return 0;
}