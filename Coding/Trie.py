class Trie(object):
    
    class node(object):
        def __init__(self, val, label = False):
            self.val = val
            self.label = label
            self.children = {}
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """       
        self.head = self.node('')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.head
        for char in word[:-1]:
            if char not in curr.children:
                curr.children[char] = self.node(char)
            curr = curr.children[char]
        
        curr.children[word[-1]] = self.node(word[-1], label = True)
               
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if curr.label:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.head
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True



ops = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
var = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

ans = Trie()

def handle(method, val):
    return method(val)

for _op, _var in zip(ops, var):
    val = _var[0]
    print(_op, val, ':', handle(eval('ans.{}'.format(_op)), val))
