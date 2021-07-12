"""
O(n) big-o complexity
"""


def fib_memo(n, fib_cache):
    if n == 0 or n == 1:
        fib_cache[n] = n
    if n not in fib_cache:
        fib_cache[n] = fib_memo(n - 1, fib_cache) + fib_memo(n - 2, fib_cache)
    return fib_cache[n]


if __name__ == "__main__":
    for i in range(1, 101):
        print(i, ": ", fib_memo(i, {}))
