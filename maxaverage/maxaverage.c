#include <stdio.h>
#include <stdlib.h>


double findMaxAverage(int nums[6], int k) {
    // Write your code here
    int s = 0;
    int f = s + k;
    float max = 0.;
    
    for(int i=0; i<f;i++)
        max = max + nums[i];
        
    float maxaver = max/k;
    printf("current max is %f average is %f\n", max, maxaver);
    for(int i=f; i<6; i++){
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
	int nums[6] = {1,12,-5,-6,50,3};
	int k =4;

	printf("%f\n", findMaxAverage(nums,k));

}
