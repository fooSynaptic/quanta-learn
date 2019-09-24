from build_binary_tree import Solution

ans = Solution()
root = ans.buildTree([7, 8, 9, 10, 11, 9, 8, 7, 6, 6, 5, 1, 4, 3, 2, 4, 5, 1, 2], [1, 6, 7, 8, 7, 9, 10, 9, 11, 8, 5, 6, 4, 3, 4, 1, 2, 5, 2])


#define of tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



#actually we want to serilize with preorder and inorder
class Codec: 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        inorder, preorder = [], []
        def inorder_track(root):
            if not root:
                return
            
            inorder_track(root.left)
            inorder.append(root.val)
            inorder_track(root.right)

        def preorder_track(root):
            if not root:
                return 
            preorder.append(root.val)
            preorder_track(root.left)
            preorder_track(root.right)
            

        curr1, curr2 = root, root
        inorder_track(curr1)
        preorder_track(curr2)

        return (inorder, preorder)

    def deserialize(self, data):
        inorder, preorder = data

        def build(preorder, inorder):
            if inorder:
                root = TreeNode(preorder.pop(0))
                idx = inorder.index(root.val)
                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])

                return root

        return build(preorder, inorder)

coder = Codec()
serlize_res = coder.serialize(root)
print(serlize_res)
deserilize_res = coder.deserialize(serlize_res)
print(deserilize_res)



