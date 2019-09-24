
class Solution():
    def deleteNode(self, root, key):
        if not root: return None
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right = self.deleteNode(root.right, key)
        else:
            if not (root.left and root.right): return root.left or root.right
            root.val = self.findClosest(root.right).val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def findClosest(self, node):
        while node.left:
            node = node.left
        return node
