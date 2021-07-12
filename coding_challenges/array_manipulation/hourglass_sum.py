def max_hourglass(a):
    max_hourglass_value = -100

    for i in range(len(a) - 2):
        for j in range(len(a[0]) - 2):
            current_max_hourglass_value = a[i][j] + a[i][j + 1] + a[i][j + 2] \
                                          + a[i + 1][j + 1] \
                                          + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
            max_hourglass_value = max(current_max_hourglass_value, max_hourglass_value)

    return max_hourglass_value


if __name__ == '__main__':
    arr = [[-9, -9, -9, 1, 1, 1],
           [0, -9, 0, 4, 3, 2],
           [-9, -9, -9, 1, 2, 3],
           [0, 0, 8, 6, 6, 0],
           [0, 0, 0, -2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    arr1 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    arr2 = [
        [0, -4, -6, 0, -7, -6],
        [-1, -2, -6, -8, -3, -1],
        [-8, -4, -2, -8, -8, -6],
        [-3, -1, -2, -5, -7, -4],
        [-3, -5, -3, -6, -6, -6],
        [-3, -6, 0, -8, -6, -7],
    ]

    print(max_hourglass(arr2))
