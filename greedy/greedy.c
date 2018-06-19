#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int start = 0;

typedef struct mergearray{
	int *a;
}marray, *newmarray;

int k = 0;

// this program realize the greedy algorithm implement in the activities allcation

int recursive(int *s, int *f, int k, int n){
	
	int m = k+1;
	while(m<=n && *(s+m)<*(f+k)){
		m++;
	}
	if(m<=n){
		printf("{%d-%d}\n", *(s+m), *(f+m));
		//printf(recursive(*s,*f,m,n));
	}
	else{
		printf("null set\n");
	}
	return recursive(*s,*f,m,n);
}




// we need to define a function to merge element into a set(maybe array)
// obviously the function we defined below dont satisfy function-recursive for it need merge of set instead
// merge inter into an array.

void merge_set(int *all, int a)
{

	int *newval;	

	
	int len = 0;
	for(int i=0;i<10;i++){
	  if((all+i) != NULL){
		len++;  
	} else{
		break;
	}
	}	

	printf("length of candidata array is %d\n", len);
	newval = all+len;
	newval = &a;
	*(all+len) = a;
	printf(" value %d has been assined into the array with value:%d\n", *(newval),*(all+len));	

	for(int i=0;i<12;i++)
		printf("%d\t",*(all+i));
	printf("\n");

}


int main(){
	
	// a simple test for the merge-set

	int s[12] = {1,2,3,4,5,6,7,8,9,10};
	int a = 11;
	int *sp = &s[0];
	

	merge_set(sp, a);
	for(int i=0;i<12;i++)
                printf("%d\t",*(sp+i));
        printf("\n");

	// we can still give a trial for the greedy-allocater
	
	int h[11] = {1,3,0,5,3,5,6,8,8,2,12};
	int f[11] = {4,5,6,7,9,9,10,11,12,14,16};
	int n = 11;
	int *hp = &h[0];	
	int *fp = &f[0];

	recursive(hp, fp, k, n);

	return 1;

}
