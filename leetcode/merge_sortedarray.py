#py3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        res = []
        tmp = -1

        for i in range(min([m,n])):
            tmp_insert = min(nums1[i], nums2[i])
            tmp_large = max(nums1[i], nums2[i])
            if tmp_insert > tmp:
                res.extend([tmp_insert, tmp_large])
                tmp = tmp_large
                print(res)
            elif tmp_insert <= tmp:
                tmp_sort = sorted([tmp_insert, tmp_large, tmp])
                res = res[:-1] + tmp_sort
                tmp = tmp_sort[-1]
                print(res)
           
        
        return res

ans = Solution()



# in place solution
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        
        res = []
        tmp = -1

        for i in range(min([m,n])):
            tmp_insert = min(nums1[i], nums2[i])
            tmp_large = max(nums1[i], nums2[i])
            if tmp_insert > tmp:
                res.extend([tmp_insert, tmp_large])
                tmp = tmp_large
            elif tmp_insert <= tmp:
                tmp_sort = sorted([tmp_insert, tmp_large, tmp])
                res = res[:-1] + tmp_sort
                tmp = tmp_sort[-1]        
        return res
        """
        nums2 = sorted(nums2)
        def _reverse_insert(arr, num):
            if arr[-1] == 0:
                arr[-1] = num
            elif arr[-1] < num:
                min_tmp = arr[-1]
                arr[-1] = num
                for i in range(len(nums2), len(nums1)):
                    if arr[i] == 0:
                        arr[i] = min_tmp
                        break

        tmp = 0
        for i in range(n):
            max1 = max(nums1)
            print(nums2[i])
            if nums2[i] > max1:
                print(nums1, nums2[i])
                _reverse_insert(nums1, nums2[i])
                print(nums1)
            else:
                nums1[nums1.index(max1)] = nums2[i]
                print(nums1, max1)
                _reverse_insert(nums1, max1)
                print(nums1)
                
        return nums1


ans2 = Solution2()
print(ans2.merge([1,2,3,0,0,0],
3,
[2,5,6],
3))