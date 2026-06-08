"""基于链表的栈实现。

参考：https://www.bilibili.com/video/av60977932/?p=13
"""


class linkedStack():
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        # 初始 first 为哨兵；压栈后 first 指向栈顶，哨兵沉到栈底（其 next 为 None 表示空栈）
        self.first = self.Node(None)

    def isEmpty(self):
        return self.first.next is None


    def push(self, item):
        oldFirst = self.first
        self.first = self.Node(item)
        self.first.next = oldFirst

    def pop(self):
        item = self.first.val
        self.first = self.first.next
        return item
