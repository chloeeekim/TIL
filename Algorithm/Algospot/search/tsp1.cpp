// https://algospot.com/judge/problem/read/TSP1

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define MAX 10

double map[MAX][MAX];
int visit[MAX];
int n;
double res;

bool check() {
	for (int i = 1; i <= n; i++) {
		if (visit[i] == 0) return false;
	}
	return true;
}

void tsp(int cur, double dis) {
	if (check()) {
		res = min(res, dis);
		return;
	}

	if (dis > res) return;
	
	for (int i = 1; i <= n; i++) {
		if (i != cur && visit[i] == 0) {
			visit[i] = 1;
			tsp(i, dis + map[cur][i]);
			visit[i] = 0;
		}
	}
}

int main() {
	int testcase;
	
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);
		memset(visit, 0, sizeof(int) * MAX);
		memset(map, 0, sizeof(double) * MAX * MAX);
		res = 0;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				scanf("%lf", &map[i][j]);
				if ((i+1) == j) res += map[i][j];
			}
		}

		visit[0] = 1;
		tsp(0, 0);

		printf("%.10lf\n", res);
	}

	return 0;
}