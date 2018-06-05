#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct btree{
	int val;
	struct btree *left;
	struct btree *right;
	}bptree, *tree;

/*=======================================*/
/* First we need to initialize the tree! */
/*=======================================*/


tree createTreeNode(int value){
        tree n = (tree)malloc(sizeof(bptree));
        n->val = value;
        n->left = NULL;
        n->right = NULL;
        return n;
        }


void exchangeBTree(bptree *root)
{
	bptree *t;
	if(root)
	{
	t = root->right;
	root->right = root->left;
	root->left = t;

	exchangeBTree(root->left);
	exchangeBTree(root->right);

		}
}

/*=========================================*/
/* Define the function to travel the tree */
/*=======================================*/
void inorder_tree_travel(bptree *root)
{
	if(root == NULL)
	return;
	
	if(root){
	inorder_tree_travel(root->left);
	printf("val of node %d\n", root->val);
	inorder_tree_travel(root->right);
	}
}



/* main function */

int main(){

        tree root = NULL;
        tree p1 = NULL, p2 = NULL, p3 = NULL, p4 = NULL, p5 = NULL,p6 = NULL;

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
	
	printf("Initial of the tree:\n");
	inorder_tree_travel(root);

	printf("After the reverse:\n");
	exchangeBTree(root);
	inorder_tree_travel(root);

}

