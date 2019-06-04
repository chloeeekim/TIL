// https://algospot.com/judge/problem/read/BRAVEDUCK

#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef struct {
	int x;
	int y;
} point;

int inQueue[102];
int n, j;

bool canjump(point a, point b) {
	double dis = pow(a.x - b.x, 2) + pow(a.y - b.y, 2);
	return dis <= j * j;
}

int main() {
	int testcase;
	int x, y;
	point item;
	point start;
	point end;

	scanf("%d", &testcase);
	while (testcase--) {	
		queue<point> pointque;
		vector<point> stone;

		scanf("%d", &j);

		memset(inQueue, 0, sizeof(inQueue));

		scanf("%d %d", &start.x, &start.y);
		scanf("%d %d", &end.x, &end.y);

		scanf("%d", &n);
		
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &item.x, &item.y);
			stone.push_back(item);			
		}

		stone.push_back(end);

		pointque.push(start);
		while (!pointque.empty() && !inQueue[n]) {
			point temp = pointque.front();
			pointque.pop();

			for (int i = 0; i <= n; i++) {
				if (inQueue[i] == 1) continue;
				if (canjump(temp, stone[i])) {
					inQueue[i] = 1;
					pointque.push(stone[i]);
				}
			}
		}

		if (inQueue[n] == 1) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}