# encoding = utf-8

class Solution:
    def findOrder(self, numCourses, prerequisites):
        def dfs(i, j, s):
            if not (0<=i<numCourses and 0<=j<numCourses) or grid[i][j] == 0:
                return s
            s.append(j)
            grid[i][j] = 0
            res = max(dfs(i+1, j, s[:]), dfs(i-1, j, s[:]), dfs(i, j+1, s[:]), dfs(i, j-1, s[:]), key = len)
            grid[i][j] = 1
            return res
        
        
        
        
        grid = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for c, pre in prerequisites:
            grid[pre][c] = 1
        
        for x in grid: print(x)
        maxPath = []
        for i in range(numCourses):
            for j in range(numCourses):
                if i == j: continue
                if grid[i][j] == 1:
                    path = dfs(i, j, [i])
                    print(i, path)
                    maxPath = max(maxPath, path, key=len)
                    
        if len(maxPath) == numCourses: return maxPath   
        return maxPath + [i for i in range(numCourses) if not i in maxPath]
        
        
                
                    
ans = Solution()

res = ans.findOrder(3, [[2,0],[2,1]])
print(res)