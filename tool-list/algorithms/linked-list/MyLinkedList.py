"""单链表实现（LeetCode 707 风格），用哨兵头节点简化边界处理。"""


class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        # pre_head 是 head 之前的哨兵节点，省去对空链表/头部的特判
        self.pre_head = self.Node(None)
        self.sz = 0

    def _get(self, i):
        """核心辅助：返回 (pre, h)，h 是第 i 个节点（越界为 None），pre 是其前驱。"""
        j = 0
        h = self.pre_head.next
        pre = self.pre_head

        while j < i and h:
            j += 1
            pre = h
            h = h.next

        return (pre, h)

    def get(self, i):
        if i < 0 or i >= self.sz:
            return -1
        (_, h) = self._get(i)
        return h.val if h else -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.sz, val)

    def addAtIndex(self, i, val):
        if i < 0 or i > self.sz:
            return
        (pre, _) = self._get(i)
        node = self.Node(val)
        node.next = pre.next
        pre.next = node
        self.sz += 1

    def deleteAtIndex(self, i):
        if i < 0 or i >= self.sz:
            return
        (pre, h) = self._get(i)
        pre.next = h.next
        self.sz -= 1


def demo():
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    print([ll.get(i) for i in range(ll.sz)])
    ll.deleteAtIndex(1)
    print([ll.get(i) for i in range(ll.sz)])


if __name__ == "__main__":
    demo()
