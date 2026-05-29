#include <stdio.h>

int my_PARTITION(int A[], int p, int r);

void quicksort(int A[], int p, int r)
{
	if (p < r) {
		int q = my_PARTITION(A, p, r);
		quicksort(A, p, q - 1);
		quicksort(A, q + 1, r);
	}
}

int my_PARTITION(int A[], int p, int r)
{
	int x = A[r];
	int i = p - 1;
	int tmp;

	for (int j = p; j < r; j++) {
		if (A[j] <= x) {
			i++;
			tmp = A[i];
			A[i] = A[j];
			A[j] = tmp;
		}
	}

	tmp = A[i + 1];
	A[i + 1] = A[r];
	A[r] = tmp;
	return i + 1;
}

int main(void)
{
	int arr[8] = {2, 8, 7, 1, 3, 5, 6, 4};

	quicksort(arr, 0, 7);

	for (int i = 0; i < 8; i++)
		printf("%d\n", arr[i]);
	return 0;
}
