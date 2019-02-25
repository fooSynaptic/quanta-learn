#py3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
for the current node is it one to be kept?

1.yes return it after trimming recursively its left and right subnodes
2.no, only one my subtrees can be a potential non Null subtree after being trimmed
'''


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif L <= root.val <= R:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
            return root
        elif root.val < L:
            return self.trimBST(root.right, L,R)
        elif root.val > R:
            return self.trimBST(root.left, L,R)
