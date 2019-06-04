// https://algospot.com/judge/problem/read/NQUEEN

#include <stdio.h>
#include <algorithm>

#define MAX 20

int n;
int arr[MAX];
int count;

bool check(int cur) {
	for (int i = 0; i < cur; i++) {
		if ((arr[i] == arr[cur]) || (cur - i == abs(arr[cur] - arr[i]))) {
			return false;
		}
	}

	return true;
}

void nqueen(int cur) {
	if (cur == n - 1) {
		count++;
		return;
	}

	for (int i = 0; i < n; i++) {
		arr[cur + 1] = i;
		if (check(cur + 1)) {
			nqueen(cur + 1);
		}
	}
}

int main() {
	int testcase;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);
		count = 0;
		nqueen(-1);
		printf("%d\n", count);
	}

	return 0;
}