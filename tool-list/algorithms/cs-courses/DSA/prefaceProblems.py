"""《数据结构》开篇问题：求数组中最大的两个元素下标的三种实现。"""


def Max2(nums, lo, hi):
    """迭代版一：先扫出最大值下标 x1，再在两侧找次大值下标 x2。"""
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


def twoLarggest(nums, lo, hi):
    """迭代版二：一趟扫描同时维护最大 x1 与次大 x2。"""
    x1, x2 = (0 if nums[0] > nums[1] else 1), (1 if nums[0] > nums[1] else 0)

    for i in range(2, hi):
        if nums[i] <= nums[x2]:
            pass
        else:
            if nums[i] > nums[x1]:
                x2 = x1
                x1 = i
            else:
                x2 = i

    return x1, x2


def twoLarggest_3th(nums, lo, hi):
    """分治版：左右各求出最大/次大，再合并比较。"""
    if hi - lo == 2:
        return (lo, lo + 1) if nums[lo] >= nums[lo + 1] else (lo + 1, lo)

    mid = (lo + hi) // 2
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
