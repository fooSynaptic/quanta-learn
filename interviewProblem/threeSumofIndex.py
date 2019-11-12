# encoding = utf-8
# /usr/bin/python3

"""
Given array s, return the minest index sum of three element, which their sum is K.
"""

def threeSumofIndex(nums, k):
    if len(nums) < 3: return -1
    
    ans = float("inf")
    n = len(nums)

    for i in range(n-2):
        d, tgt = dict(), k - nums[i]
        if not tgt >= 0: 
            continue
        
        for j in range(i+1, n):
            if nums[j] in d:
                ans = min(ans, i+j+d[nums[j]])
            else:
                d[tgt-nums[j]] = j

    return ans



def testcase():
    from random import randint
    nums = [randint(1, 100) for i in range(100)]
    res = threeSumofIndex(nums, 15)

    print(res)


if __name__ == "__main__":
    testcase()

    

