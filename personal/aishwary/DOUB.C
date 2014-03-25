#include<stdio.h>
#include<conio.h>
void main()
{ int t=0,n=0,i=0;clrscr();
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    scanf("\n%d",&n);
    if(n%2==0)
      printf("\n%d\n",n);
    else
     printf("\n%d\n",(n-1));
  }
  getch();
}
