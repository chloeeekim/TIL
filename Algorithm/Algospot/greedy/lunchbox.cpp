// https://algospot.com/judge/problem/read/LUNCHBOX

// heap -> 시간초과
// 그리디하게 단순 먹는 시간으로 정렬하면 되는 문제 ㅠㅠ

// struct 사용
#include <stdio.h>
#include <algorithm>
using namespace std;

struct item {
	int m_time;
	int e_time;
} arr[10001];

bool compare(item a, item b) {
	return a.e_time > b.e_time;
}

int main() {
	int testcase, n, res, start;
	scanf("%d", &testcase);
	while (testcase--) {
		res = start = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i].m_time);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i].e_time);
		}
		
		sort(arr, arr + n, compare);

		for (int i = 0; i < n; i++) {
			start += arr[i].m_time;
			res = max(res, start + arr[i].e_time);
		}

		printf("%d\n", res);
	}
}