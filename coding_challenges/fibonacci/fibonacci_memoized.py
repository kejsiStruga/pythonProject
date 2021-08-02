"""
O(n) big-o complexity
"""


def fib_memoization(n, fib_memo):
    if n == 0 or n == 1:
        fib_memo[n] = n
    if n not in fib_memo:
        fib_memo[n] = fib_memo(n - 1, fib_memo) + fib_memo(n - 2, fib_memo)
    return fib_memo[n]


if __name__ == "__main__":
    for i in range(1, 101):
        print(i, ": ", fib_memoization(i, {}))
