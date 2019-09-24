#python3

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = str(self.factorial(n))
        cnt = 0
        for i in range(1, len(res))[::-1]:
            if res[i] == '0':
                cnt += 1
            else:
                break
        
        return cnt
        
        
    def factorial(self, n):
        if n < 3:
            return n
        return n * self.factorial(n-1)

ans = Solution()
print(ans.trailingZeroes(7246))