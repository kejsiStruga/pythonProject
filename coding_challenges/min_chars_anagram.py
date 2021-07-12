"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters
to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and
their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' w
hich are anagrams. Two changes were necessary.
"""


def min_chars_to_anagram(s):
    if len(s) <= 1:
        return -1
    elif len(s) == 1 and s[0] != s[1]:
        return 1
    else:
        str1 = s[0:len(s) // 2]
        str2 = s[len(s) // 2:len(s)]

        str1_dict = {}
        str2_dict = {}

        for i in str1:
            if i in str1_dict:
                str1_dict[i] += 1
            else:
                str1_dict[i] = 1

        for i in str2:
            if i in str2_dict:
                str2_dict[i] += 1
            else:
                str2_dict[i] = 1

        counter = 0

        for i in str1_dict:
            si = str1_dict.get(i, 0) - str2_dict.get(i, 0)
            if si > 0:
                counter += si

        return counter


if __name__ == '__main__':
    for i in ['aaabbb', 'ab', 'abc', 'mnop', 'xyyx', 'xaxbbbxx']:
        print(min_chars_to_anagram(i))

    input2 = ['fdhlvosfpafhalll']

    print("\n")

    for i in input2:
        print(min_chars_to_anagram(i))

    for i in input2:
        print(min_chars_to_anagram(i))
