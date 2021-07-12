def is_unique(s1):
    """
    Check if a string has only unique characters.
    Here we can facilitate the set() function in Python
    which will return an arr of characters of the string,
    such that no same elements exist in the set.
    => if length of the array returned by the set() function
    has same length as the string we have => it has unique
    chars and we return True

    :param s1: input string
    :return: boolean
    """
    chars = set(s1)
    if len(chars) == len(s1):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_unique("unique"))
