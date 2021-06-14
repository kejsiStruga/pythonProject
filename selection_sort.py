import numpy as np


def print_array(arr):
    print(arr)


def selection_sort(arr):
    arr_len = len(arr)
    # Traverse through all array elements
    for i in range(arr_len - 1):
        # Find the min element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp


if __name__ == '__main__':
    a = np.array([4, 3, 2, 1])
    print("Unsorted Array:")
    print_array(a)

    selection_sort(a)

    print("Sorted Array:")
    print_array(a)