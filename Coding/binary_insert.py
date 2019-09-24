#py3
import random



def binary_insert(s, e, tgt):
    while s<=e:
        if s == e:
            if vec[s] >= tgt:
                vec.insert(s, tgt)
            else:
                vec.insert(s+1, tgt)
            return 
        if e-s == 1 and (vec[e] > tgt and vec[s] < tgt):
            vec.insert(s+1, tgt)
            return

        mid = (s+e)//2
        print(vec[s:e+1], s,e ,mid)
        if vec[mid] > tgt:
            e = mid-1
        elif vec[mid] < tgt:
            s = mid + 1
            if vec[s] < tgt:
                pass
            else:
                vec.insert(s, tgt)
                return
        else:
            vec.insert(mid, tgt)
            return
    return

vec = [1, 5, 6, 10, 11, 11, 12, 13, 15, 17]
#seq = [random.randint(0,100) for _ in range(100)]
seq = [14]
for i in seq:
    print('input:', i)
    if not vec:
        vec.insert(0,i)
    elif i >= vec[-1]:
        vec.append(i)
    elif i <= vec[0]:
        vec.insert(0, i)
    else:
        binary_insert(0,len(vec)-1, i)
    print('res:', vec)
    if not all([vec[i+1]-vec[i]>=0 for i in range(len(vec)-1)]):
        pass


print(all([vec[i+1]-vec[i]>=0 for i in range(len(vec)-1)]))


import time


arr = [random.randint(1, 10000) for _ in range(10000)]
def timer(f, input):
    def rf():
        s = time.time()
        f(input)
        print('eclaspe:', time.time()-s)
    return rf


def f1(input):
    return arr.insert(9005, input)

def f2(input):
    return arr[:9005] + [input] + arr[9005:]

timer(f1, 795)()
timer(f2, 795)()