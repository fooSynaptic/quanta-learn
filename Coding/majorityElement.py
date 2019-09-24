#py3


class Solution:
    #vote algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        threshould = len(nums)//3
        
        a, b = nums[0], nums[0]
        cnt_a, cnt_b = 0, 0
        
        for num in nums:
            if cnt_a == 0:
                a = num
            elif cnt_b == 0:
                b = num
                
            cnt_a += (1 if num == a else -1)
            cnt_b += (1 if num == b else -1)
        
        if a==b:
            return a
        else:
            return [x for x in [a,b] if x]