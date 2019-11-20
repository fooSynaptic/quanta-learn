# encoding = utf-8
# /usr/bin/python3




def get_k_top(left, right, k):
	print(left, right, k)
	def partition(left, right):
		key = nums[right]
		j = left-1

		for i in range(left, right):
			if nums[i] <= key:
				j += 1
				nums[i], nums[j] = nums[j], nums[i]

		nums[j+1], nums[right] = nums[right], nums[j+1]
		return j+1


	p = partition(left, right)
	largestBound = p - left
	if largestBound == k-1: return nums[p]
	elif largestBound > k-1:
		return get_k_top(left, p-1, k)
	elif largestBound < k-1:
		return get_k_top(p, right, k-largestBound)


def testcase():
	import random
	global nums
	nums = [i for i in range(100)]
	random.shuffle(nums)

	ans = get_k_top(0, 99, 10)
	print(ans)


testcase()
