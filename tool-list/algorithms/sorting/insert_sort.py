"""插入排序：用下标 0 作哨兵存放待插入值，向左移动较大元素腾位。"""

from random import randint

n = 20
arr = [randint(1, 100) for _ in range(n)]
# 下标 0 留作哨兵，实际数据从下标 1 开始
arr = [0] + arr

print(arr[1:])

for i in range(2, n + 1):
    if arr[i] < arr[i - 1]:
        arr[0] = arr[i]
        j = i - 1
        # 把比哨兵大的元素逐个右移，直到找到插入位置
        while arr[0] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = arr[0]

print(arr[1:])
