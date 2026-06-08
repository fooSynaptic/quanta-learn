"""快速排序（Lomuto 分区），含两份等价实现。"""


def fast_sort(nums, start, end):
    def partition(arr, l, r):
        # 以 arr[r] 为基准，s 之前是不大于基准的区域
        key = arr[r]
        s = l - 1

        for i in range(l, r):
            if arr[i] <= key:
                s += 1
                arr[s], arr[i] = arr[i], arr[s]

        arr[s + 1], arr[r] = arr[r], arr[s + 1]
        return s + 1

    if start < end:
        part = partition(nums, start, end)
        fast_sort(nums, start, part - 1)
        fast_sort(nums, part + 1, end)


def quicksort(arr, p, r):
    if p < r:
        q = my_PARTITION(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def my_PARTITION(arr, p, r):
    # 以末尾元素为基准；i 始终指向不大于基准区域的末位
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    # 把基准换到 i+1，使其左小右大
    arr[r], arr[i + 1] = arr[i + 1], arr[r]

    return i + 1


def testcase():
    arr = [6, 3, 5, 4, 1, 7, 9, 2, 6, 4, 8, 9, 1, 3, 5, 7, 9, 2, 3]
    fast_sort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    testcase()
