def array_left_rotation(a, d):
    arr_length = len(a)

    for i in range(0, d):
        for k in range(arr_length-1):
            a[k+1], a[k] = a[k], a[k+1]

    return a


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # 1 rotation -> [2, 3, 4, 5, 1]
    print(array_left_rotation(arr, 2))
