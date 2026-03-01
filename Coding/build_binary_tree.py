"""
Construct Binary Tree from Preorder and Inorder Traversal.

Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: Root of constructed tree:
            3
           / \
          9  20
            /  \
           15   7

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the recursion stack and hash map
"""

from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""
    
    def __init__(self, value: int):
        """Initialize a tree node with given value."""
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
    
    def __repr__(self) -> str:
        """String representation of the tree node."""
        return f"TreeNode({self.value})"


class Solution:
    """Solution for building binary tree from traversals."""
    
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build binary tree from preorder and inorder traversals.
        
        Args:
            preorder: List of node values in preorder traversal order
            inorder: List of node values in inorder traversal order
            
        Returns:
            Root node of the constructed binary tree, or None if empty input
            
        Raises:
            ValueError: If preorder and inorder have different lengths
        """
        if not preorder or not inorder:
            return None
            
        if len(preorder) != len(inorder):
            raise ValueError("Preorder and inorder must have the same length")
        
        # Use a copy of preorder that we can modify with pop
        preorder_copy = list(preorder)
        return self._build_subtree(preorder_copy, inorder)
    
    def _build_subtree(
        self, 
        preorder: List[int], 
        inorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Recursively build subtree from remaining preorder and inorder elements.
        
        Args:
            preorder: Remaining preorder elements (modified in place)
            inorder: Inorder elements for current subtree
            
        Returns:
            Root of constructed subtree
        """
        if not inorder:
            return None
        
        # The first element in preorder is the root of current subtree
        root_value = preorder.pop(0)
        root = TreeNode(root_value)
        
        # Find the root position in inorder to split left and right subtrees
        root_index_in_inorder = inorder.index(root_value)
        
        # Recursively build left subtree (elements before root in inorder)
        root.left = self._build_subtree(
            preorder, 
            inorder[:root_index_in_inorder]
        )
        
        # Recursively build right subtree (elements after root in inorder)
        root.right = self._build_subtree(
            preorder, 
            inorder[root_index_in_inorder + 1:]
        )
        
        return root


def print_tree(node: Optional[TreeNode], level: int = 0) -> None:
    """Print tree structure in a visual format."""
    if node is None:
        return
    
    print_tree(node.right, level + 1)
    print('    ' * level + str(node.value))
    print_tree(node.left, level + 1)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    tree = solution.build_tree(preorder, inorder)
    print("Constructed tree:")
    print_tree(tree)
