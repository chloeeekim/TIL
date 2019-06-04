// https://algospot.com/judge/problem/read/RATIO

#include <stdio.h>

typedef long long ll;

const ll MAX = 2000000000;

int get_ratio(ll win, ll total) {
	return (win * 100) / total;
}

ll get_win_num(ll win, ll total) {
	if (get_ratio(win, total) == get_ratio(win + MAX, total + MAX))
		return -1;

	ll low = 0, high = MAX;

	while (low + 1 < high) {
		ll mid = (low + high) / 2;
		if (get_ratio(win, total) == get_ratio(win + mid, total + mid)) {
			low = mid;
		}
		else {
			high = mid;
		}
	}

	return high;
}

int main() {
	int testcase;
	ll t_game, t_win;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%lld %lld", &t_game, &t_win);

		printf("%lld\n", get_win_num(t_win, t_game));
	}

	return 0;
}