#include <stdio.h>

/* Build a max-heap from an array using 1-based indexing:
 * node i (1..n) has children 2*i and 2*i+1, stored at A[i-1]. */

void max_heapify(int A[], int n, int i)
{
	int largest = i;
	int l = 2 * i;
	int r = 2 * i + 1;
	int s;

	if (l <= n && A[l - 1] > A[largest - 1])
		largest = l;
	if (r <= n && A[r - 1] > A[largest - 1])
		largest = r;

	if (largest != i) {
		s = A[largest - 1];
		A[largest - 1] = A[i - 1];
		A[i - 1] = s;
		max_heapify(A, n, largest);
	}
}

void build_max_heap(int A[], int n)
{
	for (int i = n / 2; i > 0; i--)
		max_heapify(A, n, i);
}

int main(void)
{
	int A[10] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
	int n = 10;

	build_max_heap(A, n);
	for (int i = 0; i < n; i++)
		printf("%d\n", A[i]);
	return 0;
}
