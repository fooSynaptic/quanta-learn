//this program use the thought of composite mathmatic to solove problem about upstairs
#include <iostream>

using namespace std;

int jiecheng(int n){
	if(n==0||n==1){
		   return 1;
	   }
	   else{
		   int temp=jiecheng(n-1);
		   return temp*n;
	   }
}
   
int long GetStepNum2(int n)  {  
	long count=0;
	if(n==0){
    		return 0;
    	}
        for(int i=0;i<=n/2;i++){
        	int temp=jiecheng(n-i);
        	temp=temp/(jiecheng(i));
        	temp=temp/(jiecheng(n-2*i));
        	count+=temp;
        }
        return count;
   }  

int main() {
	cout << GetStepNum2(5) << endl;
	
}
