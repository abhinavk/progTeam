#include<stdio.h>
#include<math.h>
void main()
{
    int i,j,k,t=0;
    long int b[10],sum;
    scanf("%d",&t);
    for(i=0;i<a;i++)
    {
        scanf("%ld",&b[i]);
    }
    for(i=0;i<a;i++)
    {
        s=0;
        while(pow(5,k+1)<=b[i])
            k++;
        for(j=1;j<=k;j++)
        {

            s=s+(b[i]/(pow(5,j)));
        }
       printf("%ld\n",s);

    }

}
