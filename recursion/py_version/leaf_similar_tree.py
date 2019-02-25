#py3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_sequence(root):
            if root:
                if not root.left and not root.right:#handle terminal node
                    return [root.val]
                return get_sequence(root.left) + get_sequence(root.right)
            return []
        return get_sequence(root1) == get_sequence(root2)
