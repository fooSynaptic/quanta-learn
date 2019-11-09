# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        '''
        1 2 3 4 
        5 6 7 8 
        9 10 11 12 
        13 14 15 16
        '''
        def transpose(m):
            if m == []: return m
            r, c = len(m), len(m[0])
            return [[m[i][j] for i in range(r)] for j in range(c-1, -1, -1)]
        
        
        
        ans = []
        
        while matrix != []:
            ans.extend(matrix.pop(0))
            matrix = transpose(matrix)

            
        return ans


def testcase():
    arr = [[1]]
    ans = Solution()
    res = ans.printMatrix(arr)

    print(res)


testcase()