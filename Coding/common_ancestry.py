# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print(root.left.val, p.val, root.right.val, q.val)
        #print(self.findchild(root.left, p), self.findchild(root.right, q))
        if not root.left and not root.right:         
            return  root.val == p.val or root.val == q.val
        if self.findchild(root.left, p) or self.findchild(root.right, p) and self.findchild(root.left, q) or self.findchild(root.right, q):
            return root.val 
        else:
            return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
        
    def findchild(self, curr, tgt):
        if not curr:
            return False
        if curr.val == tgt.val:
            return True
        else:
            return self.findchild(curr.left, tgt) or self.findchild(curr.right, tgt)
        

#nodes = [3,5,1,6,2,0,8,null,null,7,4]

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

ans = Solution()
print(ans.lowestCommonAncestor(root, root.left, root.right))