""""
Binary Search -> Divide-and-Conquer algorithm:
    __Divide__ - the problem into a number of subproblems that are
    smaller instances of the same problem
    __Conquer__ - the subproblems by solving them recursively. if
    they are small enough, solve the subproblems base cases
    __Combine__ - the solutions to the subproblems into the solution
    for the original problem
"""


def binary_search(arr, x, start, end):

    if start <= end:
        mid = (start+end)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, start, mid-1)
        else:
            return binary_search(arr, x, mid+1, end)
    else:
        return -1


if __name__ == "__main__":
    array = [1, 2, 5, 6]
    print(binary_search(array, 5, 0, len(array)-1))

