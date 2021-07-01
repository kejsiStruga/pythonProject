"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution
, and you may not use the same elements twice.

Example:
    arr: [1, 3, 11, 2, 7]
    target: 9
    return: [3, 4]
"""


# O(n^2)
def naive_two_sum_nrs(arr, target):
    len_arr = len(arr)

    for i in range(len_arr):
        for j in range(i + 1, len_arr):
            if arr[i] + arr[j] == target:
                d = list()
                d.append(i)
                d.append(j)
    return d


# O(n)
def two_sum_nrs(arr, target):
    if len(arr) <= 1:
        return False

    d = dict()

    for i in range(len(arr)):
        if arr[i] in d:
            return [d[arr[i]], i]
        else:
            d[target - arr[i]] = i

    return d


if __name__ == '__main__':
    a = [1, 3, 11, 2, 7]
    t = 9
    print(two_sum_nrs(a, t))













