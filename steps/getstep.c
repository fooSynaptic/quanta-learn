//this program compute the ways to upstair n 

#include "stdio.h"
#include "stdlib.h"

int long getstepnum(int n) {
	if (n<1) return 0;
	else{
	if(n==1) return 1;
	else{
	if(n==2) return 2;
	else return getstepnum(n-1) + getstepnum(n-2);
	}
	}
}

int main (){
	int n = 5;
	printf("%ld\n", getstepnum(n));

	return 1;
}
