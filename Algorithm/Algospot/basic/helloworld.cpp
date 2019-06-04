// https://algospot.com/judge/problem/read/HELLOWORLD

#include <stdio.h>

int main() {
	int num;
	char arr[51];
	scanf("%d", &num);
	while (num--) {
		scanf("%s", arr);
		printf("Hello, %s!\n", arr);
	}
	return 0;
}