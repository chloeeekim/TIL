// https://algospot.com/judge/problem/read/TRAVERSAL

#include <stdio.h>

typedef struct {
	int low;
	int high;
} index;

int preorder[100];
int inorder[100];
int postorder[100];

int n;

void traversal(index pre, index in, index post, int len) {
	if (pre.low > pre.high || in.low > in.high || post.low > post.high) return;
	if (pre.low < 0 || in.low < 0 || post.low < 0) return;
	if (pre.high > n || in.high > n || post.high > n) return;

	if (len == 0) return;
	if (len == 1) {
		postorder[post.low] = preorder[pre.low];
		return;
	}

	int root = preorder[pre.low];
	int pos = 0;

	for (int i = in.low; i <= in.high; i++) {
		if (inorder[i] == root) {
			pos = i;
			break;
		}
	}

	postorder[post.high] = root;

	int next_len = pos - in.low;
	if (next_len > 0) {
		traversal({ pre.low + 1, pre.low + next_len }, { in.low, pos - 1 }, { post.low, post.low + next_len - 1 }, next_len);
	}

	next_len = in.high - pos;
	if (next_len > 0) {
		traversal({ pre.high - next_len + 1, pre.high }, { pos + 1, in.high }, { post.high - next_len, post.high - 1 }, next_len);
	}
}

int main() {
	int testcase;
	
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf("%d", &preorder[i]);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &inorder[i]);
		}

		index idx;
		idx.low = 0;
		idx.high = n - 1;

		traversal(idx, idx, idx, n);

		for (int i = 0; i < n; i++) {
			printf("%d ", postorder[i]);
		}
		printf("\n");
	}

	return 0;
}