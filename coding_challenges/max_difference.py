"""
Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will
contain integers that represent the amount in dollars that a single stock is worth.
And return the max_profit that could have been made by buying stock on day x
and selling stock on day y such that y>x.

For example, if arr = [44, 30, 24, 32, 35, 30, 40, 38, 15] then your program
should return 16, because at index 2 the stock was worth $24 and at index 6
the stock was then worth $40, so if you bought the stock at $24 and sold it at
$40, you would have made a profit of $16, which is the max profit that could
have been made with this list of stock prices.

If there's no profit that could have been made with the stock prices, then your
program should return -1.

i.e. arr = [10, 9, 8, 2] then your program should return -1.

"""


def max_profit(a):
    min_el = a[0]
    max_diff = 0
    for i in range(len(a)):
        if a[i] < min_el:
            min_el = a[i]
        elif a[i] - min_el > max_diff:
            max_diff = a[i] - min_el

    if max_diff == 0:
        return -1
    return max_diff


if __name__ == "__main__":
    arr = [44, 30, 24, 32, 35, 30, 40, 38, 15]
    arr1 = [10, 9, 8, 1]
    print(max_profit(arr1))
    