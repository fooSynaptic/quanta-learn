#py3
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:

            print("preorder:{}, inorder:{}".format(preorder, inorder))
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind]) # Line A
            root.left = self.buildTree(preorder, inorder[:ind]) # Line C
            root.right = self.buildTree(preorder, inorder[ind+1:]) # Line B
        
            return root


ans = Solution()
#print(ans.buildTree([3,9,20,15,7], [9,3,15,20,7]))