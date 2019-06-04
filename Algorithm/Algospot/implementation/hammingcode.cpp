// https://algospot.com/judge/problem/read/HAMMINGCODE

#include <stdio.h>

char arr[8];

int main() {
	int testcase;
	int syndrome;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%s", arr);

		syndrome = 0;

		if ((arr[0] + arr[2] + arr[4] + arr[6]) % 2 == 1) syndrome += 1;
		if ((arr[1] + arr[2] + arr[5] + arr[6]) % 2 == 1) syndrome += 2;
		if ((arr[3] + arr[4] + arr[5] + arr[6]) % 2 == 1) syndrome += 4;

		syndrome--;

		if (arr[syndrome] == '0') arr[syndrome] = '1';
		else arr[syndrome] = '0';

		printf("%c%c%c%c\n", arr[2], arr[4], arr[5], arr[6]);
	}

	return 0;
}