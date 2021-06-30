def is_anagram(s1, s2):
    # normalize s1 and s2 by removing spaces and lower casing them
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    """
    O(nlogn) since any comparison based algorithm
    requires at least n log n time
    """
    print(sorted(s1) == sorted(s2))


def is_anagram_optimized(s1, s2):
    # normalize s1 and s2 by removing spaces and lower casing them
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    """
    In the second, optimized approach ( O(n) ), we make use of a dictionary
    or hash table, so we are going to keep track of letters we encounter
    and make sure that once we see a letter on s1 we also have it on s2
    """

    hash_table = dict()

    if len(s1) != len(s2):
        return False

    """
    Now,  we loop through the characters of each string and keep track 
    as to what char we've encountered on each string.
    """

    for i in s1:
        if i in hash_table:
            hash_table[i] += 1
        else:  # the first time we encounter this char
            hash_table[i] = 1

    # we do same thing for s2
    for i in s2:
        if i in hash_table:
            hash_table[i] -= 1  # we want to cancel out if its same char
        else:
            hash_table[i] = 1

    for i in hash_table:
        if hash_table[i] != 0:
            return False

    return True


if __name__ == '__main__':
    s1 = "fairy tales"
    s2 = "rail safety"
    print(is_anagram_optimized(s1, s2))
















