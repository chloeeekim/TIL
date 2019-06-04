// https://algospot.com/judge/problem/read/PICNIC

#include <stdio.h>
#include <string.h>

bool friends[10][10];
bool contain[10];

int n, m;

int picnic() {
	int remain = -1;
	for (int i = 0; i < n; i++) {
		if (!contain[i]) {
			remain = i;
			break;
		}
	}

	if (remain == -1) return 1;

	int res = 0;
	for (int i = remain + 1; i < n; i++) {
		if (!contain[i] && friends[remain][i]) {
			contain[remain] = contain[i] = true;
			res += picnic();
			contain[remain] = contain[i] = false;
		}
	}

	return res;
}

int main() {
	int testcase;
	int a, b;

	scanf("%d", &testcase);
	while (testcase--) {
		memset(friends, false, sizeof(friends));
		memset(contain, false, sizeof(contain));

		scanf("%d %d", &n, &m);

		for (int i = 0; i < m; i++) {
			scanf("%d %d", &a, &b);
			friends[a][b] = friends[b][a] = true;
		}

		printf("%d\n", picnic());
	}

	return 0;
}