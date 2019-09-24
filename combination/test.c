#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define maxn 10001
long long dp[maxn];
int main(void)
{
    int i,j,num[] = {5, 10, 20, 50, 100};
    for(i = 0; i < maxn; ++i)
        dp[i] = 1;
    for(i = 0; i < 5; ++i)
        for(j = num[i]; j < maxn; ++j)
            dp[j] += dp[j - num[i]];
    printf("%lld", dp[maxn - 1]);
    return 0;
}

