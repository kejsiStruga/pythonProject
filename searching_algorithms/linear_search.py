def linear_search(arr, element):
    if len(arr) == 0:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i] == element:
                return i
        return -1


if __name__ == "__main__":
    array = [1, 2, 5, 6, 0]
    print(linear_search(array, 5))
