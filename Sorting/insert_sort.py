# !/bin/bash/python3

from random import randint

n = 20
arr = [randint(1, 100) for _ in range(n)]
arr = [0] + arr

print(arr[1:])
i, j = 0, 0

for i in range(2, n+1):
    if arr[i] < arr[i-1]:
        arr[0] = arr[i]
        j = i-1
        while arr[0] < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = arr[0]

print(arr[1:])

