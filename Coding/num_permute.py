import time


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = time.time()
        nums = [str(x) for x in range(1, n+1)]
        return ''.join(self.permute(nums)[k-1]), round(time.time()-s, 3)
        
        
    def permute(self, s):
        if len(s) <= 1: return [s]
        res = []
        
        for i in s:
            tmp_s = s[:]
            tmp_s.remove(i)
            tmp = self.permute(tmp_s)
            
            for j in tmp:
                j.insert(0, i)
                res.append(j)
        return res
        


ans = Solution()
print(ans.getPermutation(9, 24))
9
24
