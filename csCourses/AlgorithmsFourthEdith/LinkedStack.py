# encoding = utf-8
# /usr/bin/python3

'''ref: https://www.bilibili.com/video/av60977932/?p=13'''


class linkedStack():
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.first = self.Node(None)

    
    def isEmpty(self):
        return self.first is None


    def push(self, item):
        oldFirst = self.first
        self.first = self.Node(item)
        self.first.next = oldFirst

    
    def pop(self):
        item = self.first.val
        self.first = self.first.next
        return item