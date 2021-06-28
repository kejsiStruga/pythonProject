"""
O(n) complexity
"""


def fib_bottom_up(n):
    fib_cache = {0: 0, 1: 1}

    for j in range(2, n + 1):
        fib_cache[j] = fib_cache[j - 1] + fib_cache[j - 2]

    return fib_cache[n]


if __name__ == "__main__":
    for i in range(1, 101):
        print(i, ": ", fib_bottom_up(i))
