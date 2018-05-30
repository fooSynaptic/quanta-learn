#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sort(int arr[10], int left, int right)
{
    if(left >= right)/*如果左边索引大于或者等于右边的索引就代表已经整理完成一个组了*/
    {
        return ;
    }
    int i = left;
    int j = right;
    int key = arr[left];
     
    while(i < j)                               /*控制在当组内寻找一遍*/
    {
        while(i < j && key <= arr[j])
        /*而寻找结束的条件就是，1，找到一个小于或者大于key的数（大于或小于取决于你想升
        序还是降序）2，没有符合条件1的，并且i与j的大小没有反转*/ 
        {
            j--;/*向前寻找*/
        }
         
        arr[i] = arr[j];
        /*找到一个这样的数后就把它赋给前面的被拿走的i的值（如果第一次循环且key是
        a[left]，那么就是给key）*/
         
        while(i < j && key >= arr[i])
        /*这是i在当组内向前寻找，同上，不过注意与key的大小关系停止循环和上面相fan因为排序思想是把数往两边扔，所以左右两边的数大小与key的关系相反*/
        {
            i++;
        }
         
        arr[j] = arr[i];
    }
     
    arr[i] = key;/*当在当组内找完一遍以后就把中间数key回归*/
    sort(arr, left, i - 1);/*最后用同样的方式对分出来的左边的小组进行同上的做法*/
    sort(arr, i + 1, right);/*用同样的方式对分出来的右边的小组进行同上的做法*/
                       /*当然最后可能会出现很多分左右，直到每一组的i = j 为止*/
}


void show(int num[],int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d\t",num[i]);
}




int main(){
	printf("===============================\n");
	/*int (*a)[10] = NULL;*/
	int arr[10] = {11,3,2,4,6,8,13,21,55,34};
	/*a = &arr;*/
	printf("%d\n", arr[0]);
        printf("%d\n", arr[1]);
	printf("%d\n", arr[2]);
	int left;
	int right;

	right = sizeof(arr)/sizeof(arr[0]) - 1;
	printf("The length of arr is: %d\n" , right+1);
	left = 0;

	sort( arr, left, right);
	show(arr,10);
	
	return 0;
}
