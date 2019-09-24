# py3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

arr  = [1,1,1,2,3]
head = ListNode(arr[0])

curr = head
for x in arr[1:]:
    curr.next = ListNode(x)

print("========Before===========")
while head:
    print(head.val)
    head = head.next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
                
        pre = ListNode(None)
        pre.next = head
        cur = head
        
        
        while cur:
            if not cur.next:
                return head
            if cur.val == cur.next.val:
                pre.next = pre.next.next.next
                cur = pre.next

            else:
                cur = cur.next
                pre = pre.next
                
        
        return head

res = Solution()
res.deleteDuplicates(head)


print("AFter=====")
while head:
    print(head.val)
    head = head.next