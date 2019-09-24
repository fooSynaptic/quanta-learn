#py3

class Solution:
    def wordBreak(self, s, wordDict):
        breakp = [0]
        res = []
        ans = []
        
        for i in range(len(s)+1):
            for j in breakp:
                
                if s[j:i] in wordDict:
                    print(j, i, s[j:i])
                    breakp.append(i)
                    res.append([j, i, s[j:i]])
                    
        #print(res)
        for i in range(len(res)):
            sta, end, string = res[i]
            while end < len(s):
                for j in range(i, len(res)):
                    s2, e2, string2 = res[j]
                    if end == s2:
                        sta, end = s2, e2
                        string += ' '+string2
                        #break
            #print(string)
            if len(string) > len(s): ans.append(string)
                
        return ans




ans = Solution()
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(ans.wordBreak(s, wordDict))