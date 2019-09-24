
#define of BST
Min = -9999
Max = 9999

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


preorder = [10,5,1,8,15,7]
inorder = [1,5,8,10,15,7]

#algorithm to build a tree
def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not inorder:
        return None
    root = TreeNode(preorder.pop(0))
    inorderIndex = inorder.index(root.val) 
    root.left = buildTree(preorder, inorder[:inorderIndex]) 
    root.right = buildTree(preorder, inorder[inorderIndex+1:]) 
    #root.left = self.buildTree(preorder, inorder[:inorderIndex]) 

    return root

head = buildTree(preorder, inorder)
print(head.val)
#build a wrapper solving the max_subTree problem
class Solution():
    def largestBSTSubtree(self, root):
        self.res = 0

        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return
        #for every node, search its max sub-tree count.
        tmp = self.countSub(root, Min, Max)
        if tmp != -1:
            self.res = max(tmp, self.res)
            return
        self.dfs(root.left)
        self.dfs(root.right)
    
    def countSub(self, root, MIN, MAX):
        if not root: return 0
            #return root.val
        elif root.val < MIN or root.val > MAX: return -1
        left_sum = self.countSub(root.left, MIN, root.val)
        right_sum = self.countSub(root.right, root.val, MAX)
        #check valide sub_tree
        if left_sum == -1:
            return -1
        elif right_sum == -1:
            return -1

        return left_sum+right_sum+1



ans = Solution()
print(ans.largestBSTSubtree(head))






'''
class Solution {
public:
    int largestBSTSubtree(TreeNode* root) {
        int res = 0;
        dfs(root, res);
        return res;
    }
    void dfs(TreeNode *root, int &res) {
        if (!root) return;
        int d = countBFS(root, INT_MIN, INT_MAX);
        if (d != -1) {
            res = max(res, d);
            return;
        }
        dfs(root->left, res);
        dfs(root->right, res);
    }
    int countBFS(TreeNode *root, int mn, int mx) {
        if (!root) return 0;
        if (root->val <= mn || root->val >= mx) return -1;
        int left = countBFS(root->left, mn, root->val);
        if (left == -1) return -1;
        int right = countBFS(root->right, root->val, mx);
        if (right == -1) return -1;
        return left + right + 1;
    }
};
'''