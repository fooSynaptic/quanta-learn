# encoding = utf-8
# /usr/bin/python3

class Tree_node():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def check(node):
    if not node:
        return 0
    
    left, right = 0, 0
    if node.left:
        left = check(node.left)
    
    if node.right:
        right = check(node.right)
    
    if not abs(left-right) <= 1:
        return False
    return 1 + left + right

def test_case():
    root = Tree_node(1)
    root.left = Tree_node(1)
    root.right = Tree_node(1)
    root.left.left, root.left.right = Tree_node(1), Tree_node(1)
    root.right.left = Tree_node(1)

    ###
    print('Valid balence BST' if check(root) else "Not valid")



test_case()