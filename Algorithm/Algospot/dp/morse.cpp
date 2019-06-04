// https://algospot.com/judge/problem/read/MORSE

#include <stdio.h>

typedef long long ll;
ll arr[101][101];

ll getComb(int n, int m) {
	if (n < 0 || m < 0) return 0;

	ll &ret = arr[n][m];
	if (ret) return ret;
	if (m == 0 || n == 0) return ret = 1;
	if (m == 1 || n == 1) return ret = n + m;

	ret = getComb(n - 1, m) + getComb(n, m - 1);
	return ret > 1000000000 ? 1000000000 : ret;
}

void printAns(int n, int m, int k) {
	if (n + m == 0) return;
	
	if (n == 0) while (m--) printf("o");
	else if (m == 0) while (n--) printf("-");
	else if (k > getComb(n - 1, m)) {
		printf("o");
		printAns(n, m - 1, k - getComb(n - 1, m));
	}
	else {
		printf("-");
		printAns(n - 1, m, k);
	}
}

int main() {
	int testcase;
	int n, m, k;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d %d", &n, &m, &k);

		printAns(n, m, k);
		printf("\n");
	}

	return 0;
}