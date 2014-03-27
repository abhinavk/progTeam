// Codechef Practice - Easy
// Predictopus - PREDICT

#include <cstdio>

int main()
{
  long int t;
  double pa,a=10000.0,res;
  scanf("%ld",&t);
  while(t--)
  {
    scanf("%lf",&pa);
    if(pa>0.5)
      res = a+a*(1-pa)*(2*pa-1);
    else
      res = a+a*pa*(1-2*pa);
    printf("%lf\n",res);
  }
  return 0;
}
