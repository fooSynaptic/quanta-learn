#py3

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 2:
            return [s[-1],s[0]]
        elif len(s) == 1:
            return s
        else:
            s[:len(s)//2] = self.reverseString(s[:len(s)//2])
            s[len(s)//2+1:] = self.reverseString(s[len(s)//2+1:])
        
            s = s[len(s)//2+1:] +[s[len(s)//2]] + s[:len(s)//2]
        return s


ans = Solution()
print(ans.reverseString(list('zhangshicheng')))