
#include<stdio.h>
#include<math.h>
void main()
{
  int n,i;
  double d;
  scanf("%d",&n);
  d=0;
  for(i=1;i<=n;i++)
	  d+=log10(i);
  printf("%d\n",(int)d+1);
}

