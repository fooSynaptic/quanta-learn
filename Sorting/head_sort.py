# encoding=utf-8
# /usr/bin/python3
import time



def heap_sort(arr):
    def _heap(i, field):
        if field == 'left':
            return 2*i
        elif field == 'right':
            return 2*i+1
        elif field == 'father':
            return i//2

    def heapify(arr, n, i):
        top = arr[i]

        while i*2+1 < n:
            min_pos = i*2+1
            if min_pos + 1 < n and arr[min_pos+1] > arr[min_pos]:
                min_pos += 1
            if arr[min_pos] > top:
                arr[i] = arr[min_pos]
                i = min_pos
            else:
                break
            print(arr)
            time.sleep(1)
        arr[i] = top

    ### build heap
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        print(i)
        heapify(arr, n, i)
    print("initialized heap: ", arr)

    ### sort
    ## swap the item in the pos of 0 and the tail
    for j in range(n-1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0)


    return arr


from random import randint

print('res: ', heap_sort([randint(1, 100) for _ in range(10)]))

