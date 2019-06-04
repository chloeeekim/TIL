// https://algospot.com/judge/problem/read/URI

#include <stdio.h>

int main() {
	char arr[81];
	int testcase;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%s", arr);
		for (int i = 0; ; i++) {
			if (arr[i] == '%') {
				i += 2;
				switch (arr[i]) {
				case '0': printf(" "); break;
				case '1': printf("!"); break;
				case '4': printf("$"); break;
				case '5': printf("%%"); break;
				case '8': printf("("); break;
				case '9': printf(")"); break;
				case 'a': printf("*"); break;
				default: break;
				}
			}
			else if (arr[i] == '\0') break;
			else printf("%c", arr[i]);
		}
		printf("\n");
	}

	return 0;
}