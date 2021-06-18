def fibonacci(n):
    if n <= 1:
        return n

    f = 0
    f1 = 0
    f2 = 1

    # we add +1 since range is non inclusive for 2nd element
    for i in range(2, n+1):
        f = f1 + f2
        f1, f2 = f2, f

    return f


if __name__ == '__main__':
    print(fibonacci(10))
