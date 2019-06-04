// https://algospot.com/judge/problem/read/LECTURE

#include <stdio.h>

#define MAX_ELEMENT 500

typedef struct {
	int key;
	char data[3];
} element;

typedef struct {
	element heap[MAX_ELEMENT];
	int heap_size;
} heapType;

heapType heap;

void insert_min_heap(heapType *h, element item) {
	int i;
	i = ++(h->heap_size);

	while ((i != 1) && (item.key < h->heap[i / 2].key)) {
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = item;
}

element delete_min_heap(heapType *h) {
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
	char a, b;
	element item;

	scanf("%d", &testcase);
	scanf("%c", &a);
	while (testcase--) {
		while (1) {
			scanf("%c", &a);
			if (a == '\n') break;
			scanf("%c", &b);

			item.key = a * 1000 + b;
			item.data[0] = a;
			item.data[1] = b;
			item.data[2] = '\0';

			insert_min_heap(&heap, item);
		}

		while (1) {
			if (heap.heap_size == 0) break;
			item = delete_min_heap(&heap);
			printf("%s", item.data);
		}
		printf("\n");
	}	

	return 0;
}