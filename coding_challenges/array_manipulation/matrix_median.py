"""
Given an NxM matrix in which each row is sorted,
find the overall median of the matrix.
Assume NxM is odd (tek).

ie

Matrix =
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5.

We can define a matrix as a list of lists in Python
"""


def matrix_median(A):
    if len(A) == 1:
        vec = A[0]
        return vec[len(vec)//2]
    # otherwise, if matrix has multiple rows, we loop
    else:
        new_list = []
        for row in range(len(A)):
            row.extend(A[i])