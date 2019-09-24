#py3

def bubble_sort(nums):
    ops = 0
    while not all([nums[i]<=nums[i+1] for i in range(len(nums)-1)]):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                ops += 1
    return nums, ops

def fine_bubble_sort(nums):
    ops = 0
    for i in range(len(nums)-1):
        swap = False
        for j in range(i+1, len(nums)):
            if not nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                ops += 1
                swap = True
        if swap:
            swap = False
            for j in range(len(nums)-1, i, -1):
                if not nums[i] <= nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    ops += 1
                    swap = True

    return nums, ops


def testcase():
    arr = [6, 3,5,4,1,7,9,2,6,4,8,9,1,3,5,7,9,2,3]
    print(bubble_sort(arr))






arr = [1,2,3,-1,-2,4,5,-3,6,7,-4,8]
#print(arr)

def signed_arr(nums):
    l, r = 0, len(nums)-1
    for i in range(len(nums)):
        if nums[i] < 0:
            negative_first = nums[i]
            break

    while nums[r]<0:
        r-=1
    while l < r:
        if nums[l] < 0:
            print(l, r, nums)
            nums[:] = nums[:l] + nums[l+1:r] + [nums[l]] + nums[r:]
            print('after', nums)
            for i in range(len(nums)):
                if nums[i] < 0 and not nums[i] == negative_first:
                    l = i
                else:
                    break
        
        

    return nums
    


print(signed_arr(arr))


def evaluate(nums):
    if not all([(nums[i] - nums[i+1])*nums[i] < 0 for i in range(len(nums)-1) if nums[i]*nums[i+1]>0]):
        return False
    return True

def multiple_testcase():
    n = [5, 20, 30, 50]
    for i in n:
        test_arr = []     
        for j in range(1, i+1):
            test_arr.append(j)
            test_arr.append(-j)
        
        print(evaluate(signed_arr(test_arr)))
        print(test_arr)

#multiple_testcase()
