// https://algospot.com/judge/problem/read/COINS
// n원을 만들 수 있는 가짓수 = (동전이 있다면 +1) + (n원 - x원)의 가짓수

#include <stdio.h>
#include <string.h>

#define MAX 1000000007

long long cal[10001];
long long res;

int main() {
	int testcase, m, c;
	int num;
	
	scanf("%d", &testcase);
	while (testcase--) {
		res = 0;
		scanf("%d %d", &m, &c);

		memset(cal, 0, sizeof(long long) * (m + 1));

		for (int i = 0; i < c; i++) {
			scanf("%d", &num);

			if (num > m) continue;
			cal[num]++;

			for (int j = 1; num + j <= m; j++) {
				if (cal[j] > 0) cal[j + num] += cal[j];
			}
		}

		res = cal[m];
		if (res > MAX) printf("%lld\n", res % MAX);
		else printf("%lld\n", res % MAX);
	}

	return 0;
}