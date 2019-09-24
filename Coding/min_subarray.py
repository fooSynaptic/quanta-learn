#py3

class Solution1:
    def minSubArrayLen(self, s, nums):
        sums=[0 for _ in range(len(nums))]
        sums[0]=nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
        if s in sums: return sums.index(s)
        res=[]
        for i in range(len(nums)):
            l, r = i, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                print(l, r, mid, sums)
                if sums[mid]-sums[i]>=s:
                    res.append(mid-i-1)
                    print(res)
                    r = mid-1
                else:
                    l = mid+1
        
        if not res: return 0
        return min(res)+1
       


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums=[0]
        ss=0
        for i in nums:
            ss+=i
            sums.append(ss)
        ans=[]    
        for i in range(len(nums)):
            left=i
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                print(left, right, mid, sums)
                if sums[mid+1]-sums[i]>=s:
                    ans.append(mid-i)
                    right=mid-1
                else:
                    left=mid+1
        
            return min(ans)+1
        



ans = Solution1()
print(ans.minSubArrayLen(15,[1,2,3,4,5]))