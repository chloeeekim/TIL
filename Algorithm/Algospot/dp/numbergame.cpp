// https://algospot.com/judge/problem/read/NUMBERGAME
// 턴이 바뀌면 점수가 반대로 뒤집히므로 -해줌
// 특정 인덱스 범위에서의 점수를 cache에 저장

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int arr[50];
int low, high;
int cache[50][50];

int numgame(int low, int high) {
	if (low == high) return -arr[low];

	int& res = cache[low][high];
	if (res != -1) return res;

	res = -2000;
	if (high - low >= 2) {
		res = max(res, numgame(low + 2, high));
		res = max(res, numgame(low, high - 2));
	}
	if (high - low >= 1) {
		res = max(res, numgame(low + 1, high) + arr[low]);
		res = max(res, numgame(low, high - 1) + arr[high]);
	}
	res = -res;
	return res;
}

int main() {
	int testcase, n;

	scanf("%d", &testcase);
	while (testcase--) {
		memset(cache, -1, sizeof(int) * 50 * 50);
		scanf("%d", &n);
		
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}

		printf("%d\n", -numgame(0, n - 1));
	}

	return 0;
}