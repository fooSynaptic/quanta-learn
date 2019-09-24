class Solution(object):
    #duplicated ops
    def climbStairs1(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n - 2)

    def climbStairs2(self,n):
        steps = [None for _ in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2,n):
            steps[i] = steps[i-2] + steps[i-1]
        
        return steps[n-1]


ans = Solution()
print(ans.climbStairs2(38))