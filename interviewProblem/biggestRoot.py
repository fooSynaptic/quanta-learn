# encoding=utf-8
# /usr/bin/python3

"""
Given list with parent child pair, return the root of biggest linkset.
"""

### solution1 unfion find
def biggestRoot(pairs):
    def getParent(a, block):
        if not a == block[a]:
            block[a] = getParent(block[a], block)
        return block[a]


    nodes = set()
    for i, j in pairs: nodes.update([i, j])

    node2block = dict()
    block2node = dict()
    n = len(nodes)
    for i, val in enumerate(nodes):
        node2block[val] = i
        block2node[i] = val

    blocks = [i for i in range(n)]

    ## connect
    for i, j in pairs:
        mapI, mapJ = node2block[i], node2block[j]
        bParrent, bChild = getParent(mapI, blocks), getParent(mapJ, blocks)
        if not bParrent == bChild:
            blocks[mapJ] = bParrent

    Roots = dict()
    for i in  range(n):
        root = getParent(i, blocks)
        Roots[root] = Roots.get(root, 0) + 1

    ans = sorted(Roots.items(), key=lambda x:x[1])[-1][0]
    return block2node[ans]









def testcase():
    p = [(1, 3), (1, 4), (3, 5), (5, 2), (20, 100), (100, 101), [100, 102], [100, 103], [100, 105]]
    res = biggestRoot(p)

    print(res)



if __name__ == "__main__":
    testcase()


    

    
