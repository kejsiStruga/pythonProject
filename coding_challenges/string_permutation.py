def is_permutation(s1, s2):
    """
    s1 = "hello"
    s2 = "ehllo"

    => s2 is a permutation of s1

    :param s1: string 1
    :param s2: string 2
    :return: boolean
    """
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in s2:
            s2 = s2.replace(char, "")

    if len(s2) == 0:
        return True


if __name__ == '__main__':
    str1 = "driving"
    str2 = "drivighn"

    print(is_permutation(str1, str2))
