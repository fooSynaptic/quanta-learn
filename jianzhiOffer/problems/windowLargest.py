# encoding = utf-8
# /usr/bin/python3

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, nums, size):
        # write code here
        def insert(s, left, right, val):
            if len(s) == 0: 
                s.append(val)
                return
            if val <= s[left]:
                s.insert(0, val)
                return
            elif val >= s[right]:
                s.append(val)
                return
            
            while left <= right:
                mid = (left+right)//2
                if s[mid] >= val:
                    right = mid-1
                else:
                    left = mid+1
            
            s.insert(left, val)


        ans = []
        n = len(nums)

        heap = []
        for i in range(n):
            insert(heap, 0, len(heap)-1, nums[i])
            if len(heap) == size:
                ans.append(heap[-1])
                heap.remove(nums[i-size+1])

        
            
        return ans
                    
            


def testcase():
    ans = Solution()
    nums = [2,3,4,2,6,2,5,1]
    res = ans.maxInWindows(nums, 3)
    print(res)


testcase()