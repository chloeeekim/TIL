// https://algospot.com/judge/problem/read/ROUTING

#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;

#define MAX 10001

struct edge {
	int next;
	double weight;
	bool operator < (const edge& p) const {
		if (abs(weight - p.weight) < 1e-9) return next < p.next;
		return weight > p.weight;
	}
};

vector<edge> adj[MAX];
bool visit[MAX];
double cost[MAX];

int n;

void dijkstra() {
	priority_queue<edge> pq;
	pq.push({ 0, 1 });
	cost[0] = 1;
	visit[0] = true;

	while (!pq.empty()) {
		int cur = pq.top().next;
		double weight = pq.top().weight;
		pq.pop();

		if (cur == n - 1) break;

		for (int i = 0; i < adj[cur].size(); i++) {
			int next = adj[cur][i].next;
			double next_w = cost[cur] * adj[cur][i].weight;
			if (!visit[next] || cost[next] > next_w) {
				visit[next] = true;
				cost[next] = next_w;
				pq.push({ next, next_w });
			}
		}
	}
}

int main() {
	int testcase;
	int m;
	int a, b;
	double c;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d", &n, &m);

		memset(visit, false, sizeof(visit));
		memset(cost, -1, sizeof(cost));

		for (int i = 0; i < n; i++) {
			adj[i].clear();
		}

		for (int i = 0; i < m; i++) {
			scanf("%d %d %lf", &a, &b, &c);
			adj[a].push_back({ b,c });
			adj[b].push_back({ a,c });
		}		

		dijkstra();

		printf("%lf\n", cost[n - 1]);
	}

	return 0;
}