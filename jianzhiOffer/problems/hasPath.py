# encoding = utf-8
# /usr/bin/python3
import pytest

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, grid, path):
        # write code here
        r, c = len(grid), len(grid[0])
        def dfs(i, j, p):
            if not (0<=i<r and 0<=j<c):
                return False
            if not grid[i][j] == p[0]:
                return False
            restore = grid[i][j]
            grid[i][j] = ' '
            
            ans = dfs(i+1, j, p[1:]) or dfs(i-1, j, p[1:]) or dfs(i, j+1, p[1:]) or dfs(i, j-1, p[1:])
            grid[i][j] = restore
            
            return ans

        head = 'b'

        for i in range(r):
            for j in range(c):
                if grid[i][j] == head:
                    if dfs(i, j, path): return True
                    
        return False






def test_answer():
    ans = Solution()
    res = ans.hasPath([['A']], "A")
    assert inc(res) == True


if __name__ == '__main__':
    pytest.main()