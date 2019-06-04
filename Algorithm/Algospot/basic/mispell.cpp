// https://algospot.com/judge/problem/read/MISPELL

#include <stdio.h>

int main() {
	int testcase;
	int M;
	char str[81];

	scanf("%d", &testcase);
	for (int i = 1; i <= testcase; i++) {
		scanf("%d %s", &M, str);

		printf("%d ", i);
		for (int j = 0; ; j++) {
			if (str[j] == '\0') break;
			if (j == M - 1) continue;
			printf("%c", str[j]);
		}
		printf("\n");
	}

	return 0;
}