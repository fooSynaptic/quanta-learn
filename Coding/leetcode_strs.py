#py3
import time
from time import time as now


class Solution:
    def findMaxForm(self, strs, m, n):
        store = [m, n]
        l = len(strs)
        
        maxl = 0
        
        def restore(store, candidates, s):
            #print(store, candidates, 'restore',s)
            #time.sleep(1)
            nonlocal maxl
            
            if l - len(candidates) > maxl:
                maxl = l - len(candidates)
            #maxl = max(maxl, l - len(candidates))
            if store[0] < 0 or store[1] < 0 or not candidates or len(s) == l:    
                return
            print("we will steped in candidates as :", candidates)
            for i in range(len(candidates)):
                if candidates[i].count('1') <= store[1] and candidates[i].count('0') <= store[0]:
                    restore([store[0]-candidates[i].count('0'), \
                            store[1]-candidates[i].count('1')], \
                           candidates[:i] + candidates[i+1:], \
                               s + [candidates[i]])
                    
        restore(store, strs, [])
        return maxl


ans = Solution()
strs = ["0","1101","01","00111","1","10010","0","0","00","1","11","0011"]
m = 63
n = 36
s = now()
print(ans.findMaxForm(strs, m, n))
print("Time consume: {}.".format(round(now()-s), 5))