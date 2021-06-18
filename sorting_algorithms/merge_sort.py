import numpy as np


# merge sort -> not an in-place algorithm => it has
# O(n) -> space complexity

# the function responsible for the combine step
# the simplest case is comparing elements from both arrrays and
# then according to which is smaller we place it on the parent array
def merge(left, right, arr):
    len_left = len(left)
    len_right = len(right)
    len_arr = len(arr)
    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len_left:
        arr[k] = left[i]
        k = k + 1
        i = i + 1

    while j < len_right:
        arr[k] = right[j]
        k = k + 1
        j = j + 1


# in this part, we do the DIVIDE and CONQUER steps
# here we call the upper function recursively on the subarrays
def merge_sort(arr):
    len_arr = len(arr)

    # base case,when we have only 1 element => already sorted
    if len_arr < 2:
        return

    # otherwise we construct subarrays by dividing the main array
    # in the middle
    mid = len_arr // 2
    left = []
    right = []

    # now we populate these subarrays
    for i in range(0, mid):
        left.append(arr[i])

    for i in range(mid, len_arr):
        right.append(arr[i])

    # now we make a recusive call to sort the left sublist
    # and once we're done with that, we make a recursive call
    # to merge the right sublist
    merge_sort(left)
    merge_sort(right)
    # finally, we combine both arrays together by calling merge()
    merge(left, right, arr)


if __name__ == '__main__':
    a = np.array([10, 30, 1, 5, 100, 3])
    print("Unsorted Array:")
    print(a)

    merge_sort(a)

    print("Sorted Array:")
    print(a)
