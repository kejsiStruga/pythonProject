import numpy as np


def print_array(arr):
    print(arr)


def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(1, arr_len):
        is_sorted = False
        for j in range(0, arr_len-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                is_sorted = True
        if is_sorted:
            break


if __name__ == '__main__':
    a = np.array([4, 3, 2, 1])
    print("Unsorted Array:")
    print_array(a)

    bubble_sort(a)

    print("Sorted Array:")
    print_array(a)