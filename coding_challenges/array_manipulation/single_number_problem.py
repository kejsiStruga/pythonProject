"""

Given an array of integers, every element appears
twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example:
    Input: [1, 2, 2, 3, 1]
    Output: 3

"""


def single_nr_problem(arr):
    d = dict()

    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1

    for key in d:
        if d.get(key) <= 1:
            return key


if __name__ == '__main__':
    a = [1, 2, 2, 3, 1]
    print(single_nr_problem(a))






















