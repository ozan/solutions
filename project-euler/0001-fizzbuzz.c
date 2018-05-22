#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i,a[999],sum=0;
    for(i=1;i<=999;++i)
    a[i-1]=i;
    for(i=0;i<999;++i)
    {
        if (a[i]%3==0 || a[i]%5==0)
        sum=sum+a[i];
    }
    printf("sum= %d",sum);
	  return 0;
}
