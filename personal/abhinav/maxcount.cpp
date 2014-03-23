// Codechef - Practice - Easy
// MAXCOUNT

#include <cstdio>

int main()
{
  unsigned int test_cases, array_s, inp,arr_i[100], arr[10001];
  unsigned int max_id;
  scanf("%u",&test_cases);
  while(test_cases--)
  {
    scanf("%u",&array_s);
    for(int i=0;i<10001;i++)
      arr[i]=0;
    for(int i=0;i<array_s;++i)
    {
      scanf("%u",&arr_i[i]);
      arr[arr_i[i]]++;
    }
    max_id=0;
    for(int i=1;i<array_s;i++)
      if(arr[arr_i[max_id]]<arr[arr_i[i]])
        max_id = i;
    printf("%u %u\n", arr_i[max_id], arr[arr_i[max_id]]);
  }
  return 0;
}