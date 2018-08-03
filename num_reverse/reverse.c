#include "stdio.h"


int reverse(int x) {
 
    long reval = 0;
    for(;x;x/=10){
	printf("x:\t%d\n", x);
        reval = reval *10 + x%10;
    }
    x = reval;
    if(reval != x) return 0;
    
    return reval;
}

int main(){

	printf("final result of reverse is %d!\n", reverse(12345));
	return 0;
}
