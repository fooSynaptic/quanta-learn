# encoding=utf-8
# /usr/bin/python3
from time import time


def fastPower(n, k):
    """fast power"""
    if k == 1:
        return n
    if k %2 == 0:
        return fastPower(n, k//2) ** 2
    elif k%2 == 1:
        return n*fastPower(n, k//2)**2




def brutePower(n, k):
    """brute force"""
    if k == 1:
        return n
    return n*brutePower(n, k-1)


s = time()
print(fastPower(3, 500), time()- s)

s = time()
print(brutePower(3, 500), time()- s)