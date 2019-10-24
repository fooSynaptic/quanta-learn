# encoding = utf-8
# /usr/bin/python3
from random import randint
import random




def fastKlargest(left, right, k):
    """快速排序算法中的partition函数能够用来在n个数里面查找到第k大的数字"""
    def _partition(left, p):
        key = arr[p]
        pre = left-1
 
        for i in range(left, p):
            if arr[i] <= key:
                pre += 1
                arr[i], arr[pre] = arr[pre], arr[i]

        arr[pre+1], arr[p] = arr[p], arr[pre+1]
        return pre+1

    if left <= right:
        p = _partition(left, right)
        largestBound = p - left

        if largestBound == k-1: return arr[p]
        elif largestBound > k-1:
            return fastKlargest(left, p-1, k)
        elif largestBound < k-1:
            return fastKlargest(p, right, k-largestBound)




def heapKlargest():
    """维护size为k的最小堆"""
    def heapify(i, n):
        top = arr[i]

        while 2*i+1 < n:
            minPos = 2*i+1
            if minPos+1 < n and arr[minPos+1] < arr[minPos]:
                minPos += 1
            if arr[minPos] < top:
                arr[i] = arr[minPos]
                i = minPos
            else:
                break
        
        arr[i] = top



    for i in range(k//2-1, -1, -1):
        heapify(i, k)

    for j in range(len(arr)-1, k-2, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(0, k-1)

    print(arr, arr[k:])
    return arr[k:]








def testcase():
    #points = [(randint(-50, 50), randint(-50, 50)) for _ in range(100)]
    global arr, k
    arr = [randint(1, 1000) for _ in range(10)]
    k = randint(1, 50)
    k = 5
    '''
    klargest = fastKlargest(0, 99, k)
    assert klargest == sorted(arr)[k-1], "Test case not passed..."
    print("Passed...")
    '''
    print(sorted(arr)[:k][::-1])
    assert sorted(heapKlargest()) == sorted(arr)[:k], "Test case not passed..."
    print("Passed...")
    #print(heapKlargest(), sorted(arr)[:k])





if __name__ == '__main__':
    testcase()
    