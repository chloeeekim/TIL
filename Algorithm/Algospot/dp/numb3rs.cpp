// https://algospot.com/judge/problem/read/NUMB3RS

#include <stdio.h>
#include <string.h>

int map[50][50];
int connect[50];
double cal1[50];
double cal2[50];

int main() {
	int testcase;
	int n, d, p;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d %d", &n, &d, &p);
		
		memset(connect, 0, sizeof(int) * 50);
		memset(cal1, 0, sizeof(double) * 50);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &map[i][j]);
				if (map[i][j] == 1 && j > i) {
					connect[i]++;
					connect[j]++;
				}
			}
		}

		cal1[p] = 1.0;

		while (d--) {
			memset(cal2, 0, sizeof(double) * 50);

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < i; j++) {
					if (map[i][j] == 1) {
						cal2[i] += cal1[j] / (double)connect[j];
						cal2[j] += cal1[i] / (double)connect[i];
					}
				}
			}

			for (int i = 0; i < n; i++) {
				cal1[i] = cal2[i];
			}
		}

		int t, q;

		scanf("%d", &t);
		while (t--) {
			scanf("%d", &q);
			printf("%.8f ", cal1[q]);
		}
		printf("\n");
	}

	return 0;
}