"""原地堆排序（升序），基于二叉最大堆。

参考：https://www.cnblogs.com/chengxiao/p/6129630.html
"""

from random import randint


def heap_sort(arr):
    def heapify(arr, n, i):
        """对节点 i 做下沉，使大小为 n 的子树重新满足最大堆性质。"""
        top = arr[i]
        while i * 2 + 1 < n:
            largest = i * 2 + 1
            if largest + 1 < n and arr[largest + 1] > arr[largest]:
                largest += 1
            if arr[largest] > top:
                arr[i] = arr[largest]
                i = largest
            else:
                break
        arr[i] = top

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0)

    return arr


def demo():
    print("res:", heap_sort([randint(1, 100) for _ in range(10)]))


if __name__ == "__main__":
    demo()
