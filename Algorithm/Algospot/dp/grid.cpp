// https://algospot.com/judge/problem/read/GRID

#include <stdio.h>
#include <string.h>

int cache[6][10000];
int w;

int grid(int cur, int type) {
	int temp, next;

	if (w == cur) return 1;
	if (w == cur + 1) {
		if (type == 4) return 0; // 못 채움
		else return 1;
	}

	if (cache[type][w - 1 - cur] != -1) {
		return cache[type][w - 1 - cur];
	}

	next = cur + 1;
	temp = 0;

	switch (type) {
	case 0 : 
		temp += grid(next, 0);
		temp += grid(next, 1);
		temp += grid(next, 2);
		temp += grid(next, 3);
		temp += grid(next, 5);
		break;
	case 1 : 
		temp += grid(next, 0);
		temp += grid(next, 2);
		break;
	case 2 : 
		temp += grid(next, 0);
		temp += grid(next, 1);
		break;
	case 3 : 
		temp += grid(next, 0);
		temp += grid(next, 4);
		break;
	case 4 : 
		temp += grid(next, 3);
		break;
	case 5 : 
		temp += grid(next, 0);
		break;
	}

	cache[type][w - 1 - cur] = temp;
	return temp;
}

int main() {
	int testcase;
	int res;

	memset(cache, -1, sizeof(int) * 6 * 10000);
	
	scanf("%d", &testcase);
	for (int i = 1 ; i <= testcase ; i++) {

		scanf("%d", &w);

		printf("%d %d\n", i, grid(0, 0));
	}

	return 0;
}

/*

*** 현재 column을 다 채우는 것이 목적이므로
0    10
0 -> 13 과 같은 형태는 X
0    23
0    20

// type 0 -> 0, 1, 2, 3, 5
0    10    11    10    11    11
0 -> 10 or 22 or 10 or 20 or 22
0    20    30    22    20    33
0    20    30    33    33    44

// type 1 -> 0, 2
1    10    10
1 -> 10 or 10
0    20    22
0    20    33

// type 2 -> 0, 1
0    20    22
0 -> 20 or 33
1    10    10
1    10    10

// type 3 -> 0, 4
1    10    10
0 -> 20 or 22
0    20    33
1    10    10

// type 4 -> 3
0    22    
1 -> 10
1    10
0    33

// type 5 -> 0
1    10
1 -> 10
1    10
1    10

*/