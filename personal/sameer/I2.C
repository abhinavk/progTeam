#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
	int i,j,k,a;
	long int b[10],sum;
	clrscr();
	puts("Enter no. of test case\n");
	scanf("%d",&a);
	for(i=0;i<a;i++)
	{
		scanf("%ld",&b[i]);
	}
	for(i=0;i<a;i++)
	{
		sum=0;
		while(pow(5,k+1)<=b[i])
			k++;
		for(j=1;j<=k;j++)
		{
			//c=pow(5,j);
			sum=sum+(b[i]/(pow(5,j)));
		}
		printf("%ld\n",sum);

	}
	getch();
}