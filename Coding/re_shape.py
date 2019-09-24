#py3
import numpy as np


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        d1, d2 = len(nums), len(nums[0])
        
        if not r*c == d1*d2: return nums
        
        res = []
        for row in nums: res.extend(row)
        
        return [[res[(i+1)*(j+1)-1] for j in range(c)] for i in range(r)]
                

ans = Solution()
mat = np.random.rand(1, 40)


print(np.array(ans.matrixReshape(mat, 2, 20)).shape)