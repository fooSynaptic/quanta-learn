#py3


import random

arr = [random.randint(0,50) for i in range(100)]

print(arr[len(arr)//2])

def findmid(arr):
    fast, slow = 0, 0
    while fast < len(arr):
        slow += 1
        fast += 2
    #print(slow ,fast)
    return arr[slow]
    

print("res:",findmid(arr))