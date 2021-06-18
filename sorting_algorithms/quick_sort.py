
# quick sort takes in Average case O(nlogn)
# but in worst case it take O(n^2)
# however, it is an in-place algorithm which is based on the
# divide and conquer method.

# the worst case however, is almost always avoided by using
# the "Randomized" version of it. QS is very practical sorting algorithm
# and in most cases that's what standard libs of programming languages are using
# to implement sorting (i.e in Java)

# the QS algorithm makes use of recursively partitioning the array
# into two array to the left and right
# in case they are less or greater than a chosen pivot element.

# once we have partitioned the array like this now we need to sort
# the array to the left and the one to the right. And this time, unlike
# merge_sort() we don't need to create auxiliary arrays, so we have to keep
# track of the start and end index

def partition(arr, start, end):
    # will rearrange the array such that there will be a pivot
    # and there will be elements less than the pivot on the left
    # and elements greater than the pivot on the right
    # this function will return the index of the pivot after rearrangement

    # left => less than the pivot
    # right => greater than the pivot
    pivot = arr[end]
    partition_idx = start

    for i in range(start, end):
        if arr[i] <= pivot:
            # swap arr[i] with arr[partion_idx]
            # and then we increment the partion_idx
            arr[i], arr[partition_idx] = arr[partition_idx], arr[i]
            partition_idx = partition_idx + 1

    arr[partition_idx], arr[end] = arr[end], arr[partition_idx]
    return partition_idx


def quick_sort(arr, start, end):
    # base condition: if we only have 1 element => its already sorted
    # (or if the segment is invalid, hence <)
    if start < end:
        partition_idx = partition(arr, start, end)
        # now we make the recursive calls
        quick_sort(arr, start, partition_idx - 1)
        quick_sort(arr, partition_idx + 1, end)


if __name__ == '__main__':
    a = [10, 30, 1, 5, 100, 3]
    print("Unsorted Array:")
    print(a)

    quick_sort(a, 0, 5)

    print("Sorted Array:")
    print(a)
