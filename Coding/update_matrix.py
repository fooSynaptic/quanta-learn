#py3
import copy

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """     
        ops = [(1,0), (-1,0), (0,1), (0,-1)]
        
        r, c = len(matrix), len(matrix[0])
        
        res = copy.deepcopy(matrix)
        
        for i in range(r):
            for j in range(c):
                res[i][j] = None
        
        def _dfs(r_idx, c_idx, matrix):
            candidate = []
            for op in ops:
                move_row, move_col = r_idx+op[0], c_idx+op[1]
                if 0<=move_row<r and 0<=move_col<c:
                    if matrix[move_row][move_col] == 0:
                        res[r_idx][c_idx] = 1
                    else:
                        candidate.append(res[move_row][move_col])
            candidate = [x for x in candidate if x]
            if candidate:
                print(candidate)
                res[r_idx][c_idx] = min(candidate) + 1
            else:
                print("continue search")
                res[r_idx][c_idx] = _dfs(move_row, move_col, matrix) + 1
            
            
        for r_idx in range(r):
            for c_idx in range(c):
                if matrix[r_idx][c_idx] == 0:
                    res[r_idx][c_idx] = 0
                else:
                    _dfs(r_idx, c_idx, matrix)
                
        return res
    

                                
                                
ans = Solution()
print(ans.updateMatrix([[0, 0, 0],
[0, 1, 0],
[1, 1, 1]]))