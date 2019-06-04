// https://algospot.com/judge/problem/read/ENCRYPT

#include <stdio.h>
#include <string.h>

int main() {
	int testcase, len;
	char arr[101];
	
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%s", arr);
		len = strlen(arr);

		for (int i = 0; i < len ; i = i + 2) {
			printf("%c", arr[i]);
		}
		for (int i = 1; i < len; i = i + 2) {
			printf("%c", arr[i]);
		}
		printf("\n");
	}

	return 0;
}