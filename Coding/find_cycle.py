#py3

class node():
    def __init__(self, val):
        self.val = val
        self.next = None


def f(x):
    if x:
        return x.next


def brent(f, x0):
    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        #print(power, lam)
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length λ
    mu = 0
    tortoise = hare = x0
    for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare)
    # The distance between the hare and tortoise is now λ.

    # Next, the hare and tortoise move at same speed until they agree
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
 
    return lam, mu



def buildList(s):
    head = node(s[0])
    curr = head

    for x in s[1:]:
        curr.next = node(x)
        curr = curr.next
    return head


def testcase(s = [1,2,3,4,5,2,7,8]):
    head = buildList(s)
    print(brent(f, head))


testcase()