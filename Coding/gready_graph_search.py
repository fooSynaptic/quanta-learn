# py3
import time


class greedy_Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        moves = {'right': (0,1),'left': (0,-1), 'upside': (-1, 0), 'downside': (1, 0)}
        
        # gready search
        s_idx = [len(grid)-1, len(grid[0])-1]
        res = []
        res.append(s_idx)
        
        h_dim, v_dim = len(grid), len(grid[0])
        
        while s_idx != [0, 0]:
            print(s_idx)
            tmp_val = []
            for move in moves:
                tmp_idx = [s_idx[0] + moves[move][0], s_idx[1] + moves[move][1]]
                if not tmp_idx in res and -1<tmp_idx[0]<h_dim and -1<tmp_idx[1]<v_dim:
                    print("tmp_idx:", tmp_idx)
                    print(move)
                    tmp_val.append((grid[tmp_idx[0]][tmp_idx[1]], move))

                
            tmp_val = sorted(tmp_val, key = lambda x:x[0])
            decision_move = tmp_val[0][1]
            print('decision move:', decision_move)
            # step forward
            s_idx = [s_idx[0] + moves[decision_move][0], s_idx[1] + moves[decision_move][1]]
            #store value
            res.append(s_idx)
            #time.sleep(5)
        
        val = 0
        for x in res:
            val += grid[x[0]][x[1]]
        return val


class dp_Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i==0 and j != 0:
                    grid[i][j] = grid[i][j]+grid[i][j-1]
                elif j == 0 and i != 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif i == j and i==0:
                    grid[i][j] = grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        print(grid)
        return grid[m - 1][n - 1]




ans = dp_Solution()
print(ans.minPathSum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]))      
        