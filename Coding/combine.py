#py3

class Solution:
    def combine(self, n, k):
        if k == 1: return [[i] for i in range(1, n+1)]
        if k==n: return [[i for i in range(1, n+1)]]

        res = []
        def restore(combs, n, k):
            if len(combs[0]) == n: return combs
            if k == 2:
                res = []
                for i in range(len(combs)):
                    for j in range(combs[i][-1]+1, n+1):
                        if j in combs[i]:
                            pass
                        else:
                            candidate = combs[i]+[j]
                            candidate.sort()
                            if not candidate in res: res.append(candidate)
                   
                return res if res else combs
            else:
                return restore(restore(combs, n, k-1), n, k-1)
                
            
        return restore([[i] for i in range(1, n+1)], n, k)
        
            
        

ans = Solution()
print(ans.combine(20, 16))