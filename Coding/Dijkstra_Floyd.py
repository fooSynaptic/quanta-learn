#py3
import numpy as np
import copy
import time
import logging



logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filemode='a')

grid = [
    [0, 6, 3, float('inf'), float('inf'), float('inf')],
    [6, 0, 2, 5, float('inf'), float('inf')],
    [3, 2, 3, 0, 4, float('inf')],
    [float('inf'), 5, 3, 0, 2, 3],
    [float('inf'), float('inf'), 4, 2, 0, 5],
    [float('inf'), float('inf'), float('inf'), 3, 5, 0]
]


def dijkstra():
    '''
    dijkstra算法，算法复杂度为O(n^2)。
    用于计算单元最短路径的方法，该算法要求图中不存在负权边。
    args:
        V: 全部点的集合
        S: 已经被检查最短路径点的结合
        min_path: 用于比较路径长度的hash table
        tail: 记录上一次存入集合S中的点，作为下一次搜索的起点
    '''
    V = [i for i in range(6)]
    S = []
    S.append(0)
    V.remove(0)
    min_path = {'0': 0}
    tail = 0

    while len(S) < 6:
        logging.info("BEGIN search: set S: {}, set V: {}".format(S, V))
        new_path = copy.deepcopy(min_path)
        for path in min_path.keys():
            start = int(path.split('>')[-1])
            if start == tail:
                for node in V:
                    new_path[str(path)+ '->' +str(node)] = min_path[path] + grid[start][node]          
                    new_path[path] = float('inf')

        
        global_optimize_path = sorted(new_path.items(), key=lambda new_path:new_path[1])[0][0]
        tail = int(global_optimize_path.split('>')[-1])
        S.append(tail)
        V.remove(tail)
        logging.info('choose path {}, add new node-{} to S'.format(global_optimize_path, tail))
        
        min_path = copy.deepcopy(new_path)


dijkstra()




#其中矩阵p是邻接矩阵，而矩阵path记录u,v两点之间最短路径所必须经过的点
p = [
    [0, 5, float('inf'), 7],
    [float('inf'), 0, 4, 2],
    [3, 3, 0, 2],
    [float('inf'), float('inf'), 1, 0]
]

path = [
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1]
]

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
    n_nodes = len(p)

    for k in range(n_nodes):
        for i in range(len(p)):
            for j in range(len(p[0])):
                if i == j or k == i or k == j:
                    pass
                else:
                    if p[i][j] > p[i][k] + p[k][i]:
                        p[i][j] = p[i][k] + p[k][i]
                        path[i][j] = k
    
    logging.info('distance matrix:')
    for x in p: print(x)
    logging.info('path matrix')
    for x in path: print(x)

Floyd()