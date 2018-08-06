#include "stdio.h"
#include <stdbool.h>


char line[100];
int value;

bool isPalindrome(int x) {
    if(x<0) {return false;}
    int rev = 0;
    int check = x;
    for(;x;x/=10) {rev = rev*10 + x%10;}
    printf("rev: %d\n", rev);
    
    if(rev - check == 0){
	printf("bingo\n"); 
        return true;
	}
    else
        return false;
}

int main(){
	printf("Enter arbitry number: "); 
	fgets(line, sizeof(line), stdin); 
	sscanf(line,"%d",  &value);
	printf("check about the value from input %d\n", value);
	
	if (isPalindrome(value) == true)
		printf("it is a palindrome value\n");
	else 
		printf("it is not\n");
	
	return 0;
	}
