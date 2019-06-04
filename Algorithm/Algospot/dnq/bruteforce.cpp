// https://algospot.com/judge/problem/read/BRUTEFORCE

#include <stdio.h>

const long long MAX = 1000000007;
int n;
typedef long long L;

L func1(int m) {
	if (m == 1) return n;
	L val = func1(m / 2);
	if (m % 2 == 1) return ((val*val) % MAX)*n%MAX;
	else return (val*val) % MAX;
}

L func2(int m) {
	if (!m) return 0;
	else if (m == 1) return n;
	if (m % 2 == 1) return ((func2(m / 2)*(func1(m / 2) + 1)) + func1(m)) % MAX;
	else return (func2(m / 2)*(func1(m / 2) + 1)) % MAX;
}

int main() {
	int testcase;
	int a, b;
	L res;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d %d", &a, &b, &n);
		res = (func2(b) - func2(a - 1) + MAX) % MAX;
		printf("%lld\n", res);
	}

	return 0;
}