#py3
import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution(object):
    def findBottomLeftValue(self, root):
        self.ans = None
        self.lv = -1
        self.helper(root, 0)
        return self.ans
    
    def helper(self, node, level):
        if not node:
            return
        if self.lv < level:
            self.lv = level
            self.ans = node.val
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)
'''

class Solution(object):
    def findBottomLeftValue(self, root):
        def helper(root, level):
            while root:
                print(root.val, self.lev, level)
                time.sleep(2)
                if self.lev < level:
                    self.lev = level
                    if not root.left and not root.right:
                        self.res = root.val
                        print(self.res)
                        
                helper(root.right, level+1)
                helper(root.left, level+1)
                break        
 
        self.res = None
        self.lev = -1
        helper(root, 0)
        return self.res


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ans = Solution()
res = ans.findBottomLeftValue(root)
print(res)
