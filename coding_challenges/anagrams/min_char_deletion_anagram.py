"""We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the
second string. In other words, both strings must contain the same exact letters in the same exact frequency. For
example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme
involving two large strings where encryption is dependent on the minimum number of character deletions required to
make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions
required to make  and  anagrams. Any characters can be deleted from either of the strings.

Example.

s1 = abc
s2 = amnop

The only characters that match are the 's so we have to remove  from  and  from  for a total of  deletions.
"""


def min_chars_deletion(s1, s2):
    s1_dict = {}
    s2_dict = {}

    for i in s1:
        if i in s1_dict:
            s1_dict[i] += 1
        else:
            s1_dict[i] = 1

    for i in s2:
        if i in s2_dict:
            s2_dict[i] += 1
        else:
            s2_dict[i] = 1

    s1_counter = 0
    s2_counter = 0

    for i in s1_dict:
        si = s1_dict.get(i, 0) - s2_dict.get(i, 0)
        if si > 0:
            s1_counter += si

    for i in s2_dict:
        si = s2_dict.get(i, 0) - s1_dict.get(i, 0)
        if si > 0:
            s2_counter += si

    return s2_counter + s1_counter
