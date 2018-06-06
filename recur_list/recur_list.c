#include <stdio.h>
#include <stdlib.h>


typedef struct linklist{
	int val;
	struct linklist *next_ptr;
}longlist;

longlist *first_ptr = NULL;



/* add to the head */
void add_list(int *value)
{   
    /* pointer to the next item in the list */
    longlist *new_item_ptr;
    
    new_item_ptr = malloc(sizeof(longlist));
    new_item_ptr->val = *value;	

    /*add to head (*new_item_ptr).next_ptr = first_ptr; */
    
    new_item_ptr->next_ptr = first_ptr;
    first_ptr = new_item_ptr;
}



longlist * swapPairs(longlist* head){
	if(head == NULL || head->next_ptr == NULL)
		return head;

	longlist* node1 = head;
	longlist* node2 = head->next_ptr;
	node1->next_ptr = swapPairs(node2->next_ptr);
	node2->next_ptr = head;

	return node2;
	}


/* define the function to print out the list */
void print_link(longlist *head)
{   
    if (head == NULL)
        return;
    
    print_link((*head).next_ptr);  
    printf("--");
    printf("%d\n",head->val);
}



int main(){
	int val1 = 1;
	int val2 = 2;
	int val3 = 3;
	int val4 = 4;

	add_list(&val1), add_list(&val2), add_list(&val3), add_list(&val4);

	printf("Check the list before we perform the swap pairs.\n");
	print_link(first_ptr);
	
	longlist headstar;

	printf("Check where the first pointer at:%d\n", first_ptr->val);
	headstar = *swapPairs(first_ptr);
	printf("We have our result: %d\n", headstar.val);
	
	print_link(&headstar);
	
	printf("Check where the first pointer after swap the pair:%d\n", first_ptr->val);
	return 0;
}
