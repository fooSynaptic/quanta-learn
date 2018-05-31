#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/*=================================================*/
/* max-heapify -- sort algorithm to max the heap. */
/*===============================================*/

void max_heapify(int A[10], int i){
    	printf("Follow the rule!");
	printf("inner i is %d\n",i);
	if(i<1)
        return;

        int large;
        int l = 2*i;
        int r = 2*i+1;
        int s;

        if(l<10 && A[l-1]>A[i-1])
                large = l;
        else
                large = i;

        if(r<=10 && A[r-1]>A[large-1])
                large = r;

	printf("The current largest is %d\n", A[large]);
        if (large != i)
        {
        s = A[large-1], A[large-1] = A[i-1], A[i-1] = s;
        max_heapify(A,large);
                }
	else{
	printf("we can escape!\n");
	return;
	}
}


void buildmaxheap(int A[10])
{
	printf("Start build the array into a heap!\n");
	int length = 10;

	for(int i= 5;i >0; i--){
	printf("The very important index i is:%d\n",i);
	max_heapify(A,i);
	}

}

int main(){
	int A[10] = {4,1,3,2,16,9,10,14,8,7};
	
	/* initializing success for the array. */
	printf("INITIALIZING================\n");
	buildmaxheap(A);
	for(int i=0;i<10;i++)
		printf("%d\n", A[i]);
	return 0;
	}
