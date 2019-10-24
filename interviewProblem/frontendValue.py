# encoding = utf-8
# /usr/bin/python3
from itertools import permutations


def BeginEndValues(arr, values):
    k = len(values)
    n = len(arr)

    if not n >= k: return

    dp = [[0 for _ in range(n)] for _ in range(k)]
    dp[0][0], dp[0][n-1] = arr[0]*values[0], arr[n-1]*values[0]


    for i in range(1, k):
        f, e = 0, 0
        for j in range(n):
            if dp[i-1][j] > 0:
                fchoice = dp[i-1][j] 
                f = j+1
                #dp[i][j+1] = max(dp[i-1][j] + arr[j+1]*values[i], dp[i][j+1])
                break
        
        for k in range(n-1, -1, -1):
            if dp[i-1][k] > 0:
                echoice = dp[i-1][k]
                e = k-1
                #dp[i][k-1] = max(dp[i-1][k] + arr[k-1]*values[i], dp[i][k-1])
                break
        
        preMax = max(fchoice, echoice)
        dp[i][f] = max(dp[i][f], preMax + arr[f]*values[i])
        dp[i][e] = max(dp[i][e], preMax + arr[e]*values[i])


    for line in dp: print(line)



if __name__ == "__main__":
    arr = [5, 4, 9, 2, 3, 8, 1, 10, 6, 7]
    values = [10, 20, 15, 45]
    BeginEndValues(arr, values)

    ### check
    maxAns = 0
    candidates = set(permutations([0]*5+[1]*5, 5))
    for cand in candidates:
        tmp = arr[:]
        value = 0

        for c in range(len(values)):
            val = (tmp.pop() if cand[c] == 1 else tmp.pop(0))
            val *= values[c]
            value += val

        maxAns = max(maxAns, value)

    
    print(maxAns)



