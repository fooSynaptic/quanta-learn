#include <stdio.h>
#include <stdlib.h>

typedef struct heaptree{
	int data;
	struct heaptree *left;
	struct heaptree *right;
	}heap, *newheap;


/*=======================================*/
/* First we need to initialize the tree! */
/*=======================================*/


newheap createTreeNode(int value){
	newheap n = (newheap)malloc(sizeof(heap));
	n->data = value;
	n->left = NULL;
	n->right = NULL;
	return n;
	}

/*=======================================*/
/* Function to print the tree          ! */
/*=======================================*/

void treeTravel(newheap p)  
{  
    if (NULL == p)  
    {  
        return;  
    }  
    treeTravel(p->left);  
    printf("%d  ", p->data);  
    treeTravel(p->right);  
  
}  




int main(){
	
	newheap root = NULL;
	newheap p1 = NULL, p2 = NULL, p3 = NULL, p4 = NULL, p5 = NULL,p6 = NULL;

	p1 = createTreeNode(7);
	p2 = createTreeNode(1);
	p3 = createTreeNode(9);
	p4 = createTreeNode(5);
	p5 = createTreeNode(3);
	p6 = createTreeNode(2);


	p1->left = p2, p1->right = p3;
	p2->right = p4;
	p3->left = p5, p3->right = p6;

	root = p1;
	treeTravel(root);

	getchar();
}
