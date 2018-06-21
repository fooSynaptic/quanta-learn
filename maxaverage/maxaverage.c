#include <stdio.h>
#include <stdlib.h>



double findMaxAverage(int nums[5], int length, int k) {
    // Write your code here
    int s = 0;
    int f = s + k;
    double max = 0.;
    
    for(int i=0; i<f;i++)
        max = max + nums[i];
        
    double maxaver = max/k;
    printf("current max is %f average is %f\n", max, maxaver);
    for(int i=f; i<length; i++){
        if(nums[i]>maxaver && nums[i]>nums[s]){
            s++;
            max = max + nums[i]-nums[s-1];
            maxaver = max/k;
	    printf("s:%d\tf:%d\t;maxaver:%f\n",s,f,maxaver);
        }
    }
    return maxaver;
}





int main(void){
	//int nums[6] = {1,12,-5,-6,50,3};
	int nums[5] = {3,3,4,3,0};
	int l = *(&nums+1) - nums;
	printf("the len of array is %d\n" , l);
	int k = 3;
	//int *nump = &nums[0];

	printf("%f\n", findMaxAverage(nums,l,k));

}
