import random
from functools import wraps
from threading import Thread

from time import time


def fastsort(arr, l, r):
    def partition(l, r):
        key = arr[r]
        i = l-1

        for j in range(l, r):
            if arr[j] <= key:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[r], arr[i+1] = arr[i+1], arr[r]
        return i+1

    if l<r:
        p = partition(l, r)
        fastsort(arr, l, p-1)
        fastsort(arr, p+1, r)


def mergeSort(arr):
    def _merge(s1, s2):
        res = []
        while s1 and s2:
            if s1[0] > s2[0]:
                res.append(s2.pop(0))
            else:
                res.append(s1.pop(0))

        res.extend((s1 if s1 else s2))
        return res


    if len(arr) == 1: return arr[:]
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return _merge(left, right)



def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if not arr[i] <= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(i,j,arr)

    return arr




def record_time(func):
    """自定义装饰函数的装饰器"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('{}: {}秒'.format(func.__name__, time() - start))
        return result
        
    return wrapper

def main():
    import copy
    arr = [6, 3,5,4,1,7,9,2,6,4,8,9,1,3,5,7,9,2,3]
    record_time(fastsort)(copy.deepcopy(arr), 0, len(arr)-1)
    print(arr)
    
    res = record_time(mergeSort)(copy.deepcopy(arr))
    print(res)

    print("BUBBLE SORT...")
    res = record_time(bubbleSort)([random.randint(0, 10) for _ in range(10)])
    print(res)


    

main()