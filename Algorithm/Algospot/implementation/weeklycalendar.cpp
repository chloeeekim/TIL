// https://algospot.com/judge/problem/read/WEEKLYCALENDAR

#include <stdio.h>
#include <string.h>

char week7[7][10] = { {"Sunday"}, {"Monday"}, {"Tuesday"}, {"Wednesday"}, {"Thursday"}, {"Friday"}, {"Saturday"} };
int daysofmonth[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

int main() {
	int testcase;
	int month, day;
	char week[10];
	int val;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d %d %s", &month, &day, week);

		month--;
		for (int i = 0; i < 7; i++) {
			if (strcmp(week7[i], week) == 0) {
				day -= (i + 1);
				if (day < 1) {
					month -= 1;
					if (month < 0) month = 11;
					day += daysofmonth[month];
				}
				break;
			}
		}

		for (int i = 0; i < 7; i++) {
			if (++day > daysofmonth[month]) {
				day = 1;
			}
			printf("%d ", day);
		}
		printf("\n");
	}

	return 0;
}