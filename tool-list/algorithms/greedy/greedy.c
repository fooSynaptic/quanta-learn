#include <stdio.h>

/* Greedy activity-selection: pick a maximal set of mutually compatible
 * activities given start times s[] and finish times f[] (sorted by finish). */

void greedy_select(int *s, int *f, int k, int n)
{
	int m = k + 1;

	while (m <= n && s[m] < f[k])
		m++;

	if (m <= n) {
		printf("{%d-%d}\n", s[m], f[m]);
		greedy_select(s, f, m, n);
	}
}

int main(void)
{
	int s[11] = {1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12};
	int f[11] = {4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16};
	int n = 10;

	greedy_select(s, f, 0, n);
	return 0;
}
