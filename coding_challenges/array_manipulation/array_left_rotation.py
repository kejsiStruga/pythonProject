def array_left_rotation(a, d):
    arr_length = len(a)

    for i in range(0, d):
        for k in range(arr_length-1):
            a[k+1], a[k] = a[k], a[k+1]

    return a


def array_left_rotation_optimized(a, d):
    rotated_array = []
    arr_length = len(a)
    rotate_idx = d

    while rotate_idx < arr_length:
        rotated_array.append(a[rotate_idx])
        rotate_idx = rotate_idx + 1

    rotate_idx = 0

    while rotate_idx < d:
        rotated_array.append(a[rotate_idx])
        rotate_idx = rotate_idx + 1

    return rotated_array


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # 1 rotation -> [2, 3, 4, 5, 1]
    print(array_left_rotation_optimized(arr, 4))
