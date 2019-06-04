// https://algospot.com/judge/problem/read/POTION

#include <stdio.h>
#include <algorithm>
using namespace std;

int rec[200]; // recipe
int cur[200]; // current

int gcd(int a, int b) {
	if (a < b) {
		int temp = a;
		a = b;
		b = temp;
	}
	return b == 0 ? a : gcd(b, a%b);
}

int cal(int a, int b) {
	if (a % b == 0) return a / b;
	else return (a / b + 1);
}

int main() {
	int testcase;
	int n, up, down;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		scanf("%d", &rec[0]);
		down = rec[0];
		for (int i = 1; i < n; i++) {
			scanf("%d", &rec[i]);
			down = gcd(down, rec[i]);
		}

		int up = down;
		for (int i = 0; i < n; i++) {
			scanf("%d", &cur[i]);
			up = max(up, cal(cur[i] * down, rec[i]));
		}

		for (int i = 0; i < n; i++) {
			printf("%d ", (rec[i] * up / down) - cur[i]);
		}
		printf("\n");

	}

	return 0;
}