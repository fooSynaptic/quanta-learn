

def lower_Bound(arr, val):
    if val < arr[0]: return val
    if val > arr[-1]: return arr[-1]
    l, r = 0, len(arr)-1

    while l < r:
        mid = (l+r)//2
        if arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1

    return arr[l] if arr[l] <= val else arr[l-1]





for w in [4,5,6,7,8]:
    print(lower_Bound([2,4,6,8,10], w))


print(lower_Bound([2,3,5,112, 120], 113))
