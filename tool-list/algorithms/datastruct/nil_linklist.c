#include <stdio.h>
#include <stdlib.h>

typedef struct two_sential {
	int data;
	struct two_sential *next;
} nli_two;

void nlienter(nli_two *header, int item)
{
	nli_two *node = (nli_two *)malloc(sizeof(nli_two));
	if (node == NULL)
		return;

	node->data = item;
	node->next = header->next;
	header->next = node;
}

int main(void)
{
	nli_two head = {0, NULL};
	nli_two *header = &head;

	nlienter(header, 10);
	nlienter(header, 20);

	for (nli_two *p = header->next; p != NULL; p = p->next)
		printf("%d\n", p->data);

	return 0;
}
