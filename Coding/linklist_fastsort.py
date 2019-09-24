# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _node_swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val
    
    def _fast_sort(self, pBegin, pEnd):
        def _partition_Linklist(pBegin, pEnd):
            key = pBegin.val

            p = pBegin
            q = p.next

            while q != pEnd:
                if q.val < key:
                    p = p.next
                    self._node_swap(p, q)
                q = q.next
            self._node_swap(pBegin, p)
            return p
        
        if pBegin != pEnd:
            partition = _partition_Linklist(pBegin, pEnd)
            self._fast_sort(pBegin, partition)
            self._fast_sort(partition.next, pEnd)
        
        
        
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #use fast sort for linklist
        curr = head
        end = head
        while end:
            end = end.next
        self._fast_sort(curr, end) 
        
        return head
        
        
        
    
                    