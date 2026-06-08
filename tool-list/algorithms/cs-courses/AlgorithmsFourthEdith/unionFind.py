"""并查集（Union-Find）的几种实现，并附渗流（Percolation）蒙特卡洛模拟。

原地址：https://www.coursera.org/learn/algorithms-part1
教材：《算法（第 4 版）》Algorithms, Fourth Edition
"""

import random
import time
from random import randint

random.seed(1234)


class QuickfindUF():
    """Quick-Find（急切式）：connected O(1)，union O(n)。"""

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


class QuickUnion():
    """Quick-Union：用父指针树表示，最坏情况树退化为链，操作 O(n)。"""

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
        # 让 p 的根指向 q 的根
        i = self.root(p)
        j = self.root(q)
        self.id[j] = i


class QuickUnionImprove():
    """加权 Quick-Union：把小树挂到大树下，避免树过高，近似 O(log n)。"""

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
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        # 小树挂到大树根下，并累加子树规模
        if self.SZ[i] < self.SZ[j]:
            self.id[i] = j
            self.SZ[j] += self.SZ[i]
        else:
            self.id[j] = i
            self.SZ[i] += self.SZ[j]


class QuickUnionImprove2():
    """路径压缩 Quick-Union：root 过程中把节点指向其祖父，逐步压平树。"""

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
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        self.id[j] = i


class QuickUnionImprove3():
    """加权 + 路径压缩：近乎常数的均摊复杂度。"""

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
    # QuickfindUF 太慢，已弃用，不再测
    testcase(QuickUnion)
    testcase(QuickUnionImprove)
    testcase(QuickUnionImprove2)
    testcase(QuickUnionImprove3)


if __name__ == "__main__":
    run()


def Perculation(cubeSize, threashould = 0.593):
    """渗流模拟：不断随机开格，直到顶行与底行连通，返回开格轮数。"""

    def _perculate():
        """判断当前网格是否已渗流（顶底连通）。"""
        # 先把所有相邻且都为 1（已开）的格子合并到一起
        finder = QuickUnionImprove3(cubeSize*cubeSize)
        for i in range(cubeSize):
            for j in range(cubeSize):
                if grid[i][j] == 0:
                    continue
                # 格子 (i, j) 的一维编号为 i*cubeSize+j，依次尝试与上下左右合并
                if j > 0 and grid[i][j-1] == 1:
                    finder.Union(i*cubeSize+j, i*cubeSize+j-1)
                if j+1 < cubeSize and grid[i][j+1] == 1:
                    finder.Union(i*cubeSize+j, i*cubeSize+j+1)
                if i > 0 and grid[i-1][j] == 1:
                    finder.Union(i*cubeSize+j, (i-1)*cubeSize + j)
                if i+1 < cubeSize and grid[i+1][j] == 1:
                    finder.Union(i*cubeSize+j, (i+1)*cubeSize+j)

        # 只要顶行任一格与底行任一格连通即视为渗流
        for top in range(cubeSize):
            for bottom in range(cubeSize):
                if finder.connected(top, (cubeSize-1)*cubeSize+bottom):
                    return True
        return False

    # 初始化全 0 网格
    grid = [[0 for _ in range(cubeSize)] for _ in range(cubeSize)]

    # 每轮以概率 threashould 把未开的格子开成 1，直到渗流
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
