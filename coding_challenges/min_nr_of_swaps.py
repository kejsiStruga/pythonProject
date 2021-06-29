
def min_swaps(arr):
    swap_counter = 0

    i = 0

    while i < len(arr):
        idx = arr[i] - 1
        if arr[i] != arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            swap_counter += 1
        else:
            i += 1

    return swap_counter


if __name__ == '__main__':
    a = [4, 3, 1, 2]
    print(min_swaps(a))
