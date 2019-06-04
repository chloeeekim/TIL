// https://algospot.com/judge/problem/read/PREFIX

#include <stdio.h>
#include <string.h>

char arr[3000][201];
int cal[3000][201];

int main() {
	int testcase;
	int N, M;
	int val;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d", &N, &M);

		memset(cal, 0, sizeof(int) * 3000 * 201);

		for (int i = 0; i < N; i++) {
			scanf("%s", &arr[i]);
		}

		for (int i = 0; i < M; i++) {
			if (arr[0][i] == '\0') break;
			cal[0][i] = 1;
		}

		for (int i = 1; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == '\0') {
					j = M;
					continue;
				}

				if (arr[i][j] == arr[i - 1][j] && cal[i][j - 1] != 1) {
					cal[i][j] = cal[i - 1][j] + 1;
				}
				else {
					cal[i][j] = 1;
				}
			}
		}

		int max, max_line;
		
		for (int i = 0; i < M; i++) {
			max = max_line = -1;

			for (int j = 0; j < N; j++) {
				if (cal[j][i] > max) {
					max = cal[j][i];
					max_line = j;
				}
			}

			for (int k = 0; k <= i; k++) {
				printf("%c", arr[max_line][k]);
			}

			printf("\n");
		}
	}

	return 0;
}