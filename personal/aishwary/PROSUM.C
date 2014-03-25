#include<stdio.h>
void main()
{ int i,t=0,j,k,c=0,a[10],n;
    printf("enter t");
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
	printf("enter the array size");
	scanf("%d",&n);
	printf("enter the elements");
	for(j=0;j<n;j++)
	{
	  scanf("%d",&a[j]);
	}
	for(j=0;j<n;j++)
	{
	    for(k=j+1;k<n;k++)
	    {
	      if((a[j]*a[k])>(a[j]+a[k]))
		    c++;

	    }
	}
	printf("%d",c);
     }
}
