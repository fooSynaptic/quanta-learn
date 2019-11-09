# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        
        self.ans = 0
        def backtrack(number):
            print(number)
            if number == 0:
                self.ans += 1
                return 
 
            for i in range(1, number+1):
                backtrack(number-i)

        
        
        backtrack(number)

        return self.ans

ans = Solution()
print(ans.jumpFloorII(3))