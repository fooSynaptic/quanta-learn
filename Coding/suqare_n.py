# encoding = utf-8
# /usr/bin/python3


def square(n, err = 0.000001):
    l, r = 1, n

    while True:
        pred = (l+r)/2
        if abs(n - (pred * pred)) < err:
            return pred
        if pred * pred > n:
            r = pred
        elif pred * pred < n:
            l = pred
        else:
            return pred

    return pred


print([square(x) for x in range(1, 10)])
print([pow(x, 0.5) for x in range(1, 10)])
    
