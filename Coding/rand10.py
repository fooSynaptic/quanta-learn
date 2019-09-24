#py3

import random
from collections import Counter


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
#1-7
#1-3
#2-10
def combine(s1, s2):
    res = []
    for i in range(s1[0], s1[1]):
        for j in range(s2[0], s2[1]):
            res.append(i+j)
    return Counter(res)


rand7 = random.randint

class Solution:
    def randTen(self):
        """
        :rtype: int
        """
        return rand7(1, 7) + self.randthree()-1
    
    def randthree(self):
        #1,2,3
        num = 0
        while not num:
            num = rand7(1, 7)//2
            
        return num
        

ans = Solution()
print(Counter([ans.randTen() for _ in range(1000)]))