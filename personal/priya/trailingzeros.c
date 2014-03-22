#include<stdio.h>
#include<conio.h>
int no_of_zeros(int n)
{int fact=1,i,c=0;
    for(i=1;i<=n;i++)
       {
           fact*=i;
        if(i%5==0)
            c++;
        if(i%25==0)
            c++;
}
return c;
}
int main()
{
int n,i,res,loop,num[40];
scanf("%d",&loop);
for(i=0;i<loop;i++)
    scanf("%d",&num[i]);
for(i=0;i<loop;i++)
{
res=no_of_zeros(num[i]);
printf("\n%d",res);
}
}
