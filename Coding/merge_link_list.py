#py3
import time


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#generate test cases
node1 = ListNode(1)
node2 = ListNode(1)

curr = node1
curr.next = ListNode(2)
curr.next.next = ListNode(4)

curr = node2
curr.next = ListNode(3)
curr.next.next = ListNode(4)

node1, node2 =  node2, node1
'''
node1 4 5 6
mode2 1 2 3
'''

class Solution(object):
    # in-place, iteratively        
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                #nxt = cur.next
                cur.next = l2       #for lower l2.val switch cur.next from l1 to l2
                tmp = l2.next       #similar to the condition when l2.val < l1.val, make curr.next pointer flow through l2 and point to next
                #l2.next = nxt
                l2 = tmp             #similar to l1 = l1.next
            cur = cur.next
            print(cur.val)
            time.sleep(1)
        cur.next = l1 or l2
        print(cur.val, curr.next.val)
        return dummy.next



ans = Solution()
node = ans.mergeTwoLists(node1, node2)


print('after merging===================')
while node:
    print(node.val)
    time.sleep(1)
    node = node.next
