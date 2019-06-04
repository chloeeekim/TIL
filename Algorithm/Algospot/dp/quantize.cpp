// https://algospot.com/judge/problem/read/QUANTIZE
// ∑(arr[i]-mean)^2 = (high-low+1)*mean^2 - 2*(∑arr[i])*mean + ∑arr[i]^2

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define MAX 105
#define IMAX 987654321

int arr[MAX];
int sum[MAX];
int sqsum[MAX];
int err[MAX][MAX];
int cal[MAX][11];
int n, s;

void getError(int low, int high) {
	int subsum = sum[high] - sum[low - 1];
	int sqsubsum = sqsum[high] - sqsum[low - 1];

	int ave = (subsum / (high - low + 1.0)) + 0.5;
	
	int res = sqsubsum - (2 * ave * subsum) + (ave * ave * (high - low + 1));
	/*
	for (int i = low; i <= high; i++) {
		res += pow(ave - arr[i], 2);
	}
	*/
	err[low][high] = res;
}

int quantize(int index, int uses) {
	if (index > n) return 0;
	if (uses >= s) return IMAX;

	int& num = cal[index][uses];
	if (num != -1) return num;
	
	num = IMAX;
	for (int i = index; i <= n; i++) {
		num = min(num, err[index][i] + quantize(i + 1, uses + 1));
	}

	return num;
}

int main() {
	int testcase;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d", &n, &s);

		memset(cal, -1, sizeof(cal));
		
		for (int i = 1; i <= n; i++) {
			scanf("%d", &arr[i]);
		}

		sort(arr + 1, arr + n + 1);

		for (int i = 1; i <= n; i++) {
			sum[i] = sum[i - 1] + arr[i];
			sqsum[i] = sqsum[i - 1] + (arr[i] * arr[i]);
		}

		for (int i = 1; i <= n; i++) {
			for (int j = i; j <= n; j++) {
				getError(i, j);
			}
		}

		printf("%d\n", quantize(1, 0));
	}

	return 0;
}