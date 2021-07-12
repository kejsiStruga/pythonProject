"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters
to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and
their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' w
hich are anagrams. Two changes were necessary.
"""


def anagram(s):
    if len(s) <= 1:
        return -1
    elif len(s) == 1 and s[0] != s[1]:
        return 1
    else:
        str1 = s[0:len(s)//2]
        str2 = s[len(s)//2:len(s)]

        s1 = sorted(str1)
        s2 = sorted(str2)

        if len(str1) != len(str2):
            return -1

        counter = len(str1)

        print(type(str1))
        print(type(s1))

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                counter -= 1

        return counter


if __name__ == '__main__':
    for i in ['aaabbb', 'ab', 'abc', 'mnop', 'xyyx', 'xaxbbbxx']:
        print(anagram(i))

    input2 = ['fdhlvosfpafhalll']

    for i in input2:
        print(anagram(i))














































