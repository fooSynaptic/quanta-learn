#py3


class Solution(object):
    class trie():
        def __init__(self, cnt):
            self.head = self.node('')
            self.threshold = cnt
            
        class node():
            def __init__(self, val):
                self.val = val
                self.cnt = 1
                self.children = {}
                
        def insert(self, word):
            curr = self.head
            for char in word:
                if char not in curr.children:
                    curr.children[char] = self.node(char)
                elif char in curr.children:
                    curr.children[char].cnt += 1
                curr = curr.children[char]

        def search(self, word):
            curr = self.head
            s = ''
            for i in range(max(1,len(word))):
                if word[i] not in curr.children:
                    print("1")
                    break
                elif curr.cnt == self.threshold and (curr.children[word[i]].cnt < self.threshold\
                    or not curr.children.get(word[i])):
                    print(2)
                    s += curr.val
                    break
                s += curr.val
                curr = curr.children[word[i]]
            
            if curr.cnt == self.threshold:
                return s
            else:
                return ''
            
            
        
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or '' in strs: return ''
        elif len(strs) == 1: return strs[0]
        elif len(strs) == 2:
            if strs[0] == strs[1]: return strs[0]
            else:
                return strs[0][:len([1 for i in range(min(len(x) for x in strs)) if strs[0][i] == strs[1][i]])]
        
        trie = self.trie(len(strs))
        
        for word in strs:
            trie.insert(word)
            trie.insert(sorted(strs)[-1] + ' ')
            
        return trie.search(strs[0]+ '  ')
        

ans = Solution()
print(ans.longestCommonPrefix(['a', 'a' ,'a']))