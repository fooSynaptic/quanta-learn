#py3
import time

class Solution:
    def coinChange(self, coins, amount):
        if amount in coins: return 1
        elif amount == 0: return 0

        def recursion(amount, coins):
            if amount < 0:
                return float('inf')
            elif amount == 0:
                return 0
            
            
            return min([recursion(amount-x, coins) for x in coins]) + 1

        return recursion(amount, coins)


ans = Solution()
res = ans.coinChange([1,2,5], 100)
print(res)