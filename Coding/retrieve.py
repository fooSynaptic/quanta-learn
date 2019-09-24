import time

candidate = ['ab', 'cd', 'efg', '123', 'fgt', 'sadasfsaf']

while len(candidate) > 1:
    head, tail = candidate.pop(0), candidate.pop(0)
    candidate = [[a+b for a in head for b in tail]] + candidate


    



