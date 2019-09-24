import time

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #回溯法
        res = []
        
        def restore(nums, s):
            if not s in res and len(s)>1:
                res.append(s)

            for i in range(len(nums)):
                if s and nums[i] < s[-1]:
                    return
                else:
                    restore(nums[i+1:], s + [nums[i]])
        
        restore(nums, [])
        
        return res
                

ans = Solution()
print(ans.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))