// https://algospot.com/judge/problem/read/BRACKETS2

#include <stdio.h>

char stack[10000];
int stack_top;

void push(char item) {
	stack[++stack_top] = item;
}

char pop() {
	return stack[stack_top--];
}

bool isEmpty() {
	if (stack_top == -1) return true;
	else return false;
}

int main() {
	int testcase;
	char arr[10001];
	char ch;
	bool ispaired;

	scanf("%d", &testcase);
	while (testcase--) {
		stack_top = -1;
		ispaired = true;
		scanf("%s", arr);

		for (int i = 0; ; i++) {
			if (arr[i] == '\0') break;

			if (arr[i] == '(' || arr[i] == '{' || arr[i] == '[') push(arr[i]);
			else {
				if (isEmpty()) {
					ispaired = false;
					arr[i + 1] = '\0';
					break;
				}
				else {
					ch = pop();
					if (arr[i] == ')' && ch == '(') continue;
					else if (arr[i] == '}' && ch == '{') continue;
					else if (arr[i] == ']' && ch == '[') continue;
					else {
						ispaired = false;
						arr[i + 1] = '\0';
						break;
					}
				}
			}			
		}

		if (!isEmpty()) ispaired = false;

		if (ispaired) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}