
from random import randint
import random
random.seed(123)
import numpy as np
import logging



class treeNode():
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

head = treeNode(0)

curr = head
for _ in range(10):
    num = randint(1, 10)
    if num >= 5:
        curr.left = treeNode(num)
        curr = curr.left
    else:
        curr.right = treeNode(num)
        curr = curr.right

### recursion
def traverse(node):
    if not node: return 
    traverse(node.left)
    traverse(node.right)
    print(node.val)

#traverse(head)

### iterative
def iterative(node):
    if not node: return []

    stack = []
    res = []
    curr = node
    while curr is not None or len(stack) > 0:
        while curr is not None:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.right

        if len(stack) > 0:
            curr = stack.pop()
            curr = curr.left

    return res[::-1]


#print(iterative(head))

def Dijkstra():
    """return the shortest path from 0 -> n-1"""

    n = 10
    grid = [[1 for _ in range(n)] for _ in range(n)]
    dis = [list(x) for x in np.random.rand(n, n)]
    S = {"0": 0}


    while max(len(x) for x in S) < n:
        newS = dict()
        for path in S.keys():
            head = int(path[-1])

            pathrestore = dict()
            for tgt in range(10):
                if str(tgt) in path: continue
                pathrestore[tgt] = dis[head][tgt]

            if len(pathrestore) > 0:
                tail = sorted(pathrestore.items(), key=lambda x:x[1])[-1][0]
                newS[path + str(tail)] = S[path] + pathrestore[tail]
        S.update(newS)

    for p in S:
        print(p, S[p])

    print("Done!")

Dijkstra()


        
            
            





def Floyd():
    '''
    Floyd算法是一个经典的动态规划算法。用通俗的语言来描述的话，首先我们的目标是寻找从点i到点j的最短路径。\
    从动态规划的角度看问题，我们需要为这个目标重新做一个诠释
    从任意节点i到任意节点j的最短路径不外乎2种可能，
    1是直接从i到j，
    2是从i经过若干个节点k到j。
    所以，我们假设Dis(i,j)为节点u到节点v的最短路径的距离，对于每一个节点k，
    我们检查Dis(i,k) + Dis(k,j) < Dis(i,j)是否成立，
    如果成立，证明从i到k再到j的路径比i直接到j的路径短，
    我们便设置Dis(i,j) = Dis(i,k) + Dis(k,j)，
    这样一来，当我们遍历完所有节点k，Dis(i,j)中记录的便是i到j的最短路径的距离。
    算法复杂度为O(n^3)，空间复杂度为n平方。
    '''
    n = 10
    grid = [[1 for _ in range(n)] for _ in range(n)]
    p = [list(x) for x in np.random.rand(n, n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or k == i or k == j:
                    pass
                else:
                    if p[i][j] > p[i][k] + p[k][i]:
                        p[i][j] = p[i][k] + p[k][i]
                        grid[i][j] = k
    
    logging.info('distance matrix:')
    for x in p: print(x)
    logging.info('path matrix')
    for x in grid: print(x)


Floyd()