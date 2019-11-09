# encoding = utf-8
# /usr/bin/python3
import time
global mat

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, k, r, c):
        # write code here
        self.cnt = 0
        if r == 0 or c == 0: return 0

        def p_sum(x, y):
            res = 0
            while x:
                res += x%10
                x = x//10
                
            while y:
                res += y%10
                y = y//10
            return res <= k


        mat = [[1 for _ in range(c)] for _ in range(r)]

        def dfs(i, j):
            if not (0<=i<r and 0<=j<c): return 0
            if mat[i][j] == 0: return 0
            if not p_sum(i, j): return 0
            assert mat[i][j] == 1
            s = 1
            mat[i][j] = 0
            s += dfs(i+1, j)
            s += dfs(i-1, j)
            s += dfs(i, j-1)
            s += dfs(i, j+1)
            #mat[i][j] = 1
            return s
 
        return dfs(0, 0)
       

        
def testcase():
    ans = Solution()
    res = ans.movingCount(18, 100, 100)

    print(res)


testcase()