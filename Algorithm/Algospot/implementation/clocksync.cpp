// https://algospot.com/judge/problem/read/CLOCKSYNC

#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

#define MAX 16

int clock[MAX];
int button_num[9];

vector<vector<int> > button({
	vector<int>({ 0, 1, 2 }),
	vector<int>({ 3, 7, 9, 11 }),
	vector<int>({ 4, 10, 14, 15 }),
	vector<int>({ 0, 4, 5, 6, 7 }),
	vector<int>({ 6, 7, 8, 10, 12 }),
	vector<int>({ 0, 2, 14, 15 }),
	vector<int>({ 3, 14, 15 }),
	vector<int>({ 4, 5, 7, 14, 15 }),
	vector<int>({ 1, 2, 3, 4, 5 }),
	vector<int>({ 3, 4, 5, 9, 13 })
});

void clickButton(int index, int time) {
	if (time == 0) return;

	for (int i = 0; i < button[index].size() ; i++) {
		int num = button[index][i];

		clock[num] += 3 * time;
		if (clock[num] > 12) clock[num] -= 12;
	}
}

int main() {
	int testcase;
	int res, num;

	scanf("%d", &testcase);
	while (testcase--) {
		res = 0;
		memset(button_num, 0, sizeof(int) * 9);

		for (int i = 0; i < MAX; i++) {
			scanf("%d", &clock[i]);
		}

		if (clock[8] != clock[12]) {
			printf("-1\n");
			continue;
		}
		if (clock[14] != clock[15]) {
			printf("-1\n");
			continue;
		}

		res += num = (12 - clock[11]) / 3;
		clickButton(1, num);

		res += num = (12 - clock[8]) / 3;
		clickButton(4, num);

		res += num = (12 - clock[13]) / 3;
		clickButton(9, num);

		res += num = (12 - clock[6]) / 3;
		clickButton(3, num);

		res += num = (12 - clock[10]) / 3;
		clickButton(2, num);

		res += num = (12 - clock[9]) / 3;
		clickButton(9, num);

		res += num = (12 - clock[7]) / 3;
		clickButton(7, num);

		if (clock[4] != clock[5]) {
			printf("-1\n");
			continue;
		}

		res += num = (12 - clock[4]) / 3;
		clickButton(8, num);

		if (clock[0] != clock[2]) {
			printf("-1\n");
			continue;
		}

		res += num = (12 - clock[1]) / 3;
		clickButton(0, num);

		res += num = (12 - clock[3]) / 3;
		clickButton(6, num);

		if (clock[0] != clock[14]) {
			printf("-1\n");
			continue;
		}
		
		res += num = (12 - clock[0]) / 3;
		clickButton(5, num);

		printf("%d\n", res);
	}

	return 0;
}


/*

0 - 0, 3, 5 -> 035 -> 05 -> 05 -> 05 -> 5
1 - 0, 8 -> 08 -> 08 -> 08 -> 0
2 - 0, 5, 8 -> 058 -> 058 -> 058 -> 05 -> 5
3 - 1, 6, 8, 9 -> 68 -> 68 -> 68 -> 6
4 - 2, 3, 7, 8, 9 ->2378 -> 78 -> 8
5 - 3, 7, 8, 9 -> 378 -> 78 -> 8
6 - 3, 4 -> 3
7 - 1, 3, 4, 7 -> 37 -> 7
8 - 4
9 - 1, 9 -> 9
10 - 2, 4 -> 2
11 - 1
12 - 4
13 - 9
14 - 2, 5, 6, 7 -> 2567 -> 567 -> 56 -> 56 -> 5
15 - 2, 5, 6, 7 -> 2567 -> 567 -> 56 -> 56 -> 5

*/