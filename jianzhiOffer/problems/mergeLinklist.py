# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, p1, p2):
        # write code here
        if not p1: return p2
        if not p2: return p1
        
        p = None
        
        if p1.val > p2.val:
            p = p2
            p2 = p2.next
        else:
            p = p1
            p1 = p1.next
            
        curr = p
        while p1 and p2:
            if p1.val >= p2.val:
                curr.next = p2
                p2 = p2.next
            elif p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
                
            curr = curr.next
        
        if p1: curr.next = p1
        elif p2: curr.next = p2

        return p
                



def testcase():
    class node():
        def __init__(self, val):
            self.val = val
            self.next = None


    ans = Solution()
    p1, p2 = node(1), node(1)
    curr1, curr2 = p1, p2

    for x in [1,3,5,7]:
        curr1.next = node(x)
        curr1 = curr1.next

    for y in [2,4,6,8,9]:
        curr2.next = node(y)
        curr2 = curr2.next
    p1, p2 = p1.next, p2.next

    res = ans.Merge(p1, p2)
    while res:
        print(res.val)
        res = res.next


    
            
        
        
        
testcase()