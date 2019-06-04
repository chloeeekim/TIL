// https://algospot.com/judge/problem/read/HOTSUMMER

#include <stdio.h>

int main() {
	int testcase;
	int W, A, sum;

	scanf("%d", &testcase);
	while (testcase--) {
		sum = 0;
		scanf("%d", &W);
		for (int i = 0; i < 9; i++) {
			scanf("%d", &A);
			sum += A;
		}
		if (sum <= W) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}