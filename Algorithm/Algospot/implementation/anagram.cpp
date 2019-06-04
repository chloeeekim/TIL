// https://algospot.com/judge/problem/read/ANAGRAM

#include <stdio.h>
#include <string.h>

int main() {
	int testcase;
	char str1[101], str2[101];
	int alp1[26], alp2[26];
	bool res;

	scanf("%d", &testcase);
	while (testcase--) {
		memset(alp1, 0, sizeof(int) * 26);
		memset(alp2, 0, sizeof(int) * 26);
		res = true;

		scanf("%s %s", str1, str2);

		if (strcmp(str1, str2) == 0) {
			printf("No.\n");
			continue;
		}

		for (int i = 0; ; i++) {
			if (str1[i] == '\0') break;
			alp1[str1[i] - 97]++;
			alp2[str2[i] - 97]++;
		}
		
		for (int i = 0; i < 26; i++) {
			if (alp1[i] != alp2[i]) {
				res = false;
				break;
			}
		}

		if (res == true) printf("Yes\n");
		else printf("No.\n");
	}

	return 0;
}