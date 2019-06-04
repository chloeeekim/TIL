// https://algospot.com/judge/problem/read/BOARDCOVER

#include <stdio.h>

int h, w;
char input[25][25];
int res;
int num_white;

void cover(int remain) {
	bool iscovered = false;

	if (remain == 0) {
		res++;
		return;
	}

	int x = -1, y = -1;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (input[i][j] == '.') {
				x = i;
				y = j;
				break;
			}
		}
		if (y != -1) break;
	}

	// └자 형태 (제일 왼쪽 & 위쪽 기준)
	if (x < h - 1 && y < w - 1) {
		if (input[x + 1][y] == '.' && input[x + 1][y + 1] == '.') {
			input[x][y] = input[x + 1][y] = input[x + 1][y + 1] = '#';
			iscovered = true;
			cover(remain - 3);
			input[x][y] = input[x + 1][y] = input[x + 1][y + 1] = '.';
		}
	}
	
	// ┌자 형태 (제일 왼쪽 & 위쪽 기준)
	if (x < h - 1 && y < w - 1) {
		if (input[x + 1][y] == '.' && input[x][y + 1] == '.') {
			input[x][y] = input[x + 1][y] = input[x][y + 1] = '#';
			iscovered = true;
			cover(remain - 3);
			input[x][y] = input[x + 1][y] = input[x][y + 1] = '.';
		}
	}
	
	// ┐자 형태 (제일 왼쪽 & 위쪽 기준)
	if (x < h - 1 && y < w - 1) {
		if (input[x][y + 1] == '.' && input[x + 1][y + 1] == '.') {
			input[x][y] = input[x][y + 1] = input[x + 1][y + 1] = '#';
			iscovered = true;
			cover(remain - 3);
			input[x][y] = input[x][y + 1] = input[x + 1][y + 1] = '.';
		}
	}

	// ┘자 형태 (제일 위쪽 기준)
	if (x < h - 1 && y > 0) {
		if (input[x + 1][y] == '.' && input[x + 1][y - 1] == '.') {
			input[x][y] = input[x + 1][y] = input[x + 1][y - 1] = '#';
			iscovered = true;
			cover(remain - 3);
			input[x][y] = input[x + 1][y] = input[x + 1][y - 1] = '.';
		}
	}
}

int main() {
	int testcase;
	char ch;
	int num_black;

	scanf("%d", &testcase);
	while (testcase--) {
		num_black = num_white = res = 0;
		scanf("%d %d", &h, &w);

		scanf("%c", &ch);
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				scanf("%c", &input[i][j]);
				if (input[i][j] == '.') num_white++;
				else num_black++;
			}
			scanf("%c", &ch);
		}

		if (num_black == w * h) {
			printf("1\n");
		}
		else {
			if ((num_white % 3) != 0) {
				printf("0\n");
			}
			else {
				cover(num_white);
				printf("%d\n", res);
			}
		}
	}

	return 0;
}