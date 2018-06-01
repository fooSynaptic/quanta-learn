#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void quicksort(int A[10], int p, int r){
	if(p<r){
	int q;
	q = my_PARTITION(A, p, r);
	quicksort(A, p, q-1);
	quicksort(A, q+1, r);
	}
}

int my_PARTITION(int A[8], int p, int r){
	printf("We steped in partition!\n");
	int x = A[r-1];
	int i = p-1;
	int m;
	int s;
	
	printf("x: %d\n", x);

	for(int j=p; j<r-1; j++){
		printf("aj: %d\n",A[j]);
		if(A[j]<=x){
		i=i+1;
		m=A[j], A[j]=A[i], A[i]=m;
		}
	printf("i:\t%d,j:\t%d\n", i,j);
	for(int k=0;k<r;k++)
		printf("%d", A[k]);
	printf("\n");
	
	}
	s=A[r-1], A[r-1]=A[i+1], A[i+1]=s;
        printf("================Partition fullfilled!===============\n");
	return i+1;
}


int main(){
	int arr[8] = {2,8,7,1,3,5,6,4};

	printf("===================Array initialized !==================\n");

	quicksort(arr, 0, 8);

	for(int i=0;i<8;i++)
		printf("%d\n", arr[i]);
	return 0;
	}
