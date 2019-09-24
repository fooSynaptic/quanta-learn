#py3

def select_sort(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    return nums


def testcase():
    arr = [6, 3,5,4,1,7,9,2]
    print(select_sort(arr))

testcase()