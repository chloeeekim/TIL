// https://algospot.com/judge/problem/read/FIXPAREN

#include <stdio.h>

int stack[100];
int stack_top;
char priority[5];

void push(int item) {
	stack[++stack_top] = item;
}

int pop() {
	return stack[stack_top--];
}

int getPriority(char ch) {
	for (int i = 0; i < 4; i++) {
		if (ch == priority[i]) return i;
	}
}

int main() {
	int testcase;
	char input[101];
	int pair;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%s %s", input, priority);

		for (int i = 0; ; i++) {
			if (input[i] == '\0') break;

			if (input[i] == '(' || input[i] == '{' || input[i] == '<' || input[i] == '[') {
				push(i);
			}
			else if (input[i] == ')') {
				pair = pop();
				int pri1 = getPriority(input[pair]), pri2 = getPriority('(');
				if (pri1 < pri2) {
					input[i] = input[pair] + 2;
				}
				else if (pri1 > pri2) {
					input[pair] = '(';
				}
			}
			else {
				pair = pop();
				int pri1 = getPriority(input[pair]), pri2 = getPriority(input[i] - 2);
				if (pri1 < pri2) {
					if (input[pair] == '(') input[i] = ')';
					else input[i] = input[pair] + 2;
				}
				else if (pri1 > pri2) {
					input[pair] = input[i] - 2;
				}
			}
		}

		printf("%s\n", input);
	}

	return 0;
}