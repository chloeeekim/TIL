// https://algospot.com/judge/problem/read/STRJOIN

#include <stdio.h>

#define MAX_ELEMENT 100

typedef struct {
	int key;
} element;

typedef struct {
	element heap[MAX_ELEMENT];
	int heap_size;
} HeapType;

HeapType heap;

void insert_min_heap(HeapType *h, element item) {
	int i;
	i = ++(h->heap_size);

	while ((i != 1) && (item.key < h->heap[i / 2].key)) {
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = item;
}

element delete_min_heap(HeapType *h) {
	int parent, child;
	element item, temp;

	item = h->heap[1];
	temp = h->heap[(h->heap_size)--];
	parent = 1;
	child = 2;

	while (child <= h->heap_size) {
		if ((child < h->heap_size) && (h->heap[child].key > h->heap[child + 1].key)) {
			child++;
		}
		if (temp.key <= h->heap[child].key) {
			break;
		}

		h->heap[parent] = h->heap[child];
		parent = child;
		child *= 2;
	}

	h->heap[parent] = temp;
	return item;
}

int main() {
	int testcase;
	int n, num;
	long long res;
	element item;
	element min1, min2;

	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &num);
			item.key = num;
			insert_min_heap(&heap, item);
		}

		res = 0;

		while (1) {
			min1 = delete_min_heap(&heap);
			min2 = delete_min_heap(&heap);
			item.key = min1.key + min2.key;
			insert_min_heap(&heap, item);

			res += item.key;

			if (heap.heap_size == 1) break;
		}
		
		item = delete_min_heap(&heap);
		printf("%d\n", res);
	}

	return 0;
}