// https://algospot.com/judge/problem/read/ARCTIC


#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 987654321

typedef struct {
	double x;
	double y;
} point;

point map[100];
double dis[100][100];
int visit[100];
int n;

bool isConnected(double d) {
	memset(visit, 0, sizeof(visit));

	queue<int> que;
	que.push(0);
	int count = 0;

	visit[0] = 1;

	while (!que.empty()) {
		int temp = que.front();
		que.pop();
		count++;
		for (int i = 0; i < n; i++) {
			if (visit[i] == 0 && (dis[temp][i] <= d)) {
				visit[i] = 1;
				que.push(i);
			}
		}
	}

	return count == n;
}

double getDistance(point a, point b) {
	double dis = pow(a.x - b.x, 2) + pow(a.y - b.y, 2);
	return sqrt(dis);
}

double arctic(double low, double high) {
	if (isConnected(low)) return low;

	// testcase에 따라서 반복문 횟수를 늘리거나 줄여서 확인
	// 사실 100이 기본...
	for (int i = 0; i < 25; i++) {
		double mid = (low + high) / 2;
		if (isConnected(mid)) high = mid;
		else low = mid;
	}

	return low;
}

int main() {
	int testcase;
	double tmin;
	double low, high;
	
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf("%lf %lf", &map[i].x, &map[i].y);
		}

		high = low = -1;
		for (int i = 0; i < n; i++) {
			tmin = INF;
			for (int j = 0; j < n; j++) {
				if (i != j) {
					dis[i][j] = getDistance(map[i], map[j]);
					tmin = min(tmin, dis[i][j]);
					high = max(high, dis[i][j]);
				}
			}
			low = max(low, tmin);
		}

		printf("%.2lf\n", arctic(low, high));
	}

	return 0;
}