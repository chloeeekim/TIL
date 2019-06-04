// https://algospot.com/judge/problem/read/DICT

#include <stdio.h>

typedef long long ll;
ll arr[101][101];

ll getArr(int n, int m) {
	if (n < 0 || m < 0) return 0;

	ll &ptr = arr[n][m];
	if (ptr) return ptr;
	if (n == 0 || m == 0) return ptr = 1;
	if (n == 1 || m == 1) return ptr = n + m;

	ptr = getArr(n - 1, m) + getArr(n, m - 1);
	return ptr > 1000000000 ? 1000000000 : ptr;
}

void printAns(int n, int m, int k) {
	if (n + m == 0) return;

	if (n == 0) while (m--) printf("b");
	else if (m == 0) while(n--) printf("a");
	else if (k > getArr(n - 1, m)) {
		printf("b");
		printAns(n, m - 1, k - getArr(n - 1, m));
	}
	else {
		printf("a");
		printAns(n - 1, m, k);
	}
}

int main() {
	int testcase;
	int n, m, k;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d %d", &n, &m, &k);

		if (getArr(n, m) < k) {
			printf("NONE\n");
		}
		else {
			printAns(n, m, k);
			printf("\n");
		}
	}

	return 0;
}