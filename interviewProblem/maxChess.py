# encoding=utf-8
# /usr/bin/python3

from random import randint


def maxChess(grid):
    r, c = len(grid), len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = 1

    for i in range(1, c):
        dp[0][i] = dp[0][i-1] + grid[0][i]
        
    for j in range(1, r):
        dp[j][0] = dp[j-1][0] + grid[j][0]

    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]


    return dp[r-1][c-1]





def testcase():
    r = 5; c = 10
    table = [[randint(0, 1) for _ in range(c)] for _ in range(r)]
    for x in table: print(x)
    ans = maxChess(table)

    print(ans)



testcase()