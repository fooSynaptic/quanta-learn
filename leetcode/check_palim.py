# py3

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrom(i, j):
            return all(s[i+k] == s[j-k] for k in range((j-i)//2+1))
        
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return isPalindrom(i+1, j) or isPalindrom(i, j-1)
        return True



res = Solution()


if res.validPalindrome("tcaac"):
	print("Yes!")
else:
    print("No!")