# encoding = utf-8
# /usr/bin/python3


def get_k_top_partition(left, right, k):
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
		return get_k_top_partition(left, p-1, k)
	elif largestBound < k-1:
		return get_k_top_partition(p, right, k-largestBound)






def get_k_top_minHeap(nums, k):
	def heapify(i, n):
		top = nums[i]
		while 2*i+1 < n:
			minPos = 2*i+1
			if minPos+1<n and nums[minPos+1]<nums[minPos]:
				minPos += 1
			if nums[minPos] < top:
				nums[i] = nums[minPos]
				i = minPos
			else:
				break
		nums[i] = top

	n = len(nums)
	# initialize minHeap with size k
	for i in range(k//2-1, -1, -1):
		heapify(i, k)


	for j in range(n-1, k-2, -1):
		if nums[j] < nums[0]:
			pass
		else:
			nums[j], nums[0] = nums[0], nums[j]
			heapify(0, k)
	
	return nums[0]



def get_k_top_maxHeap(nums, k):
	def heapify(i, n):
		top = nums[i]
		while 2*i+1 < n:
			maxPos = 2*i+1
			if maxPos + 1 < n and nums[maxPos+1] > nums[maxPos]:
				maxPos += 1

			if nums[maxPos] > top:
				nums[i] = nums[maxPos]
				i = maxPos
			else:
				break

		nums[i] = top

	n = len(nums)
	tgt = n-k+1
	for i in range(tgt//2-1, -1, -1):
		heapify(i, tgt)

	for j in range(n-1, tgt, -1):
		if nums[j] > nums[0]:
			pass
		else:
			nums[0], nums[j] = nums[j], nums[0]
			heapify(0, tgt)

	return nums[0]





def testcase():
	import random
	global nums
	nums = [i for i in range(100)]
	random.shuffle(nums)

	ans1 = get_k_top_partition(0, 99, 100-(10-1)+1)
	print("ans1", ans1)

	random.shuffle(nums)
	ans2 = get_k_top_minHeap(nums, 10)
	print("ans2", ans2)

	random.shuffle(nums)
	ans3 = get_k_top_maxHeap(nums, 10)
	print("ans3", ans3)
	

testcase()
