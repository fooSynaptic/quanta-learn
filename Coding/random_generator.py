#py3

import random


#from random 3 to random 5


def base():
    return random.randint(1, 3)

def random5():
    val = 3*(base() - 1) + base() #random(1-9)
    if val > 5:
        return random5()
    else:
        return val

from collections import Counter

for _ in range(5):
    res = [random5() for _ in range(100000)]
print(Counter(res))