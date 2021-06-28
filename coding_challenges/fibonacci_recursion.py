"""
O(2^n) big-o complexity
"""


def fib(n):
    # base case: f(0) = 0 and f(1) = 1
    if n <= 1:
        return n
    # n >= 2 => f(n) = f(n-1) + f(n-2)
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(10))
