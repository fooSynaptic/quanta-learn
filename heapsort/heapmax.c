#include <stdlib.h>
#include <stdio.h>
#include <string.h>


struct node{
	int *data;
	struct node *left;
	struct node *right;
};

static struct node *root = NULL;


/*=======================================*/
/* memory_error -- writes error and dies.*/
/*=======================================*/

void memory_error(void){
	fprintf(stderr, "Error: Out of memory\n");
	exit(8);
}

/*==========================================*/
/* save_string --saves a string on the heap.*/
/*==========================================*/
int *initvalue(int *value) 
{	int *new_value; 	/* where we are going to put string */ 
	new_value = malloc(sizeof(int));

	if (new_value == NULL) 
		memory_error();
	
	new_value = value;
	return new_value;
}

/*============================================*/
/* enter -- initialze value on the heap.      */
/*============================================*/

void enter(struct node **node, int *value)
{
	int result;	/* Cope of result. */
	int *initvalue(int *);	/* Save a value on the heap. */


	if((*node) == NULL){
	(*node) = malloc(sizeof(struct node));
	if ((*node) == NULL)
		memory_error();

	/* Initialize the new mode */
	(*node)->left = NULL;
	(*node)->right = NULL;
	(*node)->data = initvalue(value);
	return;
	}
	
	result = !((*node)->data == value);

	if(result == 0)
		return;

	if(result<0)
		enter(&(*node)->right, value);
	else
		enter(&(*node)->left, value);
	
}



void print_tree(struct node *top) {
	if (top == NULL)
		return; 	/* short tree */
	print_tree(top->left); 
	printf("%d\n", *(top->data)); 
	print_tree(top->right);
}


int main(){
	int input[10] = {1,7,5,3,2,4,9,8,0,6};
	int *input_ptr;
	for(int i=0; i<10; i++){
	input_ptr = &input[i];
	enter(&root, input_ptr);
	}

	print_tree(root);

}
