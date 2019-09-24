
def mergesort(nums):
    if len(nums) == 1: return nums[:]
    mid = len(nums)//2

    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)


def merge(nums1, nums2):
    l1, l2 = len(nums1), len(nums2)
    res = []

    while nums1 and nums2:
        if nums1[0]<=nums2[0]:
            res.append(nums1.pop(0))
        else:
            res.append(nums2.pop(0))
    res += (nums1 if nums1 else nums2)

    return res

def testcase():
    arr = [3,5,4,1,7,9,2]
    print(select_sort(arr))


testcase()