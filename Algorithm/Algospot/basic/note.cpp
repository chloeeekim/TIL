// https://algospot.com/judge/problem/read/NOTE

#include <stdio.h>

int main() {
	int input[8];
	bool des = false, asc = false;
	
	scanf("%d", &input[0]);
	for (int i = 1; i < 8; i++) {
		scanf("%d", &input[i]);
		if (input[i - 1] > input[i]) des = true;
		else asc = true;

		if (des == true && asc == true) break;
	}
	
	if (des == true && asc == false) printf("descending\n");
	else if (des == false && asc == true) printf("ascending\n");
	else printf("mixed\n");

	return 0;
}