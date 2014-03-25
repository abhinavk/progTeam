#include<stdio.h>
void main()
{ int t=0,n=0,i,j,k,v=0,b=0,c=0,a[10];clrscr();
    printf("enter t");
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
	printf("enter array size");
	scanf("%d",&n);
	printf("enter elements");
	for(j=0;j<n;j++)
	{  scanf("%d",&a[j]);
	}
	for(j=0;j<n;j++)
	{   c=0;
	    for(k=j;k<n;k++)
	    {
		if(a[j]==a[k])
		    c++;
	    }
	    if(c>b)
	    { b=c;
	      v=a[j];
	    }
	    if(c==b)
	    {
		if(a[j]<v)
		{ v=a[j];
		    b=c;
		}
	    }
	}
	printf("v=%d\nc=%d",v,b);

    }
}
