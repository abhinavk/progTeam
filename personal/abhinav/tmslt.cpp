// Codechef Practice Problems - Easy
// Team Split - TMSLT

#include <cstdio>
bool p[1000010],tmp;
int t;
long long i,n,a,b,c,d,rd;
int main()
{
  scanf("%d",&t);
  while(t--)
  {
    tmp=0;
    rd=0;
    scanf("%lld%lld%lld%lld%lld",&n,&a,&b,&c,&d);
    p[d]=1;
    for(i=1;i<n;i++)
    {
      d=((a*d+b)*d+c)%1000000;
      p[d]=!p[d];
    }
    for(i=999999;i>-1;i--)
      if(p[i])
      {
        if(tmp)
          rd-=i;
        else
          rd+=i;
        tmp = !tmp;
        p[i]=0;
      }
    printf("%lld\n",rd);
  }
  return 0;
}
