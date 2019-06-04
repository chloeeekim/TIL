// https://algospot.com/judge/problem/read/MAXSUM

#include <stdio.h>

#define MAX(a, b) ((a > b) ? a : b)

int main() {
	int testcase;
	int N, num;
	int thisSum, maxSum;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &N);
		thisSum = maxSum = 0;

		for (int i = 0; i < N; i++) {
			scanf("%d", &num);
			thisSum = MAX(thisSum + num, 0);
			maxSum = MAX(maxSum, thisSum);
		}

		printf("%d\n", maxSum);
	}

	return 0;
}