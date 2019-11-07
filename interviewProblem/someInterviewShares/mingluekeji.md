题目来源：
```
作者：一只不想加班的🐷
链接：https://www.nowcoder.com/discuss/335077?toCommentId=4884383
来源：牛客网

我是宣讲会现场面试的，现场只面了一面技术，问的内容记得不是太清楚了，首先介绍了一下自己的项目，尤其是项目里面的算法，问的比较细致，一些细节会详细问。问了lstm原理，优点；现场有写代码，好像是无向图里面求最短路径，这个我不会，然后面试官换了二叉树后序遍历，非递归形式。 后来是电话二面，偏工程，问了python内存释放，线程进程，python的多线程实现方式，还有几个排序算法。
```
---

# 无向图求最短路径（Dijkstra, Floyd）
```python
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
```





# 二叉树的后序遍历非递归形式
```python
from random import randint
import random
random.seed(123)

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

traverse(head)

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


print(iterative(head))
```


# python内存释放，线程进程，python的多线程实现方式
- python的垃圾收集机制：
其中涉及到的内容包括引用机制，动态类型和共享引用这些基本概念。
python动态类型是指python中的类型是在运行的过程中自动决定的，而不是通过代码声明的，而不是通过代码声明的，这意味着没有必要事先声明变量。
变量名和对象是划分开的，变量名永远没有任何关联的类型信息，类型是和对象关联的，而不存在与变量名中。
在python内部，变量事实上是到对象内存空间的一个指针，而且指向的对象可以随着程序赋值语句而不断变化。
总结一下：变量名没有类型，只有对象才有类型，变量值是引用了不同类型的对象而已。每一个对象中都包含了两个头部信息，一个是类型标志符，标志这个对象的类型，一个是引用的计数器，用来表示这个对象被多少个变量名所引用，如果此时没有变量引用他，那么就可以回收这个对象。
python的垃圾回收机制：
每当一个变量名被赋予了一个新的对象，那么之前的那个对象占用的空间就会被回收，前提是如果他没有被其他变量名或者对象引用，这种自动回收对象空间的机制就叫做垃圾回收。
具体的回收机制：python在每个对象中保存了一个计数器，计数器记录了当前指向该对象的引用的数目。一旦这个计数器被设置为0，这个对象的内存空间就会被自动回收。这就使得我们不必像C++那样需要专门编写释放内存空间的代码了。
当给一个变量附一个新的对象，并不是替换原始的对象，而是让这个变量去引用一个新的对象，原有的对象的引用计数会随之减去1.
- python的多进程实现方式：
cpu单核： 都选择使用线程
多任务处理计算密集型： 无法实现并行，创建进程的开销大，选择开启一个进程，多个线程。
多任务处理I/O密集型：无法实现并行的进程开销大，而且换进程的速度不如线程快，选择开启一个进程，多个线程。

CPU多核：
多任务处理计算密集型，多核实现进程并行，对于线程无法实现并行，选择开启多个进程。
多任务处理I/O密集型，多核情况下进程并发，线程在一个cpu内进行切换并发，差别在于并发的切换速度，选择开启一个进程，多个线程。

对于CPU单核而言，可以多线程，也可以多进程。但是单核情况下的进程也是并发的，很容易理解，由于计算单元只有一个，所以进程在某一特定时刻，只能有一个进程。由于进程之间的创建很浪费时间（可以认为是保存程序的上下文需要费时费力），切换了也还是一个cpu进行计算，不如让它耐心的一个个算好了。而同属于一个进程的多个线程，切换之间并不耗时，但是当遇到I/O处理的时候可以将cpu的算力让给其他需要的线程，所以对于单核而言，不管是计算密集型还是I/O密集型，都可以选择开启一个进程，多个线程。
在python之中，但对于多核而言，由于算力不止一个了，对于计算密集型的多任务，多进程可以完全是并行的，而多线程由于GIL的限制，同一时刻只能有一个GIL被抢占，其他的只能等待交替执行，这样反而会浪费时间。但I/O密集型，CPU算力有也白白浪费，创建那么多线程，也没有用上，还浪费创建时间，不如单进程多线程，这样线程在I/O操作的时候，也会将算力让给别的线程。

multiprocessing.Pool类可以创建一个进程池，进程池通过调用apply_async函数来创建一个新的进程
```python
from multiprocessing import Pool
import os, time

def sub_process(n):
    time.sleep(1)
    print("Process %s is running!" % os.getpid())

p = Pool(4)
for i in range(5):
    p.apply_async(sub_process, args=(i+1, ))

p.close()
p.join()
```


python的多线程实现方式：
threading模块
```python
import threading, time

def run():
    print("{} is running...".format(threading.current_thread().name))


def thread():
    run()

time.sleep(1)

#t = threading.Thread(target=thread, name="sub_Thread")
#t.start()
for _ in range(10):
    t = threading.Thread(target=thread, name="sub_Thread")
    t.start()

t.join()
```

# 排序算法
