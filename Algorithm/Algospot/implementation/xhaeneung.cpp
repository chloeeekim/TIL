// https://algospot.com/judge/problem/read/XHAENEUNG

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char number[11][10] = { {"eorz"}, {"eno"}, {"otw"}, {"eehrt" }, {"foru"}, {"efiv"}, {"isx"}, {"eensv"}, {"eghit"}, {"einn"}, {"ent"} };

int compare(const void *a, const void *b) {
	return strcmp((char*)a, (char*)b);
}

int main() {
	int testcase;

	char num1[10], num2[10], num3[10];
	int n1, n2, n3, res;
	char op, ch;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%s %c %s %c %s", num1, &op, num2, &ch, num3);
		
		n1 = n2 = n3 = -1;

		qsort(num1, strlen(num1), sizeof(char), compare);
		qsort(num2, strlen(num2), sizeof(char), compare);
		qsort(num3, strlen(num3), sizeof(char), compare);

		for (int i = 0; i < 11; i++) {
			if (strcmp(number[i], num1) == 0) n1 = i;
			if (strcmp(number[i], num2) == 0) n2 = i;
			if (strcmp(number[i], num3) == 0) n3 = i;
		}

		if (n1 == -1 || n2 == -1 || n3 == -1) {
			printf("No\n");
			continue;
		}

		switch (op) {
		case '+': res = n1 + n2;
			if (res > 10 || res != n3) printf("No\n");
			else printf("Yes\n");
			break;
		case '-': res = n1 - n2;
			if (res < 0 || res != n3) printf("No\n");
			else printf("Yes\n");
			break;
		case '*': res = n1 * n2;
			if (res > 10 || res != n3) printf("No\n");
			else printf("Yes\n");
			break;
		default: break;
		}
	}

	return 0;
}