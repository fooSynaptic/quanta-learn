#py3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
class Solution:
    def sortedArrayToBST(self, nums):
        length, mid = len(nums), len(nums)//2+1
        
        root = TreeNode(nums[mid-1])
        #hander = [root]

        curr, i = root, mid-1
        while len(nums) > length//2+1:
            curr = root
            while i:
                print('left:', curr.val)
                curr.left = TreeNode(nums[i-1])
                curr = curr.left
                i -= 1
            curr = root
            while len(nums) > length//2+1:
                print('right:', curr.val, nums)
                curr.right = TreeNode(nums.pop())
                curr = curr.right
            
        return root
'''

#iterative solution

class Solution(object):    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return
        lb = 0
        ub=len(nums)
        middle = ub//2
        root = TreeNode(nums[middle])
        walker = root
        if ub - middle > 1:
            rights = [(root,middle+1,ub)]   #store rights
        else:
            rights = []
        ub = middle
        while 1:
            print(lb, ub)
            diff = ub - lb
            if diff:
                middle = lb+(diff//2)       #the point is middle cannot stay still
                walker.left = TreeNode(nums[middle])
                walker = walker.left
            elif rights:
                walker,lb,ub = rights.pop()
                diff = ub-lb
                middle = lb+(diff//2)
                walker.right = TreeNode(nums[middle])
                walker = walker.right
            else:
                break
            if ub - middle > 1:
                rights.append((walker,middle+1,ub))
            ub=middle
            
        return root



arr = [-10,-3,0,5,9]

ans = Solution()
head = ans.sortedArrayToBST(arr)

def traverse(node):
    if not node: return

    traverse(node.left)
    print(node.val)
    traverse(node.right)

print("Inspect:")
traverse(head)


