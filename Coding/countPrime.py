#py3

class Solution:
    def __init__(self):
        self.prList = [2, 3]
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2

        for num in range(5, n, 2):
            if self.isPrimes(num):
                self.prList.append(num)
                    
        return len(self.prList)
                    
        
    def isPrimes(self, n):
        '''
        use prime got to make judge
        '''
        max1 = pow(n, 0.5)
        for div in self.prList:
            if div > max1:
                break
            if n % div == 0:
                return False
        return True


class Solution2:
    def __init__(self):
        self.priList = [2, 3]
    
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        
        def _isPrime(num):
            max1 = pow(num, 0.5)
            for i in self.priList:
                if i > max1:
                    break
                if not num%i: return False
            return True
        
        for num in range(5, n, 2):
            if _isPrime(num):
                self.priList.append(num)
        
        #print(self.handler[n-1])
        return len(self.priList)


import time



class Solution3:
    def __init__(self):
        self.priList = [2, 3, 5]
    
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        elif n <= 6:
            return 3
        
        def _isPrime(num):
            if num%6 == 5 or num%6 == 1:
                return True
            return False
        
        for num in range(7, n):
            if _isPrime(num):
                self.priList.append(num)
        
        #print(self.handler[n-1])
        print(self.priList)
        return len(self.priList)




def testSolution(input, solution):
    s = time.time()
    ans = solution()
    print(ans.countPrimes(input))
    print(time.time() - s)

#testSolution(1500000, Solution)
#testSolution(1500000, Solution2)
testSolution(100, Solution3)
