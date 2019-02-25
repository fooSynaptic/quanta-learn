class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


arr  = [5,3,2,4,1]
head = ListNode(arr[0])



def init_link_list(data, head):
    curr = head

    for i in data[1:]:
        node = ListNode(i)
        curr.next = node
        node.prev  = curr
        curr = curr.next

init_link_list(arr, head)

def node_Swap(node1, node2):
    tmp_val = node2.val
    node2.val = node1.val
    node1.val = tmp_val

'''
#solve with fast sort
def iTeration(pBegin, pEnd):
    p = pBegin
    key = pBegin.val
    q = p.next
    print('key:', key)
    while q!= pEnd:
        if q.val < key:
            p = p.next
            node_Swap(p, q)

        q = q.next
    node_Swap(p, pBegin)

    return p

def linkList_quickSort(pBegin, pEnd):
    if pBegin != pEnd:
        #print("input Mark:", pBegin.val, pEnd.val)
        partion = iTeration(pBegin, pEnd)
        linkList_quickSort(pBegin, partion)
        linkList_quickSort(partion.next, pEnd)

tmp_head = head
tmp_end = head

while tmp_end:
    tmp_end = tmp_end.next

#print('from start to end:', tmp_head.val, tmp_end.val)
linkList_quickSort(tmp_head, tmp_end)

print("========After===========")
while head:
    print(head.val)
    head = head.next
'''

#solve with insert sort

def insertionSort_List(head):
    if head == None and head.next == None:
        return head

    p = head.next
    p_start = ListNode(0)
    p_end = head
    p_start.next = head

    while p:
        tmp = p_start.next
        pre = p_start
        while tmp != p and p.val > tmp.val: #find the node to insert
            tmp = tmp.next
            pre = pre.next
        
        if tmp == p: p_end = p
        else:
            #swap the node val of p_end and p
            p_end.next = p.next
            p.next = tmp
            pre.next = p
        
        p = p_end.next
    
    head = p_start.next

    del p_start
    return head


head = insertionSort_List(head)

print("========After===========")
while head:
    print(head.val)
    head = head.next