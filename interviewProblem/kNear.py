# encoding = utf-8
# /usr/bin/python3
from random import randint


def nNear(points, k):
    def heapify(i, n):
        top = distances[i]
        
        while 2*i + 1 < n:
            minPos = 2*i + 1
            if minPos+1 < n and distances[minPos] > distances[minPos+1]:
                minPos += 1

            if distances[minPos] < top:
                distances[i] = distances[minPos]
                i = minPos
            else:
                break
        
        distances[i] = top


    distances = [(p[0]**2 + p[1]**2)**0.5 for p in points]
    n = len(distances)

    for i in range(n//2-1, -1, -1):
        heapify(i, n)


    ### sort
    ### swap the item in the pos of 0 and the tail
    for j in range(n-1, -1, -1):
        distances[0], distances[j] = distances[j], distances[0]
        heapify(0, j)


    return distances[-k:], distances[:-k]



def testcase():
    points = [(randint(-50, 50), randint(-50, 50)) for _ in range(100)]
    kleast, klargest = nNear(points, 10)
    #print(max(kleast), min(klargest))
    assert max(kleast) < min(klargest), "Test case not passed..."
    print("Passed...")





if __name__ == '__main__':
    testcase()