// https://algospot.com/judge/problem/read/CSBASEBALL

#include <stdio.h>

int main() {
	int testcase;
	long long A, B;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%lld %lld", &A, &B);
		if (A > B) {
			printf("0\n");
			continue;
		}
		else {
			printf("%d\n", B - A + 4);
			continue;
		}
	}

	return 0;
}