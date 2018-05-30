#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void maxthree(int arr[15], int low, int mid, int high){
	int sum;
	int left_sum;
	int right_sum;
	int max_left,max_right;
	int sum_count,compare_count;

	sum = 0;
	sum_count=0;
	compare_count=0;
	left_sum = -9999;
	right_sum = -9999;
	for(int i=mid;i>low;i--){
	sum = sum+arr[i];
	sum_count++;
	if(sum>left_sum){
		left_sum=sum;
		max_left=i;
		compare_count++;
	}
	}

	sum = 0;
	for(int j=mid+1;j<high;j++){
	sum = sum+arr[j];
	sum_count++;
	if(sum>right_sum){
		right_sum=sum;
		max_right=j;
		compare_count++;
		}
	}
	printf("%d\n%d\n%d\n",max_left,max_right,left_sum+right_sum);
	printf("The times of sum %d\n", sum_count);
	printf("The times of compare %d\n", compare_count);
}

int main(){
	int arr[15] = {-3,-25,20,-3,-16,-23,18,20,-1,12,-5,-22,15,-4,7};
	int low,mid,high;
	
	low = 0;
	mid = 7;
	high = 14;

	maxthree(arr,low,mid,high);
	return 0;
}
