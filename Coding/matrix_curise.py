class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        r, c = len(matrix), len(matrix[0])
        res = []
        upright = True
        idx = [0, 0]
        while idx[0] < r and idx[1] < c:
            #print(idx, upright)
            res.append(matrix[idx[0]][idx[1]])
            if upright:
                incre = [-1,1]
            else:
                incre = [1, -1]

            if idx[0] + incre[0] < 0:
                upright = not upright
                incre[0] = 0
            elif idx[1] + incre[1] < 0:
                upright = not upright
                incre[1] = 0
            if idx[1] + incre[1] > c-1:
                incre = [1, 0]
                if upright:
                    upright = not upright
            elif idx[0] + incre[0] > r-1:
                incre = [0, 1]
                if not upright:
                    upright = not upright
            idx = [idx[0]+incre[0], idx[1]+ incre[1]]
             
        return res
            
ans = Solution()
matrix = [[1,2,3,4,6,8,9],[5,6,7,8,6,8,9],[9,10,11,12,6,8,9],[13,14,15,16,6,8,9]]
print(ans.findDiagonalOrder(matrix))

for x in matrix:
    print(x)