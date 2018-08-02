//#include "math.h"
#include "stdio.h"
#define max(a,b)(a>b?a:b)
#define min(a,b)(a>b?b:a)

int maxArea(int* height, int heightSize) {
    int* begin = height; 
    int* end = height + heightSize - 1;
    int maxarea = 0, s = heightSize - 1;
    while(begin < end){
        maxarea = max(maxarea, min(*(begin), *(end))*(s-1));
        printf("left:%d\tright:%d\tmaxarea: %d\n", *begin, *end, maxarea);
	if (*begin < *end)
            begin++;
        else
            end--;
    }
    return maxarea;
}



int main() {
	int nums[9] = {1,8,6,2,5,4,8,3,7};
	int* h = &nums[0];

	printf("%d\n", maxArea(h, 8));
	return 1;

}

