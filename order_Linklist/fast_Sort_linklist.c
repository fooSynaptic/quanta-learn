#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Node 
{
	int key;
	Node* next;
	Node(int nKey, Node* pNext)
		: key(nKey)
		, next(pNext)
	{}
};
 
 
Node* GetPartion(Node* pBegin, Node* pEnd)
{
	int key = pBegin->key;
	Node* p = pBegin;
	Node* q = p->next;
 
	while(q != pEnd)
	{
		if(q->key < key)
		{
			p = p->next;
			swap(p->key,q->key);
		}
 
		q = q->next;
	}
	swap(p->key,pBegin->key);
	return p;
}
 
void QuickSort(Node* pBeign, Node* pEnd)
{
	if(pBeign != pEnd)
	{
		Node* partion = GetPartion(pBeign,pEnd);
		QuickSort(pBeign,partion);
		QuickSort(partion->next,pEnd);
	}
}


int main()
{
	int arr[5] = {3,1,5,2,4};
	Node* head = Node(3);
	Node* tmp = head;
	for(i=1;i<5;i++){
		tmp.next = Node(arr[i])
		tmp = tmp.next

	};
	
	Node* pend = head;

	while(pend->next)
		pend = pend.next;


	Node* pprint = head;
	QuickSort(pprint, pend);

	for(i=0;i<5;i++){
		printf('%s\n', head.key);
		head = head.next;
	};

return 0;
}
