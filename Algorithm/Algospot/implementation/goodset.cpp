// https://algospot.com/judge/problem/read/GOODSET

#include <stdio.h>
#include <string.h>

int pro[501];

int main() {
	int testcase;
	int N, M, X, num;
	bool isGoodSet;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d", &N, &M);

		memset(pro, 0, sizeof(int) * 501);

		isGoodSet = true;
		for (int i = 0; i < N; i++) {
			scanf("%d", &X);
			if (X == 0 || X == M) {
				isGoodSet = false;
			}
			for (int j = 0; j < X; j++) {
				scanf("%d", &num);
				pro[num] ++;
			}
		}
		
		if (isGoodSet == false) {
			printf("NO\n");
		}
		else {
			for (int i = 1; i <= M; i++) {
				if (pro[i] == 0) {
					isGoodSet = false;
					break;
				}
			}

			if (isGoodSet == false) printf("NO\n");
			else printf("YES\n");
		}
	}

	return 0;
}