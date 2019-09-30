# encoding = utf-8
# /usr/bin/python3

from random import randint

'''
Problem: given three circles with the centers o and the radius r, compute their area, 
        keep 6 decimals, the metric of o and r can be arbitrary number.
'''
"""We decide the use Monter carol simulation to deduct the area of three circles.
    While the problem tell you to keep the decimal, it's more likely to be a simulation 
    problem rather than a mathmatic solution.
"""


def withIncircle(center, r,  point):
    """
    Given a circle and a new point, return whether this point in this circles.
    """
    x0, y0 = center
    p1, p2 = point

    return pow((x0-p1)**2 + (y0-p2)**2, 0.5) <= r



def AreaofCircle():
    #define three circles
    c1, c2, c3 = (0.01*randint(100, 10000), 0.01*randint(100, 10000)), \
        (0.01*randint(100, 10000), 0.01*randint(100, 10000)), \
            (0.01*randint(100, 10000), 0.01*randint(100, 10000))
    
    r1, r2, r3 = 0.01*randint(100, 1000), 0.01*randint(100, 1000), 0.01*randint(100, 1000)

    #increase the simulate times when efficient number cannot satisfy
    simSet = []
    for _ in range(10000):
        simSet.append(
            ## we simulate the point in the range of (1, 150) * (1, 150)
            (0.01*randint(1, 15000), 0.01*randint(1, 15000))
        )

    ### compute the total sim area N
    N = 149 * 149

    ### compute the probability of sim point drop into the three circles
    posInstance = 0
    for i in range(len(simSet)):
        if withIncircle(c1, r1, simSet[i]) or withIncircle(c1, r1, simSet[i]) or withIncircle(c1, r1, simSet[i]):
            posInstance += 1

    Prob = posInstance/len(simSet)


    ### return simulation area
    return N * Prob



print('Area 1:', AreaofCircle())
print('Area 2:', AreaofCircle())
print('Area 3:', AreaofCircle())