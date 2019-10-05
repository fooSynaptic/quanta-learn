# encoding = utf-8
# /usr/bin/python3

'''
原地址：https://www.coursera.org/learn/algorithms-part1
教材：Algorithms,Fourth Edition 算法 第四版
'''
import random, time
from random import randint

random.seed(1234)


'''quick find (eager algorithm)'''
'''Time complexity On^2'''
class QuickfindUF():
    def __init__(self, N):
        self.size = N
        self.id = [i for i in range(N)]
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def Union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i in range(self.size):
            if self.id[i] == pid:
                self.id[i] = qid


"""Quick union"""
'''Time Complexity: worst case On^2'''
class QuickUnion():
    def __init__(self, N):
        self.size = N
        self.id = [i for i in range(N)]

    def root(self, item):
        while not item == self.id[item]:
            item = self.id[item]
        return item

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def Union(self, p, q):
        '''change of root of p point to root of q'''
        i = self.root(p)
        j = self.root(q)
        self.id[j] = i
       

'''Quick union-Improvement: weighting
- Modify Quick union to avoid tall trees
- Keep track the size of each tree
- Balence by link the root of smaller tree to the root of bigger tree
Time cpx: nlogn
'''
class QuickUnionImprove():
    def __init__(self, N):
        self.size = N
        self.id = [i for i in range(N)]
        self.SZ = [1 for _ in range(N)]

    def root(self, item):
        while not item == self.id[item]:
            item = self.id[item]
        return item

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def Union(self, p, q):
        '''change of root of p point to root of q'''
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.SZ[i] < self.SZ[j]:
            self.id[i] = j
            self.SZ[j] += self.SZ[i]
        else:
            self.id[j] = i
            self.SZ[i] += self.SZ[j]


'''Quick union-Improvement2: flatten the tree

Time cpx: N
'''
class QuickUnionImprove2():
    def __init__(self, N):
        self.size = N
        self.id = [i for i in range(N)]

    def root(self, item):
        while not item == self.id[item]:
            self.id[item] = self.id[self.id[item]]
            item = self.id[item]
        return item

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def Union(self, p, q):
        '''change of root of p point to root of q'''
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        self.id[j] = i


'''Quick union-Improvement3: flatten the tree + weighting

Time cpx: N
'''
class QuickUnionImprove3():
    def __init__(self, N):
        self.size = N
        self.id = [i for i in range(N)]
        self.SZ = [1 for _ in range(N)]

    def root(self, item):
        while not item == self.id[item]:
            self.id[item] = self.id[self.id[item]]
            item = self.id[item]
        return item

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def Union(self, p, q):
        '''change of root of p point to root of q'''
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.SZ[i] > self.SZ[j]:
            self.id[j] = i
            self.SZ[i] += self.SZ[j]
        else:
            self.id[i] = j
            self.SZ[j] += self.SZ[i]






def testcase(finderClass):
    s = time.time()
    n = 10**7
    finder = finderClass(n)
    i = 0
    while i < pow(n, 0.5):
        finder.Union(randint(0, n-1), randint(0, n-1))
        i += 1
    print(time.time() - s)
    

def run():
    #testcase(QuickfindUF) # too slow already abandomed
    testcase(QuickUnion)
    testcase(QuickUnionImprove)
    testcase(QuickUnionImprove2)
    testcase(QuickUnionImprove3)



run()


'''
Perculation with Monte Carol simulation
'''

def Perculation(cubeSize, threashould = 0.593):
    def _perculate():
        '''
        return whether the perculation state reached
        '''
        #first we got the grid, we want to union the block both are 1
        finder = QuickUnionImprove3(cubeSize*cubeSize)
        for i in range(cubeSize):
            for j in range(cubeSize):
                if grid[i][j] == 0:
                    continue
                #for block(i, j) the order is i*cubeSize+j
                #its left: i*cubeSize+j-1 if j > 0
                if j > 0 and grid[i][j-1]==1: finder.Union(i*cubeSize+j, i*cubeSize+j-1)
                #its right: i*cubeSize+j+1 if j+1 < cubeSize
                if j+1 < cubeSize and grid[i][j+1]==1: finder.Union(i*cubeSize+j, i*cubeSize+j+1)
                #its upside: (i-1)*cubeSize+j if i > 0
                if i>0 and grid[i-1][j]==1: finder.Union(i*cubeSize+j, (i-1)*cubeSize + j)
                #its downside: (i+1)*cubeSize+j if i+1 < cubeSize
                if i+1 < cubeSize and grid[i+1][j]==1: finder.Union(i*cubeSize+j, (i+1)*cubeSize+j)
        
        ### return if the perculate condition reached
        for top in range(cubeSize):
            for bottom in range(cubeSize):
                if finder.connected(top, (cubeSize-1)*cubeSize+bottom):
                    return True
        return False


    ### initial
    grid = [[0 for _ in range(cubeSize)] for _ in range(cubeSize)]

    ### open or not
    openTimes = 0
    while not _perculate():
        for i in range(cubeSize):
            for j in range(cubeSize):
                if grid[i][j] == 1:
                    continue
                grid[i][j] = 1 if random.random() > 1 - threashould else 0
        openTimes += 1
    
    print(threashould, openTimes)
    return openTimes
    



def testPerculation():
    import matplotlib.pyplot as plt
    times = []
    for i in range(5, 995):
        t = Perculation(100, i*0.001)
        times.append(t)
    plt.plot([i*0.001 for i in range(5, 995)], times)
    plt.show()

#testPerculation()


