#3n+1 find 1

import random
from functools import wraps
from threading import Thread

from time import time

arr = [random.randint(1000001, 1000010)]
for x in [[i] * 3 for i in range(100000)]:
    arr += x
random.shuffle(arr)


def find_one(arr):
    for x in arr:
        if arr.count(x) == 1:
             return x

def dict_one(arr):
    d = {}
    for x in arr:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in d:
        if d[x] == 1:
            return x




def record_time(func):
    """自定义装饰函数的装饰器"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('{}: {}秒'.format(func.__name__, time() - start))
        return result
        
    return wrapper

#print(record_time(find_one)(arr))
#print(record_time(dict_one)(arr))


def main():
    find1 = Thread(target = record_time(find_one), args=(arr,))
    find1.start()
    
    find2 = Thread(target = record_time(dict_one), args=(arr,))
    find2.start()

    find1.join()
    find2.join()
main()