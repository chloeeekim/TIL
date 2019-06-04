// https://algospot.com/judge/problem/read/ZEROONE

#include <stdio.h>

char input[1000001];
int change[1000000];

int main() {
	scanf("%s", input);

	int num = 0, p = 0;
	change[0] = num;

	while (input[p] == '0' || input[p] == '1') {
		p++;
		if (input[p-1] != input[p]) num++;
		change[p] = num;
	}

	int testcase, i, j;
	scanf("%d", &testcase);

	while (testcase--) {

		scanf("%d %d", &i, &j);
		if (change[i] == change[j]) printf("Yes\n");
		else printf("No\n");
	}

	return 0;
}