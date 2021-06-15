import array as arr
import numpy as np


def print_list():
    list = [1, 2, 3, 4]
    print(list)
    print(type(list))


def print_array():
    array_1 = arr.array("i", [1, 2, 3, 4, 5])
    print(array_1)
    print(type(array_1))


def print_numpy_array():
    array_2 = np.array(["numbers", 1, 2, 3, 4])
    print(array_2)
    print(type(array_2))


def print_div():
    arr1 = np.array([3, 6, 9, 12])
    div = arr1 / 3
    print(div)


def print_div2():
    arr2 = arr.array("i", [3, 6, 9, 12])
    div = arr2 / 3
    print(div)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_div2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
