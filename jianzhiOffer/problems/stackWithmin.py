# -*- coding:utf-8 -*-
### use list with pop method only

class Solution:
    def __init__(self):
        self.array, self.heap = [], []
    
    ###min heap
    def heapify(self, i, n):
        if self.heap[i] > self.heap[n]:
            self.heap[n], self.heap[i] = self.heap[i], self.heap[n]
        top = self.heap[n]
        flag = False

        while 2*i+1 < n:
            minPos = 2*i+1
            if minPos+1 < n and self.heap[minPos+1] < self.heap[minPos]:
                minPos += 1
            if self.heap[minPos] < top:
                flag = True 
                self.heap[i] = self.heap[minPos]
                i = minPos
            else:
                break
                
        if flag: self.heap[i] = top

  
    
    
    
    def push(self, node):
        # write code here
        self.array.append(node)
        self.heap.append(node)
        #self.heapify(0, len(self.heap)-1)
        for i in range(len(self.heap)//2-1, -1, -1):
            self.heapify(i, len(self.heap)-1)
        
    def pop(self):
        # write code here
        num = self.array.pop()
        self.heap.remove(num)
        for i in range(len(self.heap)//2-1, -1, -1):
            self.heapify(i, len(self.heap)-1)
        
        
    def top(self):
        # write code here
        if not self.array: return
        return self.array[-1]
    
    def min(self):
        # write code here
        print("peek heap: ", self.heap)
        if not self.heap: return  
        return self.heap[0]




def testcase():
    ops = ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
    ans = Solution()
    for p in ops:
        if "PSH" in p:
            ans.push(int(p[-1]))
        elif p == "MIN":
            print(ans.min())
        elif p == "POP":
            ans.pop()



testcase()
    