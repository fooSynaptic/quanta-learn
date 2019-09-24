#py3
from pprint import pprint

def pprint(l):
    for x in l:
        print(x)


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return matrix

        
ans = Solution()

inp = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
pprint(inp)
print(ans.rotate(inp))
pprint(inp)