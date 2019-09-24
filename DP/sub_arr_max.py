#python3

# 1 -2 3 5 -3 2

def sub_max(nums):
    overall, partial = {}, {}
    overall[0] = nums[0]
    partial[0] = nums[0]

    for i in range(1, len(nums)):
        partial[i] = max(partial[i-1]+nums[i], nums[i])
        overall[i] = max(partial[i], overall[i-1])
    return overall[len(nums)-1]

def testcase():
    #arr = [1, -2, 3, 5, -3, 2]
    arr = [0, -2, 3, 5, -1, 2]
    print(sub_max(arr))

testcase()


def record_time(func):
    """自定义装饰函数的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('{}: {}秒'.format(func.__name__, time() - start))
        return result
    return wrapper


from functools import wraps
from time import time


class Record():
    """自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper