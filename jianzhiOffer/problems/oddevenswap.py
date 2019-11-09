# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        print(array)
        n = len(array)
        pre = -1
        
        for i in range(n):
            if array[i]%2 == 1:
                pre += 1
                array[i], array[pre] = array[pre], array[i]
                for j in range(i-1, pre+1, -1):
                    if array[j]< array[j-1]:
                        array[j], array[j-1] = array[j-1], array[j]
            print(pre, array)

        for k in range(n-1, pre+1, -1):
            if array[k]< array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]

        return array


ans = Solution()

print(ans.reOrderArray([i for i in range(1, 20)]))