import random
import time


nums = []
for _ in range(5000000):
    nums.append(random.randint(0, 150))


def bucket_sort(nums):
    buckets = {}

    for num in nums:
        if not num in buckets:
            buckets[num] = 1
        else:
            buckets[num] += 1
    
    res = []
    for idx in sorted(buckets.keys()):
        res += [idx] * buckets[idx]
    
    return res

s = time.time()
ans = bucket_sort(nums)
print('time eclapse:', time.time()-s)
print(all([ans[i+1] - ans[i] >=0 for i in range(len(ans) - 1)]))
print(ans[:10], ans[-10:], len(ans))