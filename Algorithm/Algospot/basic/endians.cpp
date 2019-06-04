// https://algospot.com/judge/problem/read/ENDIANS

#include <stdio.h>

typedef struct {
	char byte_1;
	char byte_2;
	char byte_3;
	char byte_4;
}number;

int main() {
	int testcase;
	
	scanf("%d", &testcase);
	while (testcase--) {
		unsigned int bf_num;
		unsigned int af_num;
		number* bf = (number *)&bf_num;
		number* af = (number *)&af_num;
		
		scanf("%u", &bf_num);

		af->byte_1 = bf->byte_4;
		af->byte_2 = bf->byte_3;
		af->byte_3 = bf->byte_2;
		af->byte_4 = bf->byte_1;

		printf("%u\n", af_num);
	}

	return 0;
}