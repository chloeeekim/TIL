// https://algospot.com/judge/problem/read/MEETING

#include <stdio.h>
#include <algorithm>
using namespace std;

#define MAX 10000

int man[MAX];
int woman[MAX];

int main() {
	int testcase;
	int i, n, res;

	scanf("%d", &testcase);
	while (testcase--) {
		res = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", &man[i]);
		}
		for (i = 0; i < n; i++) {
			scanf("%d", &woman[i]);
		}

		sort(man, man + n);
		sort(woman, woman + n);

		for (i = 0; i < n; i++) {
			res += abs(man[i] - woman[i]);
		}

		printf("%d\n", res);
	}

	return 0;
}