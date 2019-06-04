// https://algospot.com/judge/problem/read/FENCE

/*
// 분할정복
#include <stdio.h>
#include <algorithm>
using namespace std;

int arr[20000];

int dnc(int start, int end) {
	if (start == end) return arr[start];
	int mid = (start + end) / 2;

	int res = max(dnc(start, mid), dnc(mid + 1, end));

	int low = mid, high = mid + 1;
	int height = min(arr[low], arr[high]);
	res = max(res, height * 2);
	
	while (start < low || high < end) {
		if (high < end && (low == start || arr[low - 1] < arr[high + 1])) {
			high++;
			height = min(height, arr[high]);
		}
		else {
			low--;
			height = min(height, arr[low]);
		}
		res = max(res, height * (high - low + 1));
	}

	return res;
}


int main() {
	int testcase;
	int n;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}
		printf("%d\n", dnc(0, n - 1));
	}

	return 0;
}
*/

// stack
#include <stdio.h>
#include <algorithm>
using namespace std;

int arr[20000];
int stack[20000];
int stack_top;

void push(int item) {
	stack[++stack_top] = item;
}

int pop() {
	return stack[stack_top--];
}

bool isEmpty() {
	if (stack_top == -1) return true;
	else return false;
}

int stackTop() {
	return stack[stack_top];
}

int main() {
	int testcase, n, temp, res, i;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);
		stack_top = -1;
		res = 0;
		
		push(-1);
		for (i = 0; i < n; i++) {
			scanf("%d", &arr[i]);

			while (!isEmpty() && arr[i] < arr[stackTop()]) {
				temp = pop();
				if (!isEmpty()) {
					res = max(res, arr[temp] * (i - stackTop() - 1));
				}
			}

			push(i);
		}

		while (!isEmpty()) {
			temp = pop();
			if (!isEmpty()) {
				res = max(res, arr[temp] * (i - stackTop() - 1));
			}
		}
		
		printf("%d\n", res);
	}

	return 0;
}