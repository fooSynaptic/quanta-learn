#py3

def fast_sort(nums, start, end):
    #divide
    def partition(arr, l, r):
        #print(arr, r)
        key = arr[r]
        s = l - 1

        for i in range(l, r):
            if arr[i] <= key:
                s += 1
                arr[s], arr[i] = arr[i], arr[s]
        
        arr[s+1], arr[r] = arr[r], arr[s+1]
        return s+1
    
    if start < end:
        part = partition(nums, start, end)
        fast_sort(nums, start, part-1)
        fast_sort(nums, part+1, end)
    #return nums


def quicksort(arr, p, r):
        if p < r:
                q = my_PARTITION(arr, p, r)
                quicksort(arr, p, q-1)
                quicksort(arr, q+1, r)



def my_PARTITION(arr, p, r):
        #set `x` as metric
        x = arr[r]
        i = p-1

        for j in range(p, r):
                #if arr[j] smaller than metric, swap j to left, which is the region smaller than metric
                if arr[j] <= x:
                        i = i + 1
                        arr[i], arr[j] = arr[j], arr[i]
        #swap the metric with index of i, which is the greatest one
        arr[r], arr[i+1] = arr[i+1], arr[r]

        return i+1



def testcase():
    arr = [6, 3,5,4,1,7,9,2,6,4,8,9,1,3,5,7,9,2,3]
    #arr = [2,8,7,1,3,5,6,4]
    fast_sort(arr, 0, len(arr)-1)
    print(arr)


testcase()


