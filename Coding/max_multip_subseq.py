import numpy as np


def max_subMutiplier(arr):
    maxCurrent, minCurrent = 1, 1
    maxProduct, minProduct = 1, 1

    for num in arr:
        if num < 0:
            maxCurrent, minCurrent = minCurrent, maxCurrent
        else:
            maxCurrent *= num
            minCurrent *= num

            if maxCurrent < 1: maxCurrent = 1
            if minCurrent < 1: minCurrent = 1
            maxProduct, minProduct = max(maxProduct, maxCurrent, minCurrent),\
                min(maxCurrent, minCurrent)

    return maxProduct

nums = [-2.5,4,0,3,0.5,8,-1]
print(max_subMutiplier(nums))




def func2(arr):
    n = len(arr)
    maxarr, minarr = [arr[0]], [arr[0]]
    value = maxarr[0]

    for i in range(1, n):
        maxarr.append(max(max(arr[i], maxarr[i-1]*arr[i]), minarr[i-1]*arr[i]))
        minarr.append(min(min(arr[i], maxarr[i-1]*arr[i]), minarr[i-1]*arr[i]))
        value = max(value, maxarr[i])

    return value

print(func2(nums))

def edit_dis(src, tgt):
    #i, j  = len(src), len(tgt)
    f = np.zeros([len(src), len(tgt)])
    #f[0][0] = 1

    for i in range(1, len(src)):
        for j in range(1, len(tgt)):
            f[i][j] = min(f[i-1, j]+1, f[i, j-1]+1, f[i-1, j-1]+(0 if src[i]==tgt[j] else 1)) 
    print(f)

edit_dis('abc a', 'ab ca')
edit_dis('abca', 'abca')