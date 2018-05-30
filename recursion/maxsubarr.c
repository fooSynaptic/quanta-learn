#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	int arr[16] = {13,-3,-25,20,-3,-16,-23,18,20,-1,12,-5,-22,15,-4,7}; 
	static int a[16]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	int length;
	int result[250];

	length = sizeof(arr)/sizeof(arr[0]);
	int index1;
	int index2;
	int idx2;
	int sumi;
	int resulti=0;
	int sum;
	int sum_count=0;
	int compare_count=0;	
	
	for(index1 = 0; index1<16; index1++){
	  int b[16]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	  for(int i=index1; i<16; i++)
	  	b[i] = b[i+1];
	  b[15] = 0;

		for(index2=0; index2<15; index2++)
			sum = 0;
			{
			idx2 = b[index2];
			if(index1 < idx2)
			{	for(sumi = index1;sumi<idx2+1;sumi++)
					sum = sum + arr[sumi];
					sum_count++;
			}
			else
			{
				for(sumi=idx2;sumi<index1+1;sumi++)
					sum = sum + arr[sumi];
					sum_count++;
			}	
		result[resulti] = sum;
		resulti++;	
		}
}
	printf("The times of sum is %d\n", sum_count);
	printf("The times of compare is %d\n", compare_count);
	length = sizeof(result)/sizeof(result[0]);
	printf("First of the result is %d\n", result[0]);
	printf("Length of result: %d\n", length);
	printf("End of the result is %d\n", result[239]);
	sum=result[0];
	for(int i=1; i<240; i++){
		printf("%d\n",result[i]);
		if(sum<result[i]||sum == result[i])
			printf("%d\n",result[i]),sum = result[i];
	}
	printf("The max of the result of sum is %d\n", sum);
	return 0;
}
