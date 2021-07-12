def recursive_factorial(nr):
    """
    5! = 1x2x3x4x5
    (n+1)! = (n+1)n!
    0! = 1
    1! = 1
    """

    if nr == 0 or nr == 1:
        return 1
    return nr * recursive_factorial(nr-1)


def iterative_factorial(nr):
    factorial = 1
    for i in range(1, nr+1):
        factorial = factorial * i

    return factorial


if __name__ == '__main__':
    print(recursive_factorial(6))
    print(iterative_factorial(5))