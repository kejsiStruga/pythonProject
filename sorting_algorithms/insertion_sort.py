import numpy as np


def print_array(arr):
    print(arr)


def insertion_sort(arr):
    arr_len = len(arr)

    for i in range(1, arr_len):
        print(i)
        min_el = arr[i]
        # Insert arr[i] in the sorted sequence (0 .. i-1)
        j = i - 1
        while j >= 0 and arr[j] > min_el:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = min_el


if __name__ == '__main__':
    a = np.array([4, 3, 2, 1])
    print("Unsorted Array:")
    print_array(a)

    insertion_sort(a)

    print("Sorted Array:")
    print_array(a)
