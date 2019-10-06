# encoding = utf-8
# /usr/bin/python3

'''ref: https://www.bilibili.com/video/av60977932/?p=14'''


class reSizedArrayStack():
    def __init__(self):
        self.arr = [None for _ in range(10)]
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def resize(self, mod = 'expand'):
        if mod == 'expand':
            self.arr += [None for _ in range(len(self.arr))]
        elif mod == 'shrink':
            self.arr = self.arr[:len(self.arr)//2]


    def push(self, val):
        self.arr[self.N] = val
        self.N += 1
        if self.N == len(self.arr):
            self.resize(mod = 'expand')
    
    def pop(self):
        if self.N == 0: return
        item = self.arr[self.N]
        self.N -= 1
        if self.N <= len(self.arr)/4:
            self.resize(mod = 'shrink')