// https://algospot.com/judge/problem/read/JUMPGAME

#include <stdio.h>
#include <string.h>

#define MAX 120
int cal[MAX][MAX];

char buf[100000000];
char *b = buf;

int getNum() {
	int num = 0;
	while (*b < '0' || *b > '9') b++;
	while (*b >= '0' && *b <= '9') {
		num = num * 10 + (*b - '0');
		b++;
	}

	return num;
}

int main() {
	int testcase, n, num;

	fread(buf, 1, sizeof(buf), stdin);

	//scanf("%d", &testcase);
	testcase = getNum();

	while (testcase--) {
		//scanf("%d", &n);
		n = getNum();
		
		memset(cal, 0, sizeof(int) * MAX * MAX);

		cal[0][0] = 1;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				//scanf("%d", &num);
				num = getNum();
				if (cal[i][j] == 1) {
					cal[i + num][j] = cal[i][j + num] = 1;
				}
			}
		}

		if (cal[n - 1][n - 1] == 1) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}