#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void merge(int arr[20],int p,int q,int r){
	int n1 = q-p+1;
	int n2 = r-q;
	int L[n1+2];
	int R[n2+2];

	for(int i=0;i<n1+1;i++){
	L[i] = arr[p+i-1];
	}

	for(int j=0;j<n2+1;j++){
        L[j] = arr[p+j-1];
        }

	L[n1+1] = 9999999;
	R[n2+1] = 9999999;
	int i = 1;
	int j = 1;

	for(int k=p;k<r+1;k++){
		if(L[i]<=R[j]){
		arr[k] = L[i];
		i++;
		}else{
		arr[k] = R[j];
		j++;
		
		}

		}
}


void merge_sort(int arr[20], int p, int r){
	if(p<r){
		float q = (p+r)/2;
		int q_int = floor(q); 
		merge_sort(arr, p, q_int);
		merge_sort(arr, q_int+1, r);
		merge(arr,p,q_int,r);
		}


}

int main(){
	int arr[20] = {2,3,4,5,6,1,2,4,7,8,9,11,13,19,15,16,17,18,1,0};
	int p=0;
	int r=20;

	merge_sort(arr,p,r);

	for(int i=0; i<r; i++){
	printf("%d\t",arr[i]);	

	}
	printf("\n");
	return 0;
	}
