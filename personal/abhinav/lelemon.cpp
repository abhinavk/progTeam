// Codechef Practice - Easy
// Little Elephant and Lemonade - LELEMON

#include <cstdio>
#include <vector>
#include <algorithm>

long n_lemonades(int,int);
int p[10001],c[101];

int main()
{
  int testcase,m,n;
  scanf("%d",&testcase);
  while(testcase--)
  {
    scanf("%d%d",&n,&m);
    printf("%ld\n",n_lemonades(m,n));
  }
  return 0;
}

long n_lemonades(int m,int n)
{
  int i,j,tmp;
  long lemonades=0;
  for(i=0;i<m;i++)
    scanf("%d",&p[i]);
  std::vector<long> v[n];
  for(i=0;i<n;i++)
  {
    scanf("%d",&c[i]);
    for(j=0;j<c[i];j++)
    {
      scanf("%d",&tmp);
      v[i].push_back(tmp);
    }
    std::sort(v[i].begin(),v[i].end());
  }
  for(i=0;i<m;i++)
  {
    if(!v[p[i]].empty())
    {
      lemonades += v[p[i]].back();
      v[p[i]].pop_back();
    }
  }
  return lemonades;
}
