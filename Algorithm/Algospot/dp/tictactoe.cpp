// https://algospot.com/judge/problem/read/TICTACTOE

#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int cache[20000];
char game[3][3];
char start = 'x';

bool is_finished(char turn) {
	for (int i = 0; i < 3; i++) {
		// 가로열
		if (game[i][0] == turn && game[i][1] == turn && game[i][2] == turn) {
			return true;
		}
		if (game[0][i] == turn && game[1][i] == turn && game[2][i] == turn) {
			return true;
		}		
	}
	
	// 대각선
	if (game[0][0] == turn && game[1][1] == turn && game[2][2] == turn) {
		return true;
	}
	if (game[0][2] == turn && game[1][1] == turn && game[2][0] == turn) {
		return true;
	}

	return false;
}

int get_index() {
	int res = 0;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			res *= 3;
			if (game[i][j] == 'o') ++res;
			else if (game[i][j] == 'x') res += 2;
		} 
	} 
	
	return res;
}

int play(char turn) {
	// 이전 턴에 상대방이 한 줄 생성
	if (is_finished('x' + 'o' - turn)) return -1;

	int& res = cache[get_index()];

	if (res != -2) return res;
	int m_num = 2;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (game[i][j] == '.') {
				game[i][j] = turn;
				m_num = min(m_num, play('x' + 'o' - turn));
				game[i][j] = '.';
			}
		}
	}

	if (m_num == 2 || m_num == 0) return res = 0;
	return res = -m_num;
}

int main() {
	int testcase;
	int dot_num;

	for (int i = 0; i < 20000; i++) {
		cache[i] = -2;
	}
	
	cin >> testcase;

	while (testcase--) {
		dot_num = 0;

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				cin >> game[i][j];
				if (game[i][j] == '.') dot_num++;
			}
		}

		if (dot_num == 9) {
			cout << "TIE" << endl;
			continue;
		}
		else {
			if (dot_num % 2 == 1) start = 'x';
			else start = 'o';

			int ans = play(start);

			if (ans == 1) {
				cout << start << endl;
			}
			else if (ans == -1) {
				cout << (char)('o' + 'x' - start) << endl;
			}
			else if (ans == 0) {
				cout << "TIE" << endl;
			}
		}
	}

	return 0;
}