// https://algospot.com/judge/problem/read/DRAWRECT

#include <stdio.h>

int main() {
	int testcase;
	int a1, a2;
	int b1, b2;
	int c1, c2;
	int d1, d2;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d", &a1, &a2);
		scanf("%d %d", &b1, &b2);
		scanf("%d %d", &c1, &c2);

		if (a1 == b1) d1 = c1;
		else if (a1 == c1) d1 = b1;
		else d1 = a1;

		if (a2 == b2) d2 = c2;
		else if (a2 == c2) d2 = b2;
		else d2 = a2;

		printf("%d %d\n", d1, d2);
	}

	return 0;
}