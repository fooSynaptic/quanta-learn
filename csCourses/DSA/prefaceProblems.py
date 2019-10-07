# encoding = utf-8
# /usr/bin/python3


"""Max2 iteration 1"""
def Max2(nums, lo, hi):
    """
    return the larggest two items index in array nums x1 and x2
    """
    x1, x2 = 0, 0

    for i in range(lo, hi):
        if nums[i] > nums[x1]:
            x1 = i
    
    for l in range(x1, -1, -1):
        if nums[l] > nums[x2]:
            x2 = l

    for r in range(x1, hi):
        if nums[r] > nums[x2]:
            x2 = r
    
    return x1, x2


"""
Max2 iteration 2
"""
def twoLarggest(nums, lo, hi):
    """
    return the larggest two items index in array nums x1 and x2
    """
    x1, x2 = (0 if nums[0]>nums[1] else 1), (1 if nums[0]>nums[1] else 0)

    for i in range(2, hi):
        if nums[i] <= nums[x2]:
            pass
        else:
            if nums[i] > nums[x1]:
                x1 = i
                x2 = x1
            else:
                x2 = i
    
    return x1, x2


"""
Max2 divide and recursion
"""
def twoLarggest_3th(nums, lo, hi):
    if hi-lo == 1:
        return (lo, hi if nums[lo]>nums[hi] else hi, lo)
    
    mid = (lo+hi)//2
    fstLeft, secLeft = twoLarggest_3th(nums, lo, mid)
    fstRight, secRight = twoLarggest_3th(nums, mid, hi)

    if nums[fstLeft] == nums[fstRight]:
        x1, x2 = fstLeft, fstRight
    elif nums[fstLeft] > nums[fstRight]:
        x1 = fstLeft
        x2 = (secLeft if nums[secLeft] >= nums[fstRight] else fstRight)
    else:
        x1 = fstRight
        x2 = (secRight if nums[secRight] >= nums[fstLeft] else fstLeft)
    
    return x1, x2